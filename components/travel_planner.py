import streamlit as st
import re
from utils.gemini_utils import generate_travel_itinerary
from utils.maps_utils import get_maps_link, get_directions_link

def display_travel_planner_component(city, country=None):
    """Display travel itinerary planner component"""
    st.markdown("## ✈️ Travel Itinerary Planner")
    
    # User inputs for itinerary customization
    col1, col2 = st.columns(2)
    
    with col1:
        days = st.slider("Number of days", 1, 7, 3)
    
    with col2:
        # Interest checkboxes for itinerary focus
        st.write("Travel interests:")
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            culture = st.checkbox("Culture & History", value=True)
            food = st.checkbox("Food & Dining", value=True)
        
        with col_b:
            nature = st.checkbox("Nature & Outdoors")
            shopping = st.checkbox("Shopping")
        
        with col_c:
            adventure = st.checkbox("Adventure")
            relaxation = st.checkbox("Relaxation")
    
    # Collect selected interests
    interests = []
    if culture:
        interests.append("culture and history")
    if food:
        interests.append("food and dining")
    if nature:
        interests.append("nature and outdoors")
    if shopping:
        interests.append("shopping")
    if adventure:
        interests.append("adventure")
    if relaxation:
        interests.append("relaxation")
    
    if st.button("Generate Itinerary"):
        with st.spinner(f"Creating {days}-day itinerary for {city}..."):
            itinerary = generate_travel_itinerary(city, country, days, interests)
            
            if itinerary:
                # Process the itinerary and display in a structured way
                st.markdown(f"### {days}-Day Itinerary for {city}{', ' + country if country else ''}")
                
                # Split itinerary by days
                day_pattern = r'Day (\d+)[:\s]*(.*?)(?=Day \d+|$)'
                days_content = re.findall(day_pattern, itinerary, re.DOTALL)
                
                if not days_content:
                    # If the pattern doesn't match, try an alternative pattern
                    day_pattern = r'(Day \d+)[:\s]*(.*?)(?=Day \d+|$)'
                    days_content = re.findall(day_pattern, itinerary, re.DOTALL)
                
                if days_content:
                    for i, (day_num, content) in enumerate(days_content):
                        with st.expander(f"Day {day_num if isinstance(day_num, str) else i+1}", expanded=i==0):
                            # Parse time periods (Morning, Afternoon, Evening)
                            time_periods = ["Morning", "Lunch", "Afternoon", "Dinner", "Evening"]
                            
                            for period in time_periods:
                                period_pattern = rf'{period}[:\s]*(.*?)(?=(?:{"|".join(time_periods)})|$)'
                                period_match = re.search(period_pattern, content, re.DOTALL | re.IGNORECASE)
                                
                                if period_match:
                                    period_content = period_match.group(1).strip()
                                    
                                    # Display time period heading
                                    if period == "Morning":
                                        st.markdown(f"#### 🌅 {period}")
                                    elif period == "Lunch":
                                        st.markdown(f"#### 🍽️ {period}")
                                    elif period == "Afternoon":
                                        st.markdown(f"#### ☀️ {period}")
                                    elif period == "Dinner":
                                        st.markdown(f"#### 🍷 {period}")
                                    elif period == "Evening":
                                        st.markdown(f"#### 🌙 {period}")
                                    
                                    # Extract activities or places
                                    activities = re.findall(r'[-•*]?\s*([^:\n]+)(?::|\n|$)', period_content)
                                    
                                    if activities:
                                        for activity in activities:
                                            activity = activity.strip()
                                            if activity and len(activity) > 3:  # Filter out short items
                                                maps_link = get_maps_link(activity, city, country)
                                                st.markdown(f"- **{activity}** [🗺️]({maps_link})")
                                    else:
                                        st.write(period_content)
                else:
                    # If structured parsing fails, display the raw itinerary
                    st.write(itinerary)
                
                # Offer option to download itinerary
                st.download_button(
                    label="Download Itinerary",
                    data=itinerary,
                    file_name=f"travel_itinerary_{city.lower().replace(' ', '_')}.txt",
                    mime="text/plain"
                )
            else:
                st.warning("Failed to generate itinerary. Please try again.")