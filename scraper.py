import tweepy
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

	number_of_tweets = 100
	totalCount = 1

	finalJson = "["
	finalMultimediaJson = "["

	firstIteration = True
	lastIteration = False

	hashtag_List = ["#phulwama","#phulwamaterrorattack","#SurgicalStrike2","#PhulwamaMartyrs","#crpfmartyrs","#PulwamaTerroristAttack"]
	testHashtag = ['#testingofscraper']

	print("Exracting tweets")

	iteration = 0
	for i in range(len(hashtag_List)):
		hashtag = hashtag_List[i]
		print("Processing "+hashtag)
		multimedia_tweets_count = 1
		for tweet in tweepy.Cursor(api.search,q=hashtag,lang="en").items():
			if multimedia_tweets_count>=10000:
				break
			str = tweet._json
			entity = str['entities']

			json_string = json.dumps(str)

			if 'media' not in entity:
				finalJson = finalJson+json_string+","
			else:
				finalMultimediaJson = finalMultimediaJson+json_string+","
				multimedia_tweets_count+=1

	#print(finalJson)
	#print(totalCount)
	
	finalJson = finalJson[:-1]
	finalMultimediaJson = finalMultimediaJson[:-1]

	finalJson = finalJson+"]"
	finalMultimediaJson = finalMultimediaJson+"]"

	#testFile = open('test.json','w')
	#testFile.write(finalJson)
	js = json.loads(finalJson)
	mul_js = json.loads(finalMultimediaJson)

	with open('multimedia.json','w') as outf:
		json.dump(mul_js,outf,indent = 4)

	with open('tweets.json','w') as outf:
		json.dump(js,outf,indent = 4)
