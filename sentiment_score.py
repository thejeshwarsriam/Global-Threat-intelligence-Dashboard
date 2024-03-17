import pandas as pd
from textblob import TextBlob

# Load the data
df = pd.read_csv('apt_articles.csv')

# Add a new column for the sentiment score
df['sentiment_score'] = df['Content'].apply(lambda x: (TextBlob(x).sentiment.polarity + 1) / 2)


# Print the first few rows of the dataframe
print(df.head())