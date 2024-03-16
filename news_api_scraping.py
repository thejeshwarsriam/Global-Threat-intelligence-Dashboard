from newsapi import NewsApiClient
import csv

# Initialize News API client with your API key
newsapi = NewsApiClient(api_key='8abe6ae1ee464f4f8e407251aadd44ea')

# Fetch news articles related to India's APT groups
articles = newsapi.get_everything(q='India APT groups', language='en', page_size=100)

# Extract relevant information from articles
apt_articles = []
for article in articles['articles']:
    title = article['title']
    source = article['source']['name']
    published_at = article['publishedAt']
    content = article['content']
    apt_articles.append({'Title': title, 'Source': source, 'Published At': published_at, 'Content': content})

# Save data to a CSV file
csv_file = 'apt_articles.csv'
fieldnames = ['Title', 'Source', 'Published At', 'Content']
with open(csv_file, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for article in apt_articles:
        writer.writerow(article)

print(f"News articles related to India's APT groups have been saved to {csv_file}.")
