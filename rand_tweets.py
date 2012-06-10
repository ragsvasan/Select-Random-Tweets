import json
import requests
import random
import time

'''
Author: Rags Srinivasan http://twitter.com/rags
 Generates random tweet ids and pulls those tweets
Use it for random sampling
usage: python rand_tweets.py > tweets.txt
Output is in JSON format that can be converted into CSV easily
'''

random.seed(time.time())

'''
Select 400 random tweets. Since the API to get single tweet with exact id 
is not effective I use here search api call with max_id set to random id and the number of entries per page set to 100. 
This also means I should set some value for 'q' parameter, here I set it to 'a' since it is likely to appear in all tweets.
'''

print  '{'
for page in range (1,4):
	rand = random.random()
	id = str(long( rand*1000000000000000000 ))
	query_params = { 'q':'a',
       	'include_entities':'true', 'lang':'en',
         'show_user':'true',
         'rpp': '100', 'page': page,
         'result_type': 'mixed',
       	 'max_id':id}
	r = requests.get('http://search.twitter.com/search.json',
                 params=query_params)
	tweets = json.loads(r.text)['results']
	for tweet in tweets:
		if tweet.get('text') :
			print  tweet
print  '}'
print


