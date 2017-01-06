import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'DjZQINSdfCpZ54nxlG6W5g'
consumer_secret= 'bvMPkOJo65KCXKqNsmCYEXYiGCvXqh1NPI7iMNqR9Q'

access_token='278647040-sgX4F2mbN4xYcfWVmJk6qGaXg8uu7PlfsokyU231'
access_token_secret='Q3EIeuiG0PAoXzSaK6Eyd4gDMD8qTef40yNeddAriw'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
