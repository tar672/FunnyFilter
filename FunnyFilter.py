import re
import json
import time
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import pusher
import config

send = False
lastSent = 0.0
notSentTot = 0
notSentThisTime = 0
class TweetListener(StreamListener):
	def on_data(self, data):
		global lastSent, notSentTot, notSentThisTime
		if(send and lastSent < time.time() - 1 and filterTweets(data)):
			print "1 sent, " + str(notSentThisTime) + " not sent this time and " + str(notSentTot) + " not sent in total"
			p['all-tweets'].trigger("tweet", data)
			lastSent = time.time()
			notSentThisTime = 0
		else:
			notSentTot += 1
			notSentThisTime += 1
		return True

	def on_error(self, status):
		print status

def updateStream():
	stream.disconnect()
	stream.filter(async=True, track=terms)

p = pusher.Pusher(app_id=config.app_id, key=config.app_key, secret=config.app_secret)

l = TweetListener()
auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
stream = Stream(auth, l)

#Returns false if tweet contains a banned term
def filterTweets(data):
	bannedTerms = re.compile('.*@|.*lol$|.* ur ')
	m = data.match(data)
	if m: 
		print "filtered"
		return False
	else:
		print "sent"
		return True

terms = ["dontremoveme", "funny"]
stream.filter(async=True, track=terms)

while(True):
	i = raw_input("[q]uit, [t]oggle sending, [a:]dd term <term>, [r:]emove term <term>\n")
	if(i == "q"):
		stream.disconnect()
		exit(0)
	if(i == "t"):
		send = not send
		print "sending is: " + str(send)
	if(i[0] == "a"):
		terms.append(i[2:])
		updateStream()
	if(i[0] == "r"):
		terms.remove(i[2:])
		updateStream()
