import numpy as np
import lda
from scipy.stats import mode
#import lda.datasets

#fp = open("d:/python/thesis/test/ldaTest/reuters.txt",'w',encoding='utf-8')

fp = open("d:/python/thesis/test/lda_beeertje67_TnB.txt",'w',encoding='utf-8')
fp2 = open("d:/python/thesis/test/ldaArray_beeertje67_TnB.txt",'w',encoding='utf-8')

vocabAr = []

for line in open("d:/python/thesis/test/matrix2.txt",encoding='utf-8'):
 line2 = line.replace("\n","")
 temp = np.matrix(line2)
 X = temp.view(np.ndarray)
for line in open("d:/python/thesis/test/vocab.txt",encoding='utf-8'):
 line = line.replace("\n","")
 line1 = line.split(",")
 for word in line1:
  word = word.replace(" ","")
  vocabAr.append(word)
 vocab = tuple(vocabAr)

#X = lda.datasets.load_reuters()
#fp.write(X)
#fp.close()
#vocab = lda.datasets.load_reuters_vocab()
#fp.write(vocab)
#fp.close()
count = 0
titles = []
avgT = []
nep = []
#15000 voor jpmffb
while count != 25000:
 titles.append(str(count))
 count += 1
X.shape
#X.shape(395, 4258)
model = lda.LDA(n_topics=350, n_iter=500, random_state=None)
model.fit(X)  # model.fit_transform(X) is also available
topic_word = model.topic_word_  # model.components_ also works
n_top_words = 20
doc_topic = model.doc_topic_
for i in range(25000):
 try:
    #print("{} (top topic: {})".format(titles[i], doc_topic[i].argmax()))
    topicnum = int(doc_topic[i].argmax())
    avgT.append(topicnum)
 except IndexError:
    nep.append("skip")
 else:
    nep.append("---")
fp2.write(str(avgT))
print(mode(avgT))
#fp.write("{} (top topic: {})".format(titles[0], doc_topic[0].argmax()))
fp.write("\n")
for i, topic_dist in enumerate(topic_word):
 topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
 fp.write('Topic {}: {}'.format(i, ' '.join(topic_words)))
 fp.write("\n")
fp.close()