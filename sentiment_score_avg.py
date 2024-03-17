import pandas as pd
from textblob import TextBlob

# Load the data
df = pd.read_csv('apt_articles.csv')

# Add a new column for the sentiment score
df['sentiment_score'] = df['Content'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Add a new column for the average of sentiment_score and geo-political quotient
df['avg_sentiment_geo'] = (df['sentiment_score'] + 0.5)/2
df['avg_sentiment_geo'] = df['avg_sentiment_geo'].apply(lambda x: round(x, 1))

# Print the first few rows of the dataframe
print(df.head())

# Save the dataframe to a new csv file
df.to_csv('apt_articles_with_sentiment.csv', index=False)