__author__ = "Akki"
import tweepy
from textblob import TextBlob

consumer_key = "FjydQtt0yMcvy6Uv6iAxUIC8f"
consumer_secret = "34q62rYJGFC97vbL7Gh2Z5HVRQOVotKinaEuACEzbZ4o52LX0R"

access_token = "1914203616-9vg2pHtwGSAP3rLsZXzzEjEiLA8S9TeujcBwLwA"
access_token_secret = "oOO5Jminmm8gTRXTPL4iuvGuA63qA14f6UQ3jDfKc6rmW"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("Trump")

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
