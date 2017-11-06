from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey="i5EpvF5fswF8xMtIjzkb04WFd"
csecret="i7BEJen8QnkB53SLUfWpAte32ib5k6Zp4qMURN8mohUJq7b0FY"
atoken="4909129803-lGUdCs77Pb6PN8fMlHlne40w2kGAsLivZpuuMZu"
asecret="Lh60OPniFNoWckPzDXWaad4p9GmfE1zbFH6Oij65fniBt"

#from twitterapistuff import *

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet, sentiment_value, confidence)
        
        if confidence*100 >= 80:
            output = open("twitter.txt","a")
            #output.write(tweet)
            #output.write('\t')
            output.write(sentiment_value)
            #output.write('\t')
            #output.write(confidence)
            output.write('\n')
            output.close()
        return True
	
    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=['terrorism'])




