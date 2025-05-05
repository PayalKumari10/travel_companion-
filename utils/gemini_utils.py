import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_travel_info(city, country=None):
    """
    Get travel information about a city using Gemini API
    """
    location = f"{city}, {country}" if country else city
    
    prompt = f"""Provide concise travel details for {location} including:
    1. Three famous places to visit with a brief one-line description for each
    2. Three popular local foods with a brief one-line description for each
    3. Three recommended restaurants with cuisine type for each
    4. Three shopping areas or malls with what they're known for
    5. Best time to visit and brief weather information
    6. Two local cultural tips or etiquette to be aware of

    Format as bullet points for each category.
    """
    
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

def generate_travel_itinerary(city, country=None, days=3, interests=None):
    """
    Generate a travel itinerary for the specified number of days
    """
    location = f"{city}, {country}" if country else city
    interests_prompt = f" with focus on {', '.join(interests)}" if interests else ""
    
    prompt = f"""Create a detailed {days}-day travel itinerary for {location}{interests_prompt}.
    For each day include:
    - Morning activities (1-2 activities)
    - Lunch recommendation (1 restaurant or food place)
    - Afternoon activities (1-2 activities)
    - Dinner recommendation (1 restaurant or food place)
    - Evening activity (1 optional activity)

    Format the itinerary day by day with clear headings and organize each day's schedule by time period.
    Include a brief one-line description for each place or activity.
    """
    
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

def get_local_phrases(city, country=None):
    """
    Get common local phrases and their meanings
    """
    location = f"{city}, {country}" if country else city
    
    prompt = f"""Provide 5 useful everyday phrases or expressions in the local language of {location}.
    For each phrase include:
    1. The phrase in the local language
    2. Pronunciation guide (in simple phonetics)
    3. English translation
    4. When to use this phrase

    Format as a numbered list with clear separations between each phrase.
    """
    
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

def get_budget_estimation(city, country=None, trip_days=3, travel_style="mid-range"):
    """
    Get budget estimation for the trip
    """
    location = f"{city}, {country}" if country else city
    
    prompt = f"""Create a detailed travel budget estimation for a {trip_days}-day trip to {location} for a {travel_style} style traveler (options: budget, mid-range, luxury).
    
    Include average costs for:
    1. Accommodation (per night)
    2. Meals (breakfast, lunch, dinner)
    3. Local transportation
    4. Attractions/activities
    5. Shopping/souvenirs (optional)
    
    Provide costs in both local currency and USD equivalent.
    Also include an estimated total budget for the entire {trip_days}-day trip.
    """
    
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

def get_travel_tips(city, country=None):
    """
    Get travel tips and safety information
    """
    location = f"{city}, {country}" if country else city
    
    prompt = f"""Provide essential travel tips for visitors to {location}, including:
    
    1. Safety tips (2-3 points)
    2. Transportation tips (2-3 points)
    3. Weather and packing advice (2-3 points)
    4. Money and payment information (2-3 points)
    5. Local customs to be aware of (2-3 points)
    
    Format as bullet points under clear headings.
    """
    
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text