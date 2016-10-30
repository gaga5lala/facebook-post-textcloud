#-*- coding: utf-8 -*-

import requests
import json
import jieba
import operator

print("start...")

# 達到更好的中文斷詞效果
jieba.set_dictionary('dict.txt.big')

FB_TOKEN = "EAACEdEose0cBAAmHDUaUb0otyouBq1B4p4NZCoZC4CjTmbVwrMAny3b4ZAZChO9zsUYOrIoHZBEFOep0WUMZA8IsDGZBbWwYryGyQC9NG8LdjZC69kbo1hSSkYNtVsmZAhnT9AO5BisR96ET8Rrn2ZBRDKWhLZACpkYQz0fMnPKSZBZC69wZDZD"

token = FB_TOKEN or input("請輸入 FB token")

req = requests.get("https://graph.facebook.com/v2.8/me/posts?limit=100&access_token=" + token)

js = json.loads(req.text)
coupus = []

# TODO: enhance paging control, eg. last 5 page
while "paging" in js:
    for post in js["data"]:
        if "message" in post:
            coupus  += jieba.cut(post["message"])

    req = requests.get(js["paging"]["next"])
    print("## next page\n")
    js = json.loads(req.text)

dic = {}
for ele in coupus:
    if ele not in dic:
        dic[ele] = 1
    else:
        dic[ele] += 1

sorted_word = sorted(dic.items(), key = operator.itemgetter(1), reverse=True)

filename = "fb_post.txt"
file = open(filename, "w")

words = ""

for ele in sorted_word:
    if len(ele[0]) >= 2:
        print ele[0], ele[1]
        words += "{0} {1}\n".format(ele[0].encode("utf-8"), ele[1])

file.write(words)
file.close()
