import json

# create a dictionary to store your twitter credentials

twitter_cred = dict()

# Enter your own consumer_key, consumer_secret, access_key and access_secret
# Replacing the stars ("********")

twitter_cred['CONSUMER_KEY'] = 'DZWEzkcpl3mMtGgfQwWW8bm7L'
twitter_cred['CONSUMER_SECRET'] = 'CdidHE8xwrgmlNbFdfyn5SE1euE9joo49XnCFltStKX0IBMIcT'
twitter_cred['ACCESS_KEY'] = '985063033750749184-aKusUrNcaGLuWDfk7swsquOS7qgZ8M8'
twitter_cred['ACCESS_SECRET'] = 'NUN0b5NCy7hJq8qmbtDb88jAMB12qYlvyluSuHpcu4Rjc'

# Save the information to a json so that it can be reused in code without exposing
# the secret info to public 

with open('twitter_credentials.json', 'w') as secret_info:
	json.dump(twitter_cred, secret_info, indent=4, sort_keys=True)
