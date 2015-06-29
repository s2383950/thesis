import glob
import os

os.chdir("d:/python/thesis/test/stuff")

userclass = {}
fp = open("d:/python/thesis/test/test",'w')
fp2 = open("d:/python/thesis/test/nearbyLocationTW_serkoapd",'w')
coordinate = '51.842113'
coordinate2 = '3.941836'

for file in glob.glob("*.bak"):
 for line in open(file):
  line1 = line.split('\t')
  if line1[6].find("$") != -1:
   line6 = line1[6].replace("[","")
   line6 = line6.replace("]","")
   line6 = line6.replace("{","")
   line6 = line6.replace("}","")
   line6 = line6.replace('"',"")
   line6 = line6.replace("display_","")
   coors = line6.split('$')
   if coors[0] != "" and coors[1] != '':
    co1 = coors[0]
    co2 = coors[1]
    if co1[:6] == coordinate[:6] and co2[:5] == coordinate2[:5]:
     ltp = ''.join([line1[2],'\n'])
     if line1[3] not in userclass:
      fp2.write(ltp)
      userclass[line1[3]] = 1
     else:
      if userclass[line1[3]] < 2:
       fp2.write(ltp)
       userclass[line1[3]] += 1

os.chdir("d:/python/thesis/test/ma")

for file in glob.glob("*.bak"):
 for line in open(file):
  line1 = line.split('\t')
  if line1[6].find('$') != -1:
   line6 = line1[6].replace("[","")
   line6 = line6.replace("]","")
   line6 = line6.replace("{","")
   line6 = line6.replace("}","")
   line6 = line6.replace("display_","")
   coors = line6.split('$')
   if coors[0] != "" and coors[1] != '':
    co1 = coors[0]
    co2 = coors[1]
    if co1[:6] == coordinate[:6] and co2[:5] == coordinate2[:5]:
     ltp = ''.join([line1[2],'\n'])
     if line1[3] not in userclass:
      fp2.write(ltp)
      userclass[line1[3]] = 1
     else:
      if userclass[line1[3]] < 2:
       fp2.write(ltp)
       userclass[line1[3]] += 1

fp2.close()
for value,key in userclass.items():
 altp = ''.join([value,'\t',str(key),'\n'])
 fp.write(altp)
 print(value," ",str(key))
fp.close()