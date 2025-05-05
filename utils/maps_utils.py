import urllib.parse

def get_maps_link(place, city=None, country=None):
    """
    Generate a Google Maps search link for a place
    """
    if city and country:
        query = urllib.parse.quote(f"{place} {city} {country}")
    elif city:
        query = urllib.parse.quote(f"{place} {city}")
    else:
        query = urllib.parse.quote(place)
        
    return f"https://www.google.com/maps/search/?api=1&query={query}"

def get_maps_embed_html(place, city=None, country=None, width=600, height=450):
    """
    Generate HTML for embedding Google Maps for a place
    """
    if city and country:
        query = urllib.parse.quote(f"{place} {city} {country}")
    elif city:
        query = urllib.parse.quote(f"{place} {city}")
    else:
        query = urllib.parse.quote(place)
        
    embed_url = f"https://www.google.com/maps/embed/v1/place?key=YOUR_API_KEY&q={query}"
    
    html = f"""
    <div style="width: 100%; max-width: {width}px; margin: 0 auto;">
        <iframe 
            width="100%" 
            height="{height}" 
            frameborder="0" 
            style="border:0" 
            src="{embed_url}" 
            allowfullscreen>
        </iframe>
    </div>
    """
    
    return html

def get_directions_link(origin, destination):
    """
    Generate a Google Maps directions link between two places
    """
    origin_encoded = urllib.parse.quote(origin)
    destination_encoded = urllib.parse.quote(destination)
    
    return f"https://www.google.com/maps/dir/?api=1&origin={origin_encoded}&destination={destination_encoded}"