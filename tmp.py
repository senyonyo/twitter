#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import secret
import codecs

CK= secret.twkey['ck']
CS= secret.twkey['cs']
ATK= secret.twkey['atk']
ATS= secret.twkey['ats']

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(ATK, ATS)
api = tweepy.API(auth_handler=auth)

#api.update_status("Hello, world!")
keyword = "lang:ja min_retweets:50"

def search_rest(api,keyword,search_count=10):
  search_result = api.search(keyword,count=search_count)
  for i,twt in enumerate(search_result):
    fp = open("tweet.txt","w")
    fp.write("---%3d---" % (i + 1))
    fp.write("%s" % twt.created_at)
    fp.write("%s" % twt.user.name)
    fp.write("%s" % twt.text +"\n")
    fp.close()

search_rest(api,keyword,30)
