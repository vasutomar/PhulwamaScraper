import requests
import json

jsonFile = open('tweets.json','r')
jsonObject = json.load(jsonFile)
print(jsonObject[1])

