import pandas as pd
import csv
import spacy

# Load the spaCy model for English
nlp = spacy.load('en_core_web_sm')

# Load the apt_articles.csv file
apt_articles_df = pd.read_csv('apt_articles.csv')

# Function to extract country names using spaCy NER
def extract_country_names(text):
    doc = nlp(text)
    countries = [ent.text for ent in doc.ents if ent.label_ == 'GPE']
    return countries

# Apply the function to the 'Content' column, processing each paragraph individually
country_lists = []
for content in apt_articles_df['Content']:
    paragraphs = content.split('\n')  # Assuming paragraphs are separated by newline characters
    country_names = []
    for paragraph in paragraphs:
        country_names.extend(extract_country_names(paragraph))
    country_lists.append(country_names)

# Add extracted country names to the DataFrame
apt_articles_df['Countries'] = country_lists

# Flatten the list of country names
apt_articles_df['Countries'] = apt_articles_df['Countries'].apply(lambda x: ', '.join(x))

# Save the extracted country names to a different CSV file
output_csv = 'extracted_countries.csv'
apt_articles_df.to_csv(output_csv, columns=['Countries'], index=False, quoting=csv.QUOTE_NONNUMERIC)

print(f"Extracted country names have been saved to {output_csv}.")