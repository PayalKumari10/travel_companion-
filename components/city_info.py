import streamlit as st
from utils.wiki_utils import get_city_description, get_city_image
from utils.gemini_utils import get_travel_info
from utils.maps_utils import get_maps_link
import re

def display_city_info_component(city, country=None):
    """Display city information component"""
    st.markdown("## 🌆 City Overview")
    
    # Get city description from Wikipedia
    description = get_city_description(city, country)
    
    # Get city image
    image_url = get_city_image(city, country)
    
    # Display city image and description in columns
    col1, col2 = st.columns([1, 2])
    
    with col1:
        if image_url:
            st.image(image_url, caption=f"{city}{', ' + country if country else ''}", use_column_width=True)
        else:
            st.info(f"No image found for {city}")
    
    with col2:
        if description:
            st.markdown(f"### About {city}{', ' + country if country else ''}")
            st.write(description)
        else:
            st.warning(f"No information found for {city}")
        
        # Add direct link to Google Maps
        location_text = f"{city}{', ' + country if country else ''}"
        maps_link = get_maps_link(city, country=country)
        st.markdown(f"[View {location_text} on Google Maps]({maps_link})")
    
    # Get and display travel information using Gemini
    st.markdown("## 🧳 Travel Information")
    
    with st.spinner("Generating travel information..."):
        travel_info = get_travel_info(city, country)
        
        if travel_info:
            # Parse the travel information to display in an organized way
            sections = re.split(r'(?:\d+\.\s+|\*\*|##)', travel_info)
            sections = [s.strip() for s in sections if s.strip()]
            
            # Display in tabs
            if len(sections) >= 5:
                tab1, tab2, tab3, tab4, tab5 = st.tabs(["Places to Visit", "Local Foods", "Restaurants", "Shopping", "Travel Tips"])
                
                with tab1:
                    st.markdown("### 🏛️ Famous Places to Visit")
                    places_section = next((s for s in sections if "place" in s.lower() or "visit" in s.lower()), "")
                    if places_section:
                        places = re.findall(r'[-•*]\s*([^:]+)(?::|\n|$)', places_section)
                        for place in places:
                            place = place.strip()
                            if place:
                                maps_link = get_maps_link(place, city, country)
                                st.markdown(f"- **{place}** [🗺️]({maps_link})")
                    else:
                        st.write("No information about places to visit.")
                
                with tab2:
                    st.markdown("### 🍽️ Local Foods")
                    foods_section = next((s for s in sections if "food" in s.lower() or "cuisine" in s.lower()), "")
                    if foods_section:
                        foods = re.findall(r'[-•*]\s*([^:]+)(?::|\n|$)', foods_section)
                        for food in foods:
                            st.markdown(f"- **{food.strip()}**")
                    else:
                        st.write("No information about local foods.")
                
                with tab3:
                    st.markdown("### 🍴 Recommended Restaurants")
                    restaurants_section = next((s for s in sections if "restaurant" in s.lower()), "")
                    if restaurants_section:
                        restaurants = re.findall(r'[-•*]\s*([^:]+)(?::|\n|$)', restaurants_section)
                        for restaurant in restaurants:
                            restaurant = restaurant.strip()
                            if restaurant:
                                maps_link = get_maps_link(restaurant, city, country)
                                st.markdown(f"- **{restaurant}** [🗺️]({maps_link})")
                    else:
                        st.write("No information about restaurants.")
                
                with tab4:
                    st.markdown("### 🛍️ Shopping Areas")
                    shopping_section = next((s for s in sections if "shop" in s.lower() or "mall" in s.lower()), "")
                    if shopping_section:
                        shops = re.findall(r'[-•*]\s*([^:]+)(?::|\n|$)', shopping_section)
                        for shop in shops:
                            shop = shop.strip()
                            if shop:
                                maps_link = get_maps_link(shop, city, country)
                                st.markdown(f"- **{shop}** [🗺️]({maps_link})")
                    else:
                        st.write("No information about shopping areas.")
                
                with tab5:
                    st.markdown("### ⚠️ Travel Tips")
                    tips_section = next((s for s in sections if "time" in s.lower() or "weather" in s.lower() or "tip" in s.lower()), "")
                    if tips_section:
                        st.write(tips_section)
                    else:
                        st.write("No travel tips available.")
            else:
                st.write(travel_info)
        else:
            st.warning("Failed to generate travel information. Please try again.")