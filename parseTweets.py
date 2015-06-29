# -*- coding: utf-8 -*-
#aanroepen van /net/aps/64/bin/python3.2 !!!!
import xml.etree.ElementTree as ET
import glob
import os
import sys
import socket
import re
import string

fp = open("d:/python/thesis/test/nearbyLocationTW_hasan0162_TnB",'a',encoding='utf-8')

file1 = 'd:/python/thesis/test/nearbyLocationTW_hasan0162'
#os.walk("d:/python/thesis/test/Treebank")
# parse input sentence and return alpino output as an xml element tree
def alpino_parse(sent, host='zardoz.service.rug.nl', port=42424):
 s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 s.connect((host,port))
 sent = sent + "\n\n"
 #sentbytes= sent.encode('utf-8')
 #s.sendall(sentbytes)
 s.sendall(sent.encode())
 total_xml=[]
 #bytes_received= b''
 while True:
  xml = s.recv(8192)
  if not xml:
   break
  #bytes_received += byte
  #print(bytes_received.decode('utf-8'), file=sys.stderr)
  #xmlRES = etree.fromstring(bytes_received)

  total_xml.append(str(xml,encoding='utf-8'))
 return "".join(total_xml) 

def tweetloc():
 ltp = ''
 for line in open(file1):
  #ALLEEN VOOR TWEETS VAN EIGEN USERS!
  #line1 = line.split('\t')
  #line1 = line1[1]
  line1 = line.replace("\t","")
  #line1 = line1[1]
  words = line1.split(" ")
  for word in words:
   if word.find("@") != -1:
    wordtoreplace = word
    line1 = line1.replace(wordtoreplace,"gebruiker")
   if word.find("\\") != -1 and len(word) > 5:
    line1 = line1.replace(word,"")
  words = line1.split(" ")
  for word in words:
   if word.find("gebruiker") != -1:
    line1 = line1.replace(word,"")
  line1 = line1.replace("\n","")
  line1 = line1.replace("'","")
  line1 = line1.replace("\\","")
  line1 = line1.replace('"',"")
  line1 = line1.replace(';',"")
  line1 = line1.replace('-',"")
  line1 = line1.replace('_',"")
  line1 = line1.replace('(',"")
  line1 = line1.replace('?',"")
  line1 = line1.replace('!',"")
  line1 = line1.replace(':',"")
  line1 = line1.replace(')',"")
  line1 = line1.replace('^',"")
  line1 = line1.replace('$',"")
  line1 = line1.replace('#',"")
  line1 = line1.replace("  "," ")
  line1 = line1.replace(chr(8221),"")
 
  #line1 = line1.split(" ")
  if len(line1) > 10 and line1 != '' and line1 != ' ' and line1 != '   ':
   lines = line1.split(".")
   parseLine(lines)

def parseLine(lines):
 ltp = ''
 for line in lines:
  if(line != ' ' and line != ''):
   print(line)
   #print("------")
   #haal de interpunctie weg
   regex = re.compile('[%s]' % re.escape(string.punctuation))
   out = regex.sub('', line)
   xmlRES = alpino_parse(out)
   xml2 = ET.fromstring(xmlRES)
   #print(xmlRES)
   #root = xml2.getroot()
   #xml2 = etree.fromstring(xmlRES)
   theX = xml2.findall('.//node[@pos="noun"]')
   for x in theX:
    #doe iets ermee
    thX = x.attrib['root']
    if ltp == '':
     ltp = thX
    else:
     ltp = ''.join([ltp,' ',thX])
   #theX = xml2.xpath('//node[@pos="phrase"]')
   '''theX = xml2.findall('.//node[@pos="phrase"]')
   for x in theX:
    #doe iets ermee
    thX = x.attrib['root']
    if ltp == '':
     ltp = thX
    else:
     ltp = ''.join([ltp,' ',thX])'''
   #theX = xml2.xpath('//node[@pos="name"]')
   theX = xml2.findall('.//node[@pos="name"]')
   for x in theX:
    #doe iets ermee
    thX = x.attrib['root']
    if ltp == '':
     ltp = thX
    else:
     ltp = ''.join([ltp,' ',thX])
   #theX = xml2.xpath('//node[@pos="pronoun"]')
 if ltp != '' and ltp != "gebruiker":
  ltp = ''.join([ltp,'\n']) 
 fp.write(ltp)

tweetloc() 
fp.close()

