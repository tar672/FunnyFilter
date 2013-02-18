import time
import threading
import json

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import pusher

import config

from flask import Flask, request

class TweetListener(StreamListener):
	def on_data(self, data):
		global terms
		print "tweet!"
		for t in terms:
			if(t not in data):
				continue

			if(len(terms[t]['cache'])+len(data) < 900):
				if(terms[t]['cache'] != ""):
					data = "," + data
				terms[t]['cache'] += data

			if(terms[t]['time'] < time.time()-3):
				print "sent!"
				p['all-tweets'].trigger(t, "[" + terms[t]['cache'] + data + "]")

				terms[t]['time'] = time.time()
				terms[t]['cache'] = ""

		return True

	def on_error(self, status):
		print status

new = True
def getStream():
	global new
	stream = Stream(auth, l)
	while(1):
		if(new):
			print "update stream"
			stream.disconnect()
			t = threading.Thread(target=stream.filter, kwargs={'track':terms})
			t.daemon = True
			t.start()
			new = False
		time.sleep(2)

p = pusher.Pusher(app_id=config.app_id, key=config.app_key, secret=config.app_secret)
terms = {"maithu":{"time":0, "cache":""}}

l = TweetListener()
auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

t = threading.Thread(target=getStream)
t.daemon = True
t.start()

app = Flask(__name__)
app.debug = True

@app.route('/addTerm')
def addTerm():
	global new, terms
	print "addTerm: " + request.args.get("term")
	terms[request.args.get("term")] = {"time":0, "cache":""}
	new = True
	return "yay"
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, use_reloader=False)
