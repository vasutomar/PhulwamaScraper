import tweepy
import json
import wget
import csv
import networkx as nx

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

	g = nx.Graph()
	g.add_edge(1,2)

	nx.write_adjlist(g,'vasu')	
			
