import tweepy
from tweepy import OAuthHandler
import json
import wget
import csv

#Twitter Authentication
with open('twitter_credentials.json') as cred_data:
	info = json.load(cred_data)

	consumer_key = info['CONSUMER_KEY']
	consumer_secret = info['CONSUMER_SECRET']
	access_token = info['ACCESS_KEY']
	access_secret = info['ACCESS_SECRET']

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth,wait_on_rate_limit=True)

	data={}

	for tweet in tweepy.Cursor(api.search,q="#phulwama",count=2,lang="en").items():
    	    str = tweet._json
    	    with open('tweets.json','a') as outfile:
    	    	json.dump(str,outfile, indent = 4)
