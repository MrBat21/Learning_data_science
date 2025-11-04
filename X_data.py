import tweepy
from textblob import TextBlob

bearer_token = "AAAAAAAAAAAAAAAAAAAAAAgZ5QEAAAAA%2BSq1JKiDXBEw11ksZSOds7M5tWk%3DN87dWvuVUs5pnuLRM9EHWqvecurzPHCWiw9eDHotPbIIwbUuQH"

client = tweepy.Client(bearer_token=bearer_token)

# Exact keyword search
query = "Vini.Jr"

#Fetch recent tweets
tweets = client.search_recent_tweets(query=query, max_results=10, tweet_fields=['text','author_id','created_at'])

for tweet in tweets.data:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)