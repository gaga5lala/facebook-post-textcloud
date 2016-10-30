#-*- coding: utf-8 -*-

import requests
import json
import jieba
import operator

print("start...")

# 達到更好的中文斷詞效果
jieba.set_dictionary('dict.txt.big')

FB_TOKEN = "EAACEdEose0cBAD4E8aIdyOQtUEV5lSgtxUEcmkKIklqbDvi9MjTJ1kPnw74V0Xid1muHVTLh8iweCo7v67PHD0ZAbXtYM3V7JhjZBXYS0S2RS7mQxpkEWwtDIlsJ6fvTv7tKhH90kwB42EKBZA97iGLG854DWqzRiZAdwFG6NQZDZD"

token = FB_TOKEN or input("請輸入 FB token")

req = requests.get("https://graph.facebook.com/v2.8/me?fields=posts&limit=100&access_token=" + token)

js = json.loads(req.text)
coupus = []

# TODO: paging, current only fetch first 25
for post in js["posts"]["data"]:
    if "message" in post:
        coupus  += jieba.cut(post["message"])

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
