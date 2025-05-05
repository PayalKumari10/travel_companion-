import streamlit as st
import os
import pycountry
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import components
from components.city_info import display_city_info_component
from components.travel_planner import display_travel_planner_component
from components.food_explorer import display_food_explorer_component
from components.budget_calculator import display_budget_calculator_component
from utils.wiki_utils import check_valid_city

# Set page configuration
st.set_page_config(
    page_title="AI Travel Companion",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load and apply CSS
with open('assets/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Main app header
st.markdown("<div class='app-header'>✈️ AI Travel Companion</div>", unsafe_allow_html=True)
st.markdown("<div class='app-subheader'>Your personal AI-powered travel guide</div>", unsafe_allow_html=True)

# Initialize session state variables if they don't exist
if 'city' not in st.session_state:
    st.session_state.city = ""
if 'country' not in st.session_state:
    st.session_state.country = ""
if 'tab_selected' not in st.session_state:
    st.session_state.tab_selected = "City Info"
if 'search_history' not in st.session_state:
    st.session_state.search_history = []

# Sidebar for city search and history
with st.sidebar:
    st.markdown("<div class='sidebar-header'>Find Your Destination</div>", unsafe_allow_html=True)
    
    # Get list of countries for dropdown
    countries = sorted([country.name for country in pycountry.countries])
    
    # City input
    city = st.text_input("City", placeholder="Enter city name")
    
    # Country dropdown (optional)
    country = st.selectbox("Country (optional)", [""] + countries)
    
    # Search button
    if st.button("Search", use_container_width=True):
        if city:
            city = city.strip().title()
            
            # Validate city
            is_valid = check_valid_city(city, country if country else None)
            
            if is_valid:
                st.session_state.city = city
                st.session_state.country = country
                
                # Add to search history if not already present
                search_term = f"{city}{', ' + country if country else ''}"
                if search_term not in st.session_state.search_history:
                    st.session_state.search_history.append(search_term)
                    # Keep only the last 5 searches
                    if len(st.session_state.search_history) > 5:
                        st.session_state.search_history.pop(0)
            else:
                st.error(f"Could not find information for {city}. Please check spelling or try another city.")
        else:
            st.warning("Please enter a city name.")
    
    # Display search history
    if st.session_state.search_history:
        st.markdown("<div class='sidebar-subheader'>Recent Searches</div>", unsafe_allow_html=True)
        for i, item in enumerate(reversed(st.session_state.search_history)):
            if st.button(item, key=f"history_{i}", use_container_width=True):
                # Parse city and country from history item
                if ", " in item:
                    city_part, country_part = item.split(", ", 1)
                    st.session_state.city = city_part
                    st.session_state.country = country_part
                else:
                    st.session_state.city = item
                    st.session_state.country = ""

    # Tab selector in sidebar
    st.markdown("<div class='sidebar-subheader'>Navigation</div>", unsafe_allow_html=True)
    tabs = ["City Info", "Travel Planner", "Food Explorer", "Budget Calculator"]
    
    for tab in tabs:
        if st.button(tab, key=f"tab_{tab}", use_container_width=True):
            st.session_state.tab_selected = tab
    
    # About section
    st.markdown("<div class='sidebar-subheader'>About</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='sidebar-about'>
    This AI Travel Companion helps you plan your perfect trip with:
    
    - City information and highlights
    - Customized travel itineraries
    - Local food recommendations
    - Budget planning assistance
    
    Created for Google Gen AI Bootcamp
    </div>
    """, unsafe_allow_html=True)

# Main content area
if st.session_state.city:
    # Display selected tab content
    if st.session_state.tab_selected == "City Info":
        display_city_info_component(st.session_state.city, st.session_state.country)
    elif st.session_state.tab_selected == "Travel Planner":
        display_travel_planner_component(st.session_state.city, st.session_state.country)
    elif st.session_state.tab_selected == "Food Explorer":
        display_food_explorer_component(st.session_state.city, st.session_state.country)
    elif st.session_state.tab_selected == "Budget Calculator":
        display_budget_calculator_component(st.session_state.city, st.session_state.country)
else:
    # Welcome screen when no city is selected
    st.markdown("<div class='welcome-header'>Welcome to your AI Travel Companion!</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='welcome-text'>
    This smart travel assistant helps you discover new destinations and plan your trips with ease.
    
    <b>How to use:</b>
    1. Enter a city name in the sidebar
    2. Optionally select a country for more accurate results
    3. Click "Search" to explore
    4. Navigate between different features using the tab buttons
    
    Get started by searching for a city in the sidebar!
    </div>
    """, unsafe_allow_html=True)
    
    # Feature highlights
    st.markdown("<div class='features-header'>Features:</div>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class='feature-card'>
            <div class='feature-icon'>🌆</div>
            <div class='feature-title'>City Info</div>
            <div class='feature-desc'>Discover city highlights, attractions, and essential tips</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='feature-card'>
            <div class='feature-icon'>✈️</div>
            <div class='feature-title'>Travel Planner</div>
            <div class='feature-desc'>Get personalized itineraries based on your interests</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='feature-card'>
            <div class='feature-icon'>🍲</div>
            <div class='feature-title'>Food Explorer</div>
            <div class='feature-desc'>Find local cuisine and dining experiences</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class='feature-card'>
            <div class='feature-icon'>💰</div>
            <div class='feature-title'>Budget Calculator</div>
            <div class='feature-desc'>Plan your travel expenses with custom estimations</div>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class='footer'>
            Created by Payal Kumari 2025 | Powered by Streamlit, Gemini AI & Wikipedia

</div>
""", unsafe_allow_html=True)