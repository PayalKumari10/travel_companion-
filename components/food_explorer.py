import streamlit as st
import re
import random
from utils.gemini_utils import get_local_phrases
from utils.maps_utils import get_maps_link

def display_food_explorer_component(city, country=None):
    """Display local cuisine explorer component"""
    st.markdown("## 🍲 Local Cuisine Explorer")
    
    # Create tabs for different food experiences
    tab1, tab2, tab3 = st.tabs(["Must-Try Foods", "Food Experiences", "Language Guide"])
    
    with tab1:
        st.markdown("### Must-Try Local Dishes")
        
        # Use Gemini to get information about local cuisine
        with st.spinner("Finding local cuisine information..."):
            # Generate prompts to get food information
            prompt = f"""
            Provide detailed information about 5 must-try local dishes in {city}{', ' + country if country else ''}.
            For each dish include:
            1. The dish name
            2. Brief description (2-3 sentences)
            3. Main ingredients
            4. Where to find it (specific restaurant or area)
            5. Approximate price range
            
            Format the response as:
            
            **Dish Name**
            Description: [description]
            Ingredients: [ingredients]
            Where to find: [location]
            Price range: [price]
            """
            
            # This would normally use the Gemini API, but for now we'll simulate the response
            # Replace this with actual API call in your implementation
            
            # Simulated response for demonstration
            simulated_dishes = [
                {
                    "name": f"Signature Dish of {city} 1",
                    "description": "This is a traditional dish with rich flavors and history. Often served during special occasions.",
                    "ingredients": "Local ingredients specific to the region",
                    "location": f"Popular Restaurant in {city} 1",
                    "price": "$$ (10-15 USD)"
                },
                {
                    "name": f"Signature Dish of {city} 2",
                    "description": "A street food favorite among locals and tourists alike. Known for its unique combination of flavors.",
                    "ingredients": "Fresh local produce and spices",
                    "location": f"Street Food Area in {city}",
                    "price": "$ (5-8 USD)"
                },
                {
                    "name": f"Signature Dish of {city} 3",
                    "description": "A hearty meal that represents the culinary tradition of the region. Often eaten as a main course.",
                    "ingredients": "Regional specialties and seasonal ingredients",
                    "location": f"Local Market Area in {city}",
                    "price": "$$ (12-18 USD)"
                }
            ]
            
            # Display dishes in an attractive format
            for dish in simulated_dishes:
                col1, col2 = st.columns([1, 3])
                
                with col1:
                    # Display food emoji randomly
                    food_emojis = ["🍲", "🍛", "🍜", "🍝", "🍱", "🍚", "🍤", "🍗", "🥘", "🌮", "🌯", "🍔", "🥗"]
                    st.markdown(f"### {random.choice(food_emojis)}")
                
                with col2:
                    st.markdown(f"### {dish['name']}")
                    st.write(dish['description'])
                    st.markdown(f"**Ingredients:** {dish['ingredients']}")
                    
                    maps_link = get_maps_link(dish['location'], city, country)
                    st.markdown(f"**Where to find:** [{dish['location']}]({maps_link})")
                    
                    st.markdown(f"**Price range:** {dish['price']}")
                
                st.markdown("---")
    
    with tab2:
        st.markdown("### Food Tours & Experiences")
        
        # Display food tour options
        st.markdown("""
        #### Recommended Food Experiences
        
        Here are some food-related activities you might enjoy:
        """)
        
        # Food experiences cards
        food_experiences = [
            {
                "title": f"Street Food Tour in {city}",
                "description": "Discover hidden local gems and popular street food stalls with a knowledgeable guide.",
                "duration": "3-4 hours",
                "price_range": "$ (25-45 USD per person)"
            },
            {
                "title": "Cooking Class",
                "description": f"Learn to prepare authentic dishes from {city} with a local chef in a hands-on cooking class.",
                "duration": "4-5 hours",
                "price_range": "$$ (50-80 USD per person)"
            },
            {
                "title": "Food & Culture Walking Tour",
                "description": f"Explore the cultural heritage of {city} through its food traditions and historical sites.",
                "duration": "5-6 hours",
                "price_range": "$ (35-60 USD per person)"
            }
        ]
        
        for i, exp in enumerate(food_experiences):
            col1, col2 = st.columns([1, 3])
            
            with col1:
                food_icons = ["🍳", "🥂", "🍴", "👨‍🍳", "🧆", "🥙"]
                st.markdown(f"### {food_icons[i % len(food_icons)]}")
            
            with col2:
                st.markdown(f"### {exp['title']}")
                st.write(exp['description'])
                st.markdown(f"**Duration:** {exp['duration']}")
                st.markdown(f"**Price range:** {exp['price_range']}")
            
            st.markdown("---")
    
    with tab3:
        st.markdown("### Food & Dining Language Guide")
        
        # Get local phrases related to food and dining
        with st.spinner("Generating useful local phrases..."):
            phrases = get_local_phrases(city, country)
            
            if phrases:
                # Display phrases in a nicely formatted way
                st.markdown("#### Essential phrases for ordering food and dining")
                st.write("These phrases will help you navigate restaurants and food markets:")
                
                # Parse the phrases and display them
                phrase_pattern = r'(\d+)[.)]?\s+([^\n]+)'
                matches = re.findall(phrase_pattern, phrases, re.DOTALL)
                
                if matches:
                    for _, phrase_block in matches:
                        lines = phrase_block.strip().split('\n')
                        if lines and len(lines) >= 2:
                            local_phrase = lines[0].strip()
                            
                            # Check if there's pronunciation info
                            pronunciation = ""
                            translation = ""
                            usage = ""
                            
                            for line in lines[1:]:
                                line = line.strip()
                                if "pronunciation" in line.lower():
                                    pronunciation = line
                                elif "translation" in line.lower():
                                    translation = line
                                elif "use" in line.lower():
                                    usage = line
                            
                            st.markdown(f"##### *\"{local_phrase}\"*")
                            if pronunciation:
                                st.write(pronunciation)
                            if translation:
                                st.write(translation)
                            if usage:
                                st.write(usage)
                            
                            st.markdown("---")
                else:
                    # If pattern matching fails, just display the raw text
                    st.write(phrases)
            else:
                st.warning("Could not generate local phrases. Please try again.")