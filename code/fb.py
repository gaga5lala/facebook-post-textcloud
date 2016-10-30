#-*- coding: utf-8 -*-

import requests
import json
import jieba
import operator

# 達到更好的中文斷詞效果
jieba.set_dictionary('dict.txt.big')

# TODO: fb token
req = requests.get("https://graph.facebook.com/v2.8/10201977955963715/posts?limit=25&until=1467088017&__paging_token=enc_AdBL5uZBNcSQ7XN6CGxDVPxbnJgF67jEZBZBAyKkZC7z00sZCMkIHXIkFudBZBwyv73RKig9pwk36IS5RllrwoWLuf6aTL&access_token=EAACEdEose0cBAOSX9RCyJyuqs801mf8q6B0KP6T0zT231U5wqy2yQRDEeRuwoUsOUHyRQXw5MGpHSZBHBQsys10j8vIBHvFafOsaZB2BWB3ZCxDqbsAvmVshZCpXTRPeehyNKZCN0QM1lHzqcRZBdy01XciBBetLxOTr3efK9aOQZDZD")
js = json.loads(req.text)
coupus = []

# TODO: paging, current only fetch first 25

for post in js["data"]:
    if "message" in post:
        coupus  += jieba.cut(post["message"])

# print coupus

# use
# execfile("/usr/local/lib/python2.7/site-packages/jieba/code/fb.py")

dic = {}
for ele in coupus:
    if ele not in dic:
        dic[ele] = 1
    else:
        dic[ele] += 1

sorted_word = sorted(dic.items(), key = operator.itemgetter(1), reverse=True)

filename = "fb_post.txt"
file = open(filename, "w")

for ele in sorted_word:
    if len(ele[0]) >= 2:
        print ele[0], ele[1] && file.write ele[0], ele[1]

file.close()
