#!/usr/bin/python3
import subprocess
import sys
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pprint import pprint
import json
import time

model = sys.argv[1]
question = 'When was the beginning of time?'
cmd = './sample.py cv/lm_lstm_epoch8.02_1.5343.t7 "When was the beginning of time?"'

#Variables that contains the user credentials to access Twitter API
access_token = "731629216412798977-Pda8jDn4BjSgPFI4YHkL2ynuCmhQ4ES"
access_token_secret = "R9fQMHFoTGhXb43hpPJzDWvNcOy0SsoszNhAlUkxKNnMh"
consumer_key = "Vi2tBZs6u9ixGE704JS4mr0An"
consumer_secret = "iAJHhOn0XA1a4aciqae5VwyhWSuasPFn2yxwZpt8LVcUuJQn2T"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while True:
    proc = subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE)
    text = proc.stdout.read().decode("UTF-8")
    end_str = "--------------------------"
    text = text[text.find(end_str) + len(end_str)+2:]
    
    if text.startswith(question):
        text = text[len(question)+2:]
        
    text = text.replace("\n", " ")
        
    api.update_status(text)
    time.sleep(86400)    
