import requests

URL = "http://search.twitter.com/search.json?q=phulwama&rpp=5&include_entities=true&with_twitter_user_id=true&result_type=mixed"
location = "AMU"

r = requests.get(url = URL)
data = r.json()

print(data)
