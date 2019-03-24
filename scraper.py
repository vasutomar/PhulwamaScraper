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

	regular_tweet_count = 0
	multimedia_tweets_count = 0
	totalCount = 0

	finalJson = "["
	finalMultimediaJson = "["

	firstIteration = True
	lastIteration = False

	hashtag_List = ["#phulwama","#phulwamaterrorattack","#SurgicalStrike2","#PhulwamaMartyrs","#crpfmartyrs","#BalakotAirstrikes","#IndiaStrikesBack","#PulwamaTerroristAttack","#CRPF","#Balakot"]
	testHashtag = ['#testingofscraper']

	print("Exracting tweets")

	iteration = 0
	for i in range(len(hashtag_List)):
		hashtag = hashtag_List[i]
		print("Processing "+hashtag)
		multimedia_tweets_count = 1
		totalCount = 0
		for tweet in tweepy.Cursor(api.search,q=hashtag,lang="en").items():
			if multimedia_tweets_count>=10:
				break

			if totalCount>=50:
				break

			str = tweet._json
			entity = str['entities']

			json_string = json.dumps(str)

			#print("total tweet count - ",totalCount)
			totalCount+=1

			if 'media' not in entity:
				#print("regular tweet count = ",regular_tweet_count)
				finalJson = finalJson+json_string+","
				regular_tweet_count+=1
			else:
				print("multimedia tweet count",multimedia_tweets_count)
				finalMultimediaJson = finalMultimediaJson+json_string+","
				multimedia_tweets_count+=1
	
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

	allTweetGraph = nx.Graph()
	mulTweetGraph = nx.Graph()

	tweetFile = open('tweets.json','r')
	multiFile = open('multimedia.json','r')

	tweets = json.load(tweetFile)
	multim = json.load(multiFile)

	#Adding all nodes in normal graph
	for tweet in tweets:
		userEntity = tweet['user']
		username = userEntity['name']
		allTweetGraph.add_node(username)

	for mtweet in multim:
		userEntity = mtweet['user']
		username = userEntity['name']
		mulTweetGraph.add_node(username)

	nx.write_adjlist(allTweetGraph,"allTweetGraph")
	nx.write_adjlist(mulTweetGraph,"multimediaTweetGraph")


