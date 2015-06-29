import numpy as np
from numpy import matrix
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

#filename = 'tweetsof_sannekemaartje_'

a = []


def rundbscan(filename):
 fileofTweets = 'd:/python/thesis/test/locationclusterTweets_bramdesmit'
 
 b = []
 co1 = []
 co2 = []
 coordinate = 51.071572
 coordinate2 = 4.359153
 #coordinate = 52.916866
 #coordinate2 = 5.164232
 #num_lines = 100000
 num_lines = filename['hits']['total']
 #print(num_lines)
 b.append(coordinate)
 b.append(coordinate2)
 
 for hit in filename['hits']['hits']:
  coordinates = "%(coordinates)s" % hit["_source"]
  if coordinates.find("$") != -1: 
   coordinates = coordinates.split('$')
   cor0 = coordinates[0].replace(']',"")
   cor1 = coordinates[1].replace(']',"")
   cor0 = cor0.replace('}',"")
   cor1 = cor1.replace('}',"")
  #if(cor0 != '' and cor1 != '' and cor0 != '.' and cor1 != '.'):
   #if(float(cor0) > 49 and float(cor0) < 54 and float(cor1) > 3 and float(cor1) < 8):
   co1.append(cor0)
   co2.append(cor1)
   #else:
    #num_lines = num_lines - 1
  #else:
   #num_lines = num_lines - 1
  else:
   num_lines = num_lines - 1
 appendIt(co2,co1,num_lines)
 Satrix = np.array(a)
 Satrix2 = np.array(b)
#print(Satrix[0][0])

##############################################################################
# Generate sample data
#centers = [[1, 1], [-1, -1], [1, -1]]
#X, labels_true = make_blobs(n_samples=10, centers=centers, cluster_std=0.4,random_state=0)

#Satrix = StandardScaler().fit_transform(Satrix)
#print(Satrix)
##############################################################################
# Compute DBSCAN
 db = DBSCAN(eps=0.1).fit(Satrix)
#print(X)
 core_samples = db.core_sample_indices_
 labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
 n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
 createBlob(labels,core_samples,Satrix,n_clusters_)
#clusters zijn als volgt terug te halen: The first cluster is X[labels == 0], etc.: en outliniers zijn hieronder weergegeven.
 outliers = Satrix[labels == -1]
 cluster1 = Satrix[labels == 0]
 cluster2 = Satrix[labels == 1]
 cluster3 = Satrix[labels == 2]
 cluster4 = Satrix[labels == 3]
 cluster5 = Satrix[labels == 4]
 cluster6 = Satrix[labels == 5]
 cluster7 = Satrix[labels == 6]
 cluster8 = Satrix[labels == 7]
 cluster9 = Satrix[labels == 8]
 cluster10 = Satrix[labels == 9]
 
 #print(cluster1)
 #print("hoi")
 #print(cluster2)
 #print("hoi")
 #print(cluster3)
#find current time cluster
 timefound = False
 cluster = 0
 #coor1 = np.asscalar(Satrix[0][0])
 coor1 = coordinate
 coor2 = coordinate2
 #print(coor1)
 #coor2 = np.asscalar(Satrix[0][1])
 #print(coor2)
 for (x,y) in cluster1:
  tempx = np.asscalar(x)
  tempy = np.asscalar(y)
  if float(coor1) == float(tempy) and float(coor2) == float(tempx):
   timefound = True
   cluster = 1
 if timefound == False and cluster2.size:
  for (x,y) in cluster2:
   tempx = np.asscalar(x)
   tempy = np.asscalar(y)
   if float(coor1) == float(tempy) and float(coor2) == float(tempx):
    timefound = True
    cluster = 2
 if timefound == False and cluster3.size:
  for (x,y) in cluster3:
   tempx = np.asscalar(x)
   tempy = np.asscalar(y)
   if float(coor1) == float(tempy) and float(coor2) == float(tempx):
    cluster = 3
    timefound = True
 if timefound == False and cluster4.size:
  for (x,y) in cluster4:
   tempx = np.asscalar(x)
   tempy = np.asscalar(y)
   if float(coor1) == float(tempy) and float(coor2) == float(tempx):
    timefound = True
    cluster = 4
 if timefound == False and cluster5.size:
  for (x,y) in cluster5:
   tempx = np.asscalar(x)
   tempy = np.asscalar(y)
   if float(coor1) == float(tempy) and float(coor2) == float(tempx):
    timefound = True
    cluster = 5
 if timefound == False and cluster6.size:
  for (x,y) in cluster6:
   tempx = np.asscalar(x)
   tempy = np.asscalar(y)
   if float(coor1) == float(tempy) and float(coor2) == float(tempx):
    timefound = True
    cluster = 6
 if timefound == False and cluster7.size:
  for (x,y) in cluster7:
   tempx = np.asscalar(x)
   tempy = np.asscalar(y)
   if float(coor1) == float(tempy) and float(coor2) == float(tempx):
    timefound = True
    cluster = 7
 if timefound == False and cluster8.size:
  for (x,y) in cluster8:
   tempx = np.asscalar(x)
   tempy = np.asscalar(y)
   if float(coor1) == float(tempy) and float(coor2) == float(tempx):
    timefound = True
    cluster = 8
 if timefound == False and cluster9.size:
  for (x,y) in cluster9:
   tempx = np.asscalar(x)
   tempy = np.asscalar(y)
   if float(coor1) == float(tempy) and float(coor2) == float(tempx):
    timefound = True
    cluster = 9
 if timefound == False and cluster10.size:
  for (x,y) in cluster10:
   tempx = np.asscalar(x)
   tempy = np.asscalar(y)
   if float(coor1) == float(tempy) and float(coor2) == float(tempx):
    timefound = True
    cluster = 10

#maak tijdelijk bestandje met alle tweets van huidige locatiecluster
 if cluster == 1:
  defTimeCluster = cluster1
 elif cluster == 2:
  defTimeCluster = cluster2
 elif cluster == 3:
  defTimeCluster = cluster3
 elif cluster == 4:
  defTimeCluster = cluster4
 elif cluster == 5:
  defTimeCluster = cluster5
 elif cluster == 6:
  defTimeCluster = cluster6
 elif cluster == 7:
  defTimeCluster = cluster7
 elif cluster == 8:
  defTimeCluster = cluster8
 elif cluster == 9:
  defTimeCluster = cluster9
 elif cluster == 10:
  defTimeCluster = cluster10
 
 fo = open(fileofTweets, "w")
 
 for hit in filename['hits']['hits']:
  coordinates = "%(coordinates)s" % hit["_source"]
  coordinates = coordinates.split('$')
  lineWrittin = False
  for (x,y) in defTimeCluster:
   if y == coordinates[0] and x == coordinates[1]:
    if lineWrittin == False:
     fo.write("%(author)s\t%(text)s\t%(createdAt)s\t%(location)s\t%(coordinates)s\t%(place)s\n" % hit["_source"])
     lineWrittin = True
 fo.close()
 return fileofTweets
#print('Estimated number of clusters: %d' % n_clusters_)

def appendIt(co1,co2,num_lines):
 count1 = 0
 for i in range(num_lines):
  a.append([])
  for j in range(2):
   if j == 0:
    a[i].append(co1[count1])
   else:
    a[i].append(co2[count1])
  count1+=1
  
#print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
#print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
#print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
#print("Adjusted Rand Index: %0.3f" % metrics.adjusted_rand_score(labels_true, labels))
#print("Adjusted Mutual Information: %0.3f" % metrics.adjusted_mutual_info_score(labels_true, labels))
#print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels))

##############################################################################
# Plot result
import pylab as pl

# Black removed and is used for noise instead.
def createBlob(labels,core_samples,Satrix,n_clusters_):
 unique_labels = set(labels)
 colors = pl.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
 for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = 'k'
        markersize = 6
    class_members = [index[0] for index in np.argwhere(labels == k)]
    cluster_core_samples = [index for index in core_samples
                            if labels[index] == k]
    for index in class_members:
        x = Satrix[index]
        if index in core_samples and k != -1:
            markersize = 14
        else:
            markersize = 6
        pl.plot(x[0], x[1], 'o', markerfacecolor=col,
                markeredgecolor='k', markersize=markersize)

 pl.title('Estimated number of clusters: %d' % n_clusters_)
 pl.show()