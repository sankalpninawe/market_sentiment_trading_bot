import tweepy
import json

# Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

def get_tweets(query, count=100):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    tweets = api.search(q=query, count=count)
    tweet_data = [{'text': tweet.text, 'created_at': tweet.created_at} for tweet in tweets]
    
    return tweet_data

if __name__ == "__main__":
    tweets = get_tweets('stock market')
    with open('tweets.json', 'w') as f:
        json.dump(tweets, f)
