import tweepy
from jsonmerge import merge
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

	number_of_tweets = 2
	count = 1

	finalJson = None
	firstIteration = True
	lastIteration = False



	for tweet in tweepy.Cursor(api.search,q="#phulwama",lang="en").items():
    	    if count > number_of_tweets:
    	    	break
    	    if count == number_of_tweets:
    	    	lastIteration = True
    	    count = count+1
    	    str = tweet._json     #this is a dictionary
    	    json_string = json.dumps(str) #this is a json string

    	    if firstIteration:
    	    	finalJson="["+json_string+","
    	    	firstIteration = False

    	    elif lastIteration:
    	    	finalJson = finalJson + json_string+"]"
    	    	lastIteration = True

    	    else:
    	    	finalJson = finalJson + json_string+","
		
	#print(finalJson)
	js = json.loads(finalJson)
	with open('tweets.json','w') as outf:
		json.dump(js,outf,indent = 4)	