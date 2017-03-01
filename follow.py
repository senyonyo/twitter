#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import secret

CK= secret.twkey['ck']
CS= secret.twkey['cs']
ATK= secret.twkey['atk']
ATS= secret.twkey['ats']

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(ATK, ATS)

api = tweepy.API(auth)

api.update_status("bot テスト")
