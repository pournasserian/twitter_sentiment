
# Simple Twitter Sentiment analysis 
### Using tweepy and textblob


```python
import tweepy
from textblob import TextBlob
import json
```

### Authentication


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

### Creating basic listener to print out the result


```python
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
```

### Filtering public live stream for Trump!


```python
myStream = tweepy.Stream(auth = api.auth, listener = StdOutListener())
myStream.filter(track = ["Trump"], languages=["en"])
```

    RT @JDDeezus: What https://t.co/fITTWMzuWc
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    US election hacking: Putin 'sought to help' Trump https://t.co/SBTr7k9Kmy
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    @CoryBooker Trump is following in Hitler ' s footsteps!  He is one  sick S.O.B.
    Sentiment(polarity=-0.35714285714285715, subjectivity=0.47857142857142854)
    -------------------------------------------------------------
    RT @aravosis: In 1 day, Trump was dissed by all 3 intelligence heads, dumped by former CIA director Woolsey, &amp; thrown shade by former chair…
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    RT @JamilSmith: Racism and sexism are much better predictors for Trump support than is economic dissatisfaction, per a new study. https://t…
    Sentiment(polarity=0.27878787878787875, subjectivity=0.38484848484848483)
    -------------------------------------------------------------
    RT @purpl3rainb0ws: @JordanHancock_ "but I voted for Donald Trump to save jobs! I'm a genius and I know so much about the economy!" - peopl…
    Sentiment(polarity=0.25, subjectivity=0.2)
    -------------------------------------------------------------
    2) Trump's willful ignorance must be tried in a court of law. The case is very strong. @ODNIgov @FBI @CIA @NSAGov @justinamash
    Sentiment(polarity=0.5633333333333334, subjectivity=0.9533333333333333)
    -------------------------------------------------------------
    RT @NPR: The @ODNIgov report concludes that "the Russian Government developed a clear preference for President-elect Trump."… 
    Sentiment(polarity=0.06666666666666667, subjectivity=0.22777777777777777)
    -------------------------------------------------------------
    RT @maggiepriceless: Maybe US tourists should need visas to get into Mexican resorts... or be denied altogether. https://t.co/dOyED6VmmU
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    Trump shadow looms over Detroit auto show https://t.co/at8j1cmsoj https://t.co/CliskHwbxX
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    Never seen so many inbreds in one place. Was this before or after the orgy with the family dog? https://t.co/17wQUhIUU4
    Sentiment(polarity=0.5, subjectivity=0.5)
    -------------------------------------------------------------
    RT @HamiltonElector: When Trump commits his next act of depravity, remember this @MaxineWaters @JacksonLeeTX18 @RepRaulGrijalva… 
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    RT @TheSun: Putin ‘ordered US election hacking to boost Donald Trump’s chances' https://t.co/MVpzGD7BOY https://t.co/OZFpWavpsF
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    RT @LeDonnePrime: He's so ungrateful you'd think he would at least thank them. Truly classless of him. https://t.co/Wd5dsSWISp via @voxdotc…
    Sentiment(polarity=-0.3, subjectivity=0.4)
    -------------------------------------------------------------
    RT @JohnMahr23: @RDannely  Lets  get  to  the  real  issues. https://t.co/dkNuovT9RL
    Sentiment(polarity=0.2, subjectivity=0.30000000000000004)
    -------------------------------------------------------------
    RT @CNN: BREAKING: US intel report finds Russia tried to influence election outcome by boosting Trump and harming Clinton… 
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    RT @APHClarkson: This passage in the US DNI hacking report that suggests Trump, Schröder and Berlusconi are the Kremlin's preferred… 
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    RT @yesnicksearcy: From all the whining you pathetic crybabies have been doing, @salon, seems like you idiots are the ones "confused a… 
    Sentiment(polarity=-0.7333333333333334, subjectivity=0.8333333333333334)
    -------------------------------------------------------------
    RT @igorvolsky: .@NRA spent $10,603,626 to elect Trump. So you know he won't actually do anything to reduce gun violence. He'll jus… 
    Sentiment(polarity=0.23333333333333336, subjectivity=0.3666666666666667)
    -------------------------------------------------------------
    RT @Newsweek: Putin 'sought to help' Trump win U.S. vote, says intel https://t.co/lr4540ddWm https://t.co/BXZV87rB63
    Sentiment(polarity=0.8, subjectivity=0.4)
    -------------------------------------------------------------
    The BLS shows Obama did not create as many jobs as you think. #BLMKidnapping #TRUMP # JobReports #Dow20K #MichelleObama #FLOTUS #POTUS
    Sentiment(polarity=0.5, subjectivity=0.5)
    -------------------------------------------------------------
    US election hacking: Putin 'sought to help' Trump https://t.co/THepHEQVaN
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    RT @The_Trump_Train: BREAKING: Trump/Pence are now officially certified as the winners of the 2016 election. Together we will MAKE AMERICA…
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    US election hacking: Putin 'sought to help' Trump https://t.co/Ic8RBmY8GE https://t.co/6XzFIip9Oj
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    @carrie_simmer  now as he dropped that Trump dissing track in Oct..Fans fear that he might be censored again .. just cuz of  personal grudge
    Sentiment(polarity=0.0, subjectivity=0.3)
    -------------------------------------------------------------
    @PrisonPlanet Trying to make it look (and hoping that it is) like a Trump supportive act! I think they're going to be disappointed!!
    Sentiment(polarity=-0.1875, subjectivity=0.875)
    -------------------------------------------------------------
    @ksl #Polls2017 I don't see these numbers saying "don't" besides polling has been questionable these past few years… https://t.co/URzqypb7Ih
    Sentiment(polarity=-0.31666666666666665, subjectivity=0.45)
    -------------------------------------------------------------
    RT @peterdaou: 1. Bernie did more damage to Hillary's reputation in a few months than Republicans did in 30 years. He is part of t… 
    Sentiment(polarity=0.15, subjectivity=0.3)
    -------------------------------------------------------------
    @CNN You're pathetic to put it mildly. Get a grip and stop sucken off the DNC for BS stories https://t.co/JXWvZECqQj
    Sentiment(polarity=-0.33333333333333337, subjectivity=0.75)
    -------------------------------------------------------------
    US election hacking: Putin 'sought to help' Trump https://t.co/gEazx3zbxF #News
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    U.S. intel report says Putin directed cyber campaign aimed at helping #Trump
    https://t.co/4eQt5FBUYP https://t.co/9gpq0O97td
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    Russian President Vladimir Putin sought to help Donald Trump in presidential... https://t.co/qPKaLM0o99 by #BBCBreaking via @c0nvey
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    RT @RichardWeaving: Kevin Jackson : Dem's love their hate, they create HATE GROUPS like BLM and bring terrorists in our midst. And they… 
    Sentiment(polarity=-0.3666666666666667, subjectivity=0.7999999999999999)
    -------------------------------------------------------------
    @realDonaldTrump ......Estaban Santiago just gave Trump another reason to build the wall.
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    This was released by our government today.
    
    You may be going to jail Mr. #Trump 
    #TrumpLeaks https://t.co/ypqhFlxlJA
    Sentiment(polarity=-0.1, subjectivity=0.0)
    -------------------------------------------------------------
    Biden: Certifies Trump’s Election and Declares ‘It is Over’ to Dems Objections https://t.co/O9gEhYu7gI https://t.co/EatkaaNw5i
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    RT @JackieMartling: Trump wants to replace the CIA with an agency that's easier to spell. ...Jan 21 Levoy Theatre, Millville NJ https://t.c…
    Sentiment(polarity=0.2, subjectivity=0.1)
    -------------------------------------------------------------
    RT @traytrayolay: trump: "we're sending  our battleships to russia"
    #niggernavy: "who all over there"
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    RT @sinanflp: Me trump, attack on florida airport is done by feto @realDonaldTrump @FBI 
    👇👇👇👇👇👇👇👇👇👇👇👇👇👇 https://t.co/jUz95xvDtF
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    RT @comgenKDT: Trump thanks intel community for report he disagrees with   https://t.co/ap9w22nE7L
    Sentiment(polarity=0.2, subjectivity=0.2)
    -------------------------------------------------------------
    BREAKING: Trump Didn’t Expect Ted Cruz To Put The Final Nail In Obama’s Coffin Today! https://t.co/JHBUSMIG0z https://t.co/qJDvyeV7PX
    Sentiment(polarity=0.0, subjectivity=1.0)
    -------------------------------------------------------------
    RT @byefeIicia: Trump: We gotta go to war 
    
    Captain: You got gas money? 
    #niggernavy
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    RT @nytimes: John Kerry: Here's everything Obama did in the world. Trump: I'll be doing the opposite. https://t.co/KPYw3ZOZp1
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    RT @anneapplebaum: Will the Trump White House join Russia in its attempt to destabilize Europe? https://t.co/C2cMveIazA
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    RT @funder: RT ALERT! Donald Trump's Foundation gave $100,000 to the Eric #Trump Foundation #TrumpLeaks #wednesdaywisdom #msnbc… 
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    OPINION: Let's try to stay off Trump's radar, writes Alan Freeman. https://t.co/12JcUVdmbA #cdnpoli #uspoli https://t.co/uO4upwFX5r
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    The CIA is PETRIFIED! Trump Just Promised His Retaliation After Their Attacks Against Him https://t.co/JkLT5Fid79 https://t.co/2sW272aaYS
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    RT @Bikers4Liberty: We fully support the efforts of the 2 Million Bikers 2 DC &amp; their @TrumpInaugural event 2 Million  Trump... https://t.c…
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    RT @dremmelqueen: Arnold Schwarzenegger Has the Perfect Grownup Response to Trump's Moronic Twitter Attack @alternet https://t.co/dqytrGPHBr
    Sentiment(polarity=1.0, subjectivity=1.0)
    -------------------------------------------------------------
    RT @ramadeyrao: U.S. intelligence agencies: Putin ordered intervention in presidential election NOW we know why he want IC GONE!  https://t…
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    Politics|Trump Nods to DNC Hack but Says It Had 'No Effect' on Election - New York Times https://t.co/3RLPmPqYDK https://t.co/1nixQ2fHf1
    Sentiment(polarity=0.13636363636363635, subjectivity=0.45454545454545453)
    -------------------------------------------------------------
    RT @Eating: RT if you think this mozzarella stick would be a better president than Donald Trump. https://t.co/xwXui5MeYr
    Sentiment(polarity=0.5, subjectivity=0.5)
    -------------------------------------------------------------
    RT @grudging1: My 2 cents:
    
    Comey huge impact for Rs coming home to Trump.
    
    Putin/WL huge impact for Steining/Abstaining Ds.
    
    HRC wins with…
    Sentiment(polarity=0.3666666666666667, subjectivity=0.6666666666666666)
    -------------------------------------------------------------
    RT @profpeppard: "What are the lengths America will go to protect its mythic identity of Anglo-Saxon greatness?...answer: Donald Trump."
    
    -…
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-4-ba534ace0d5c> in <module>()
          1 myStream = tweepy.Stream(auth = api.auth, listener = StdOutListener())
    ----> 2 myStream.filter(track = ["Trump"], languages=["en"])
    

    C:\Users\amirp\Anaconda3\lib\site-packages\tweepy\streaming.py in filter(self, follow, track, async, locations, stall_warnings, languages, encoding, filter_level)
        443         self.session.params = {'delimited': 'length'}
        444         self.host = 'stream.twitter.com'
    --> 445         self._start(async)
        446 
        447     def sitestream(self, follow, stall_warnings=False,
    

    C:\Users\amirp\Anaconda3\lib\site-packages\tweepy\streaming.py in _start(self, async)
        359             self._thread.start()
        360         else:
    --> 361             self._run()
        362 
        363     def on_closed(self, resp):
    

    C:\Users\amirp\Anaconda3\lib\site-packages\tweepy\streaming.py in _run(self)
        292             # call a handler first so that the exception can be logged.
        293             self.listener.on_exception(exception)
    --> 294             raise exception
        295 
        296     def _data(self, data):
    

    C:\Users\amirp\Anaconda3\lib\site-packages\tweepy\streaming.py in _run(self)
        261                     self.snooze_time = self.snooze_time_step
        262                     self.listener.on_connect()
    --> 263                     self._read_loop(resp)
        264             except (Timeout, ssl.SSLError) as exc:
        265                 # This is still necessary, as a SSLError can actually be
    

    C:\Users\amirp\Anaconda3\lib\site-packages\tweepy\streaming.py in _read_loop(self, resp)
        322             next_status_obj = buf.read_len(length)
        323             if self.running:
    --> 324                 self._data(next_status_obj)
        325 
        326             # # Note: keep-alive newlines might be inserted before each length value.
    

    C:\Users\amirp\Anaconda3\lib\site-packages\tweepy\streaming.py in _data(self, data)
        295 
        296     def _data(self, data):
    --> 297         if self.listener.on_data(data) is False:
        298             self.running = False
        299 
    

    <ipython-input-3-3b302cf5bb23> in on_data(self, data)
          4     def on_data(self, data):
          5         tweet = json.loads(data)
    ----> 6         analysis = TextBlob(tweet['text'])
          7         print(tweet['text'])
          8         print(analysis.sentiment)
    

    KeyError: 'text'


### Searchin the user's tweets


```python
public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print('-------------------------------------------------------------')
```

    President-elect Trump does now admit Russia hacked the DNC, but obscures fact by adding PRC and 'other countries'. MSM needs to c obscuring
    Sentiment(polarity=-0.125, subjectivity=0.375)
    -------------------------------------------------------------
    RT @LouDobbs: Incredible: Intelligence Leaders Aren't Acting Very Smart. Mr. Trump's Right--This Conduct Isn't Acceptable  #MAGA #TrumpTrai…
    Sentiment(polarity=0.39285714285714285, subjectivity=0.5785714285714286)
    -------------------------------------------------------------
    RT @Cernovich: Since Trump's election there have been hate crime hoaxes, and
    
    - #BLMKidnapping
    
    - Esteban Santiago shot up airport
    
    The Lef…
    Sentiment(polarity=-0.8, subjectivity=0.9)
    -------------------------------------------------------------
    @geckomeat After Trump beating Clinton, anything is possible and reality is clearly broken -:D
    Sentiment(polarity=0.19999999999999998, subjectivity=0.7999999999999999)
    -------------------------------------------------------------
    RT @GreggyBennett: Trump could take away Scientology's tax exempt status to pay for his wall
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    Find out if Trump colluded with Russia &amp; is either being bribed or blackmailed by them. If so, hang him for treason @RepAdamSchiff @ODNIgov
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    ‘Louisiana’s most racist high school’ sending its marching band to Trump inauguration https://t.co/T2ZHmm0jFe #wiunion #wipolitics #MKE #UWM
    Sentiment(polarity=0.33, subjectivity=0.52)
    -------------------------------------------------------------
    RT @Independent: Released US intelligence report states Putin ordered cyber campaign to help Trump https://t.co/rtnEhwEQIu https://t.co/sPX…
    Sentiment(polarity=0.0, subjectivity=0.125)
    -------------------------------------------------------------
    RT @VanityFair: The president-elect is not happy the media received intelligence on alleged Russian hacking before him https://t.co/9P9Ggkp…
    Sentiment(polarity=-0.16666666666666666, subjectivity=0.3666666666666667)
    -------------------------------------------------------------
    @Reuters #KidRock Releases Pro-Donald #Trump T-shirts Only 14$ on Amazon
     BUY IT HERE--&gt;&gt;https://t.co/9P5ORULCiT… https://t.co/2WftqsRzXy
    Sentiment(polarity=0.0, subjectivity=1.0)
    -------------------------------------------------------------
    RT @StevenTDennis: So Comey's FBI says it has high confidence that Putin wanted to help Trump win. Which Comey actually did. A pickle.
    Sentiment(polarity=0.32, subjectivity=0.3466666666666667)
    -------------------------------------------------------------
    @HuffingtonPost Wikileaks concluded that the DEMS got the corrupt MSM (YOU) to prop trump up, thinking he'd be easiest to beat. SO WRONG!
    Sentiment(polarity=-0.5625, subjectivity=0.95)
    -------------------------------------------------------------
    RT @CNN: BREAKING: US intel report finds Russia tried to influence election outcome by boosting Trump and harming Clinton https://t.co/a8XB…
    Sentiment(polarity=0.0, subjectivity=0.0)
    -------------------------------------------------------------
    RT @awzurcher: But Trump won election "fair and square" https://t.co/Zg04D9QACT
    Sentiment(polarity=0.7, subjectivity=0.9)
    -------------------------------------------------------------
    RT @washingtonpost: Declassified report says Putin ‘ordered’ effort to undermine faith in election and help elect Trump https://t.co/akQitF…
    Sentiment(polarity=0.8, subjectivity=0.9)
    -------------------------------------------------------------
    
