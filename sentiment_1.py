import tweepy
from textblob import TextBlob

consumer_key = 'ks2wNuhkWiWCGsuQ2b1OMM7a8'
consumer_secret = '1T2ziC6QCvqX9dXxWryk9jI1gMXC3rULwUIMR9ow9sxd3W0uyd'
access_token = '170800208-IJwxY0fh5iagSbCPXxrV5v8NCNWiNtQMLSPGZ2Rm'
access_token_secret = 'J2gKmvAnOxCaA9gu4ajn2jhI0X9E5LXjjPQfxE03iyzpc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

public_tweets = api.search('Tim Cook')
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	print('\n')