

```python
import tweepy
from textblob import TextBlob
```


```python
# Step 1 - Authenticate
consumer_key= 'DjZQINSdfCpZ54nxlG6W5g'
consumer_secret= 'bvMPkOJo65KCXKqNsmCYEXYiGCvXqh1NPI7iMNqR9Q'

access_token='278647040-sgX4F2mbN4xYcfWVmJk6qGaXg8uu7PlfsokyU231'
access_token_secret='Q3EIeuiG0PAoXzSaK6Eyd4gDMD8qTef40yNeddAriw'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
```


```python
#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')
```


```python
#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
```

    Man murders UPS driver thinking it was Trump, media silent https://t.co/EMzbdNkrws via @worldnetdaily
    Sentiment(polarity=0.0, subjectivity=0.1)
    
    RT @NYTNational: U.S. economy adds 156,000 jobs in December, a tepid ending to Obama era, even as Trump promises much bigger gains. https:/…
    Sentiment(polarity=0.0, subjectivity=0.5)
    
    RT @eileendefreest: When the muck hits the fan it will cost taxpayers millions to impeach Trump when all it should've taken is this to stop…
    Sentiment(polarity=0.0, subjectivity=0.0)
    
    RT @lilduval: Trump got 4 years to back up all that shit he be talking. This is why I don't trip. I believe in letting a person hang they s…
    Sentiment(polarity=-0.1, subjectivity=0.4)
    
    RT @TMZ: Arnold Schwarzenegger Tells Trumps To Focus on U.S., Not TV Ratings (VIDEO) https://t.co/Yv4lbnCyod
    Sentiment(polarity=0.0, subjectivity=0.0)
    
    RT @PrisonPlanet: MTV &amp; Billboard also promoted another song literally called "f**k Donald Trump". https://t.co/xZwDOdxK1b
    
    This is the cul…
    Sentiment(polarity=0.0, subjectivity=0.0)
    
    RT @traytrayolay: trump: "we're sending  our battleships to russia"
    #niggernavy: "who all over there"
    Sentiment(polarity=0.0, subjectivity=0.0)
    
    RT @missLtoe: Contractors file liens against trump's D.C. hotel, claiming they were stiffed $5 million https://t.co/KuZipoGIQy via @HuffPos…
    Sentiment(polarity=0.0, subjectivity=0.0)
    
    RT @SenSanders: Mr. Trump must make it clear that he will keep his word and veto any legislation that cuts Social Security, Medicare and Me…
    Sentiment(polarity=0.06666666666666668, subjectivity=0.22499999999999998)
    
    RT @nycsouthpaw: Trump can't accomplish a peaceful transfer of power on Celebrity Apprentice.
    Sentiment(polarity=0.25, subjectivity=0.5)
    
    RT @DailyCaller: Opinion: More Citizen-Ambassadors, Please, Mr. Trump https://t.co/0QngTEGEVd https://t.co/rJhhSzIswz
    Sentiment(polarity=0.5, subjectivity=0.5)
    
    RT @Evan_McMullin: General Mattis is a leader of great character. That's the underlying reason for these clashes with Trump's team. https:/…
    Sentiment(polarity=0.42500000000000004, subjectivity=0.625)
    
    RT @kylegriffin1: Today, Trump is receiving an important intel briefing on Russia's interference in the US election—and he's tweeting about…
    Sentiment(polarity=0.4, subjectivity=1.0)
    
    Massive Kritik - US-Starökonom Larry Summers sauer: "Trump erpresst Unternehmen" https://t.co/QVJlWWrBkt
    Sentiment(polarity=0.0, subjectivity=1.0)
    
    Trump me cae como una patada en los huevos
    Sentiment(polarity=0.0, subjectivity=0.0)
    
    


```python

```
