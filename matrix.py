# -*- coding: utf-8 -*-
import operator
wordDict = {}

#stopWords = ["aan","afd","als","bij","dat","de","den","der","des","deze","die","dit","dl","door","dr","ed","een","en","enige","enkele","enz","et","etc","haar","het","hierin","ho","hoe","hun","ik","in","inzake","is","je","met","na","naar","nabij","niet","no","nu","of","om","onder","ons","onze","ook","oorspr","op","over","pas","pres","prof","publ","sl","st","te","tegen","ten","ter","tot","uit","uitg","vakgr","van","vanaf","vert","vol","voor","voortgez","voortz","wat","wie","zijn"]
user = "beeertje67"

'''for line in open("d:/python/thesis/test/TwenteCorpus/locationclusterTweetsSan1",encoding='UTF-8'):
 line = line.replace(":","")
 line = line.replace(",","")
 line = line.replace(".","")
 line = line.replace("!","")
 line = line.replace("?","")
 line = line.replace(";","")
 line = line.replace("\t","")
 line = line.replace("\n","")
 line = line.replace("'","")
 line = line.replace('"',"")
 line = line.replace('(',"")
 line = line.replace(')',"")
 line = line.replace(']',"")
 line = line.replace('[',"")
 line = line.replace('`',"")
 line = line.replace('/',"")
 line = line.replace(chr(8221),"")
 line1 = line.split(" ")
 for line2 in line1:
  if line2.isdigit() == True:
   line2 = "getal"
  if line2.find("@") == -1:
   if line2.find("http") == -1:
    if line2.find(user) == -1:
     if line2.lower() not in wordDict:
      if line2 is not " " and line2 is not "" and line2 is not None:
       if line2 not in stopWords:
        wordDict[line2.lower()] = 1
'''
for line in open("d:/python/thesis/test/nearbyLocationTW_beeertje67_TnB",encoding='UTF-8'):
 line1 = line.split(" ")
 for line2 in line1:
  if line2.isdigit() == True:
   line2 = "getal"
  if line2.find("@") == -1:
   if line2.find("http") == -1:
    if line2.lower() not in wordDict:
     if line2 is not " " and line2 is not "" and line2 is not None:
      wordDict[line2.lower()] = 1

fp = open("d:/python/thesis/test/vocab.txt",'w',encoding='utf-8')
sorted_x = sorted(wordDict.items(), key=operator.itemgetter(1))
for key, value in sorted_x:
 if key is not "":
  ltp = ''.join([key,' , '])
  fp.write(ltp)
fp.close()
