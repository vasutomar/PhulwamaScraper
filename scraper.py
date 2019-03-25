import tweepy
import json
import wget
import csv
import networkx as nx

info = None

def authenticate():
	with open('twitter_credentials.json') as cred_data:
		info = json.load(cred_data)

	consumer_key = info['CONSUMER_KEY']
	consumer_secret = info['CONSUMER_SECRET']
	access_token = info['ACCESS_KEY']
	access_secret = info['ACCESS_SECRET']

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth,wait_on_rate_limit=True)

	return api

def extractTweets(api):
	regular_tweet_count = 0
	multimedia_tweets_count = 0
	totalCount = 0
	
	finalJson = "["
	finalMultimediaJson = "["
	
	firstIteration = True
	lastIteration = False

	hashtag_List = ["#phulwama","#phulwamaterrorattack","#SurgicalStrike2","#PhulwamaMartyrs","#crpfmartyrs","#BalakotAirstrikes","#IndiaStrikesBack","#PulwamaTerroristAttack","#CRPF","#Balakot"]
	hashtag_List2 = ['#testingofscraper']

	print("Exracting tweets")
	multimedia_tweets_count = 1

	iteration = 0

	for i in range(len(hashtag_List)):
		hashtag = hashtag_List[i]
		print("Processing"+hashtag)
		totalCount = 0
		for tweet in tweepy.Cursor(api.search,q=hashtag,lang="en",tweet_mode = "extended").items():
			if totalCount>=1000:
				break
		str = tweet._json
		entity = str['entities']

		json_string = json.dumps(str)
		print("total tweet count  ",totalCount)
		totalCount+=1

		if 'media' not in entity:
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

	js = json.loads(finalJson)
	mul_js = json.loads(finalMultimediaJson)

	with open('multimedia.json','w') as outf:
		json.dump(mul_js,outf,indent = 4)

	with open('tweets.json','w') as outf:
		json.dump(js,outf,indent = 4)

def generateGraphs():
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

	#Adding all nodes in multimedia graph
	for mtweet in multim:
		userEntity = mtweet['user']
		username = userEntity['name']
		mulTweetGraph.add_node(username)

	for tweet in tweets:
		inReply = tweet['in_reply_to_screen_name']
		firstUser = tweet['user']
		firstUserName = firstUser['screen_name']
	for twee in tweets:
		user = twee['user']
		name = user['screen_name']
		if name == inReply:
			allTweetGraph.add_edge(name,firstUserName)

	for tweet in multim:
		inReply = tweet['in_reply_to_screen_name']
		firstUser = tweet['user']
		firstUserName = firstUser['screen_name']
	for twee in multim:
		user = twee['user']
		name = user['screen_name']
		if name == inReply:
			allTweetGraph.add_edge(name,firstUserName)

	nx.write_adjlist(allTweetGraph,"allTweetGraph")
	nx.write_adjlist(mulTweetGraph,"multimediaTweetGraph")


if __name__ == "__main__": 
    api = authenticate()
    extractTweets(api)
    generateGraphs()






