import streamlit as st
import re
import plotly.graph_objects as go
from utils.gemini_utils import get_budget_estimation

def display_budget_calculator_component(city, country=None):
    """Display travel budget calculator component"""
    st.markdown("## 💰 Travel Budget Calculator")
    
    # User inputs for budget customization
    col1, col2 = st.columns(2)
    
    with col1:
        days = st.slider("Number of days", 1, 14, 3, key="budget_days")
    
    with col2:
        travel_style = st.selectbox(
            "Travel style", 
            ["Budget", "Mid-range", "Luxury"],
            index=1,
            key="travel_style"
        )
    
    if st.button("Calculate Budget"):
        with st.spinner(f"Estimating travel budget for {city}..."):
            budget_info = get_budget_estimation(city, country, days, travel_style.lower())
            
            if budget_info:
                st.markdown(f"### Travel Budget for {days} days in {city}{', ' + country if country else ''}")
                st.markdown(f"*Travel style: {travel_style}*")
                
                # Process and display the budget information
                # Parse expense categories and costs
                categories = ["Accommodation", "Food", "Transportation", "Activities", "Shopping"]
                costs = {}
                
                # Extract costs using regex
                for category in categories:
                    pattern = rf'{category}.*?(\$\d+(?:-\$\d+)?|\d+(?:-\d+)?\s*\$)'
                    matches = re.findall(pattern, budget_info, re.IGNORECASE)
                    
                    if matches:
                        # Extract the first number for visualization
                        cost_str = matches[0]
                        # Extract just the numeric part
                        num_match = re.search(r'(\d+)', cost_str)
                        if num_match:
                            costs[category] = int(num_match.group(1))
                    else:
                        costs[category] = 0
                
                # Extract total budget
                total_pattern = r'total.*?(\$\d+(?:-\$\d+)?|\d+(?:-\d+)?\s*\$)'
                total_matches = re.findall(total_pattern, budget_info, re.IGNORECASE)
                
                if total_matches:
                    total_str = total_matches[0]
                    total_match = re.search(r'(\d+)', total_str)
                    if total_match:
                        total_budget = int(total_match.group(1))
                    else:
                        total_budget = sum(costs.values())
                else:
                    total_budget = sum(costs.values())
                
                # Display the detailed breakdown and the raw budget info
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    # Display the raw budget information
                    st.markdown("#### Budget Breakdown")
                    st.write(budget_info)
                
                with col2:
                    # Create a pie chart of the budget
                    if any(costs.values()):
                        fig = go.Figure(data=[go.Pie(
                            labels=list(costs.keys()),
                            values=list(costs.values()),
                            hole=.3,
                            marker_colors=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#c5b0d5']
                        )])
                        
                        fig.update_layout(
                            title_text=f"Budget Distribution",
                            showlegend=True,
                            height=400,
                            margin=dict(l=20, r=20, t=40, b=20)
                        )
                        
                        st.plotly_chart(fig, use_container_width=True)
                    
                    # Display total budget prominently
                    st.markdown(f"#### Estimated Total: ${total_budget}")
                
                # Add money-saving tips
                st.markdown("#### 💡 Money-Saving Tips")
                
                tips = [
                    f"Book accommodations outside the main tourist areas in {city} for better rates.",
                    "Use public transportation instead of taxis when possible.",
                    "Look for free or discounted museum days.",
                    "Eat where locals eat for authentic and often cheaper meals.",
                    "Consider getting a city pass if you plan to visit multiple attractions."
                ]
                
                for tip in tips:
                    st.markdown(f"- {tip}")
                
                # Add download button for budget
                st.download_button(
                    label="Download Budget Estimate",
                    data=f"Travel Budget for {days} days in {city}{', ' + country if country else ''}\n" + 
                         f"Travel style: {travel_style}\n\n" + budget_info + 
                         f"\n\nTotal Estimated Budget: ${total_budget}",
                    file_name=f"travel_budget_{city.lower().replace(' ', '_')}.txt",
                    mime="text/plain"
                )
            else:
                st.warning("Failed to estimate budget. Please try again.")