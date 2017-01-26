import tweepy
from textblob import TextBlob
import json

# Step 1 - Authenticate
consumer_key= 'KNqXZEmCJJEtIHyN6hTYWzmAv'
consumer_secret= 'Hg0FtDHeOahSpOTjPIuiDLPRSFCZkr4PZwduSUTKmc6gC7OtWK'

access_token='278647040-sBWFMwsnCDP6kG5UDSuIXvbuJoyQUdJBihiilWR1'
access_token_secret='oPcpzqH4D5HhO5JEgowEv8eM9XWDD07gNOrssBLE37dHw'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(tweepy.StreamListener):
    counter = 0 
    def on_data(self, data):
        tweet = json.loads(data)
        #analysis = TextBlob(tweet['text'])
        print(tweet['text'].encode('utf-8'))
        #print(analysis.sentiment)
        #print('-------------------------------------------------------------')
        return True

    def on_error(self, status):
        #print('11111111111111111')
        print(status)
        
    def on_status(self, status):
        global counter
        counter = counter + 1
        if counter < 5:
            return True
        else:
            return False


#myStream = tweepy.Stream(auth = api.auth, listener = StdOutListener())
#myStream.filter(track = ["Trump"], languages=["en"])


public_tweets = api.search('Iran')

for tweet in public_tweets:
	line = tweet.text
	h = tweet.entities.get('hashtags')
	#print(line.encode('utf-8'))
	print(h)
	#analysis = TextBlob(tweet.text)
	#print(analysis.sentiment)
	print('-------------------------------------------------------------')
