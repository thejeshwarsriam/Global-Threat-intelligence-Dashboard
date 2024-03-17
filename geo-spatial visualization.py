import pandas as pd
import spacy
from geopy.geocoders import Nominatim
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the spaCy model for English
nlp = spacy.load('en_core_web_sm')

# Read the extracted-countries.csv file
extracted_countries_df = pd.read_csv('extracted_countries.csv')

# Function to extract country names using spaCy NER
def extract_country_names(text):
    doc = nlp(text)
    countries = [ent.text for ent in doc.ents if ent.label_ == 'GPE']
    return countries

# Apply the function to the 'Countries' column
extracted_countries_df['Countries'] = extracted_countries_df['Countries'].apply(extract_country_names)

# Flatten the list of country names
extracted_countries = extracted_countries_df['Countries'].explode().dropna().unique().tolist()

# Use GeoPy to get the coordinates of the countries
geolocator = Nominatim(user_agent="country_locator")
country_coordinates = {}
for country_name in extracted_countries:
    location = geolocator.geocode(country_name)
    if location:
        country_coordinates[country_name] = (location.latitude, location.longitude)

# Plot the countries on a world map using GeoPandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
for country_name, coordinates in country_coordinates.items():
    country = world[world['name'] == country_name]
    if not country.empty:
        fig, ax = plt.subplots(figsize=(10, 6))
        world.plot(ax=ax, color='lightgray')
        country.plot(ax=ax, color='blue', edgecolor='black')
        ax.set_title(f'Country: {country_name}')
        ax.annotate(country_name, xy=coordinates, xytext=(coordinates[0] + 5, coordinates[1] + 5),
                    arrowprops=dict(facecolor='black', shrink=0.05))
        plt.show()
    else:
        print(f"Country '{country_name}' not found in the world dataset.")
