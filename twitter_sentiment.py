import tweepy
from textblob import TextBlob
import json

# Step 1 - Authenticate
consumer_key= 'DjZQINSdfCpZ54nxlG6W5g'
consumer_secret= 'bvMPkOJo65KCXKqNsmCYEXYiGCvXqh1NPI7iMNqR9Q'

access_token='278647040-sgX4F2mbN4xYcfWVmJk6qGaXg8uu7PlfsokyU231'
access_token_secret='Q3EIeuiG0PAoXzSaK6Eyd4gDMD8qTef40yNeddAriw'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(tweepy.StreamListener):
    counter = 0 
    def on_data(self, data):
        tweet = json.loads(data)
        analysis = TextBlob(tweet['text'])
        print(tweet['text'])
        print(analysis.sentiment)
        print('-------------------------------------------------------------')
        return True

    def on_error(self, status):
        print(status)
        
    def on_status(self, status):
        global counter
        counter = counter + 1
        if counter < 5:
            return True
        else:
            return False


myStream = tweepy.Stream(auth = api.auth, listener = StdOutListener())
myStream.filter(track = ["Trump"], languages=["en"])


public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print('-------------------------------------------------------------')
