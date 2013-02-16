from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import pusher

import config

p = pusher.Pusher(app_id=config.app_id, key=config.app_key, secret=config.app_secret)


class StdOutListener(StreamListener):
	""" A listener handles tweets are the received from the stream. 
	This is a basic listener that just prints received tweets to stdout.
	"""
	def on_data(self, data):
		p['my-channel'].trigger('my_event',{'msg': data})
		return True
	def on_error(self, status):
		print status

if __name__ == '__main__':
	l = StdOutListener()
	auth = OAuthHandler(config.consumer_key, config.consumer_secret)
	auth.set_access_token(config.access_token, config.access_token_secret)
	stream = Stream(auth, l)	
	stream.filter(track=['basketball'])
