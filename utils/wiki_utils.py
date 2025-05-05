import wikipedia
import requests

def get_city_description(city, country=None):
    """
    Get a brief description of the city from Wikipedia
    """
    search_term = f"{city}, {country}" if country else city
    
    try:
        # Try with the full search term first
        summary = wikipedia.summary(search_term, sentences=5, auto_suggest=False)
        return summary
    except wikipedia.DisambiguationError as e:
        # If disambiguation is needed, use the first option
        try:
            summary = wikipedia.summary(e.options[0], sentences=5, auto_suggest=False)
            return summary
        except:
            # If that fails, try just the city name
            try:
                if country:
                    summary = wikipedia.summary(city, sentences=5, auto_suggest=False)
                    return summary
                else:
                    return "Couldn't find a proper description for this city."
            except:
                return "Couldn't find a proper description for this city."
    except Exception as e:
        # For any other exception
        try:
            if country:
                summary = wikipedia.summary(city, sentences=5, auto_suggest=False)
                return summary
            else:
                return f"Couldn't find a proper description for this city. Error: {str(e)}"
        except:
            return f"Couldn't find a proper description for this city. Error: {str(e)}"

def get_city_image(city, country=None):
    """
    Attempt to get a representative image of the city from Wikipedia
    """
    search_term = f"{city}, {country}" if country else city
    
    try:
        # First try to get the Wikipedia page
        page = wikipedia.page(search_term, auto_suggest=False)
        
        # If found, get the images
        if page and page.images:
            # Filter for jpg or png images
            images = [img for img in page.images if img.lower().endswith(('.jpg', '.jpeg', '.png'))]
            if images:
                return images[0]  # Return the first image URL
        
        # If no page found for city + country, try just city
        if country:
            try:
                page = wikipedia.page(city, auto_suggest=False)
                if page and page.images:
                    images = [img for img in page.images if img.lower().endswith(('.jpg', '.jpeg', '.png'))]
                    if images:
                        return images[0]
            except:
                pass
                
        return None
    except:
        return None

def check_valid_city(city, country=None):
    """
    Check if the entered city (and optional country) is valid by attempting to find it on Wikipedia
    """
    search_term = f"{city}, {country}" if country else city
    
    try:
        # See if Wikipedia has a page for this city
        results = wikipedia.search(search_term, results=5)
        if not results:
            return False
        
        # Check if any of the search results contain the city name
        city_lower = city.lower()
        for result in results:
            if city_lower in result.lower():
                return True
                
        return False
    except:
        return False