# -*- coding: utf-8 -*-
import operator
wordDict = {}
matrix = {}
lineDict = {}

first = 0

#stopWords = ["aan","afd","als","bij","dat","de","den","der","des","deze","die","dit","dl","door","dr","ed","een","en","enige","enkele","enz","et","etc","haar","het","hierin","hoe","hun","ik","in","inzake","is","je","met","na","naar","nabij","niet","no","nu","of","om","onder","ons","onze","ook","oorspr","op","over","pas","pres","prof","publ","sl","st","te","tegen","ten","ter","tot","uit","uitg","vakgr","van","vanaf","vert","vol","voor","voortgez","voortz","wat","wie","zijn"]

fp = open("d:/python/thesis/test/matrix2.txt",'w',encoding='utf-8')

for line in open("d:/python/thesis/test/vocab.txt",encoding='utf-8'):
 line = line.replace("\n","")
 line = line.replace(" ","")
 line = line.split(",")
 for line2 in line:
  wordDict[line2] = 1

for line in open("d:/python/thesis/test/nearbyLocationTW_beeertje67_TnB",encoding='utf-8'):
 lineDict = {}
 line1 = line.split(" ")
 for line2 in line1:
  if line2.isdigit() == True:
   line2 = "getal"
  if line2.lower() not in lineDict:
   if line2 is not " " and line2 is not "" and line2 is not None:
    lineDict[line2.lower()] = 1
  else:
    lineDict[line2.lower()] += 1
 ltp = ''
 if first == 0:
  ltp = ''
  first = 1
 else:
  ltp = ';'
 for key in wordDict:
  if key in lineDict:
   ltp = "".join([ltp," ",str(lineDict[key])])
  else:
   ltp = "".join([ltp," ","0"])
 fp.write(ltp)
fp.close() 

