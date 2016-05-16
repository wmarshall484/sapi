#!/usr/bin/python3
import subprocess
import sys
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pprint import pprint
import json

model = sys.argv[1]

#Variables that contains the user credentials to access Twitter API
access_token = "731629216412798977-Pda8jDn4BjSgPFI4YHkL2ynuCmhQ4ES"
access_token_secret = "R9fQMHFoTGhXb43hpPJzDWvNcOy0SsoszNhAlUkxKNnMh"
consumer_key = "Vi2tBZs6u9ixGE704JS4mr0An"
consumer_secret = "iAJHhOn0XA1a4aciqae5VwyhWSuasPFn2yxwZpt8LVcUuJQn2T"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        tweet = "@"
        data = json.loads(data)
        tweet = tweet + data['user']['screen_name'] + ", "
        length = 140-len(tweet)
        cmd = 'th sample.lua {} -gpuid -1 -temperature 0.6 -length {} -primetext "{}" -seed `rand`'.format(model, length, data['text'])
        cmd = cmd.replace("@","")
        proc = subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE)
        text = proc.stdout.read().decode("UTF-8")
        end_str = "--------------------------"
        text = text[text.find(end_str) + len(end_str)+2:]
        
        if text.startswith(data['text'].replace("@", "")):
            text = text[len(data['text'].replace("@", "")):]
            
        text = text.replace("\n", " ")
        tweet = tweet + text
        print("about to update: " + tweet)
        api.update_status(tweet, data['id'])
        
        def on_error(self, status):
            print("=======================================")
            pprint(status)
            
            
l = StdOutListener()
stream = Stream(auth, l)

#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
stream.filter(track=['@auto_stoopidity'])
