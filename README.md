# AI Travel Companion

An AI-powered travel assistant built with Streamlit, Google's Gemini API, and Wikipedia. This application helps users explore destinations, plan itineraries, discover local cuisine, and estimate travel budgets.

![AI Travel Companion Screenshot](screenshot.png)

## Features

- **City Information**: Get detailed information about destinations, including attractions, local tips, and essential visitor information.
- **Travel Planner**: Generate customized travel itineraries based on the number of days and personal interests.
- **Food Explorer**: Discover local cuisine, food experiences, and learn essential dining phrases.
- **Budget Calculator**: Estimate travel expenses based on your trip duration and preferred travel style.
- **Interactive Interface**: User-friendly design with Google Maps integration for locations.

## Technologies Used

- **Streamlit**: Web app framework for building the interactive UI
- **Google Gemini API**: AI model for generating travel recommendations and information
- **Wikipedia API**: For fetching city descriptions and information
- **Plotly**: For data visualization (budget charts)
- **Python**: Core programming language

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/travel-companion.git
cd travel-companion
```

2. Create a virtual environment and activate it:
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

5. Run the application:
```bash
streamlit run app.py
```

## Usage

1. Enter a city name (and optionally a country) in the sidebar.
2. Click "Search" to load information about the destination.
3. Navigate between different features using the tab buttons in the sidebar.
4. Explore the city information, generate itineraries, discover local food, and calculate your budget.
5. Download itineraries and budget estimates for offline use.

## Project Structure

```
travel_companion/
├── app.py               # Main Streamlit application
├── requirements.txt     # Dependencies
├── utils/               # Utility functions
│   ├── gemini_utils.py  # Functions for Gemini API integration
│   ├── wiki_utils.py    # Functions for Wikipedia data
│   └── maps_utils.py    # Functions for Google Maps integration
├── components/          # UI components
│   ├── city_info.py     # City information component
│   ├── travel_planner.py # Travel itinerary planner component
│   ├── food_explorer.py  # Local cuisine explorer component
│   └── budget_calculator.py # Travel budget calculator component
├── assets/              # Static assets
│   └── style.css        # Custom CSS styles
└── README.md            # Project documentation
```

## Future Enhancements

- User accounts and saved trips
- Offline mode for downloaded itineraries
- Weather forecast integration
- Public transportation information
- Photo gallery for destinations

## Created For

Google Gen AI Bootcamp project submission

## License

This project is licensed under the MIT License - see the LICENSE file for details.