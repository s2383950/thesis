import glob
import os
from dbscan import rundbscan 
from kmeans import runkmeans
from bigrams import runbigrams
from trigrams import runtrigrams
from elasticsearch import Elasticsearch
from randomize import createBigrams
from randomize2 import createTrigram
from unigram import rununigrams

es = Elasticsearch()
#os.chdir("d:/python/thesis/test/stuff")
#fp = open("d:/python/thesis/test/tweetsof_xrobijntjex2",'w')

#sanne: sannekemaartje_
#anne: annexsummer
#gerard: gerardvankooten
#space = spacecakee_
#robijn = xrobijntjex
#mdewidt = mdewidt
#lisa = ohmylisa_
#sheri = sheriiidax
#mariehose = mariejosegmh
#babi = babipangyang
res = es.search(index="thesis", body={"size":7500,"query": { 
        "bool" : {
            "must" : {
                "term" : { "author" : "bramdesmit" }
            }
        }
    }
})
'''res = es.search(index="thesis", body={"size":150000,"query": { 
        "bool" : {
            "must" : {
                "term" : { "place" : "arnhem" }
            }
        }
    }
})'''

#res = es.search(index="thesis", body={"size":100000})
"""print(res['hits']['total'])
locationtweets = 'd:/python/thesis/test/theTest'
fo = open(locationtweets, "w")
for hit in res['hits']['hits']:
 fo.write("%(author)s\t%(text)s\t%(createdAt)s\t%(location)s\t%(coordinates)s\t%(place)s\n" % hit["_source"])
fo.close()
for file in glob.glob("*.bak"):
 for line in open(file):
  line1 = line.split('\t')
  if line1[3] == '"sannekemaartje_"':
   fp.write(line)
fp.close()"""

"""for hit in res['hits']['hits']:
 print("%(coordinates)s" % hit["_source"])"""
locationtweets = rundbscan(res)
#print(locationtweets)
#timetweets = runkmeans(res)
#print(timetweets)
#unigrams = rununigrams(locationtweets)
#print(unigrams)
#bigrams = runbigrams(locationtweets,timetweets)
#print(bigrams)
#trigrams = runtrigrams(locationtweets,timetweets)
#print(trigrams)
#count = 0
'''while (count < 19):
 bigramTweet = createBigrams(bigrams)
 trigramTweet = createTrigram(trigrams)
 ltp = ''.join([bigramTweet,'\t',trigramTweet,'\n'])
 fp.write(ltp)
 count = count + 1
fp.close()'''
#print(bigramTweet)
#print(trigramTweet)