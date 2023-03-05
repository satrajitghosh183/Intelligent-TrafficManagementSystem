import daal4py as d4p
import joblib
import pandas as pd
import numpy as np

d4p.daalinit() 
infile = "./data/distributed_data/daal4py_Distributed_Kmeans_" + str(d4p.my_procid()+1) + ".csv"

# read data
X = pd.read_csv(infile)





init_result = d4p.kmeans_init(nClusters = 3, method = "plusPlusDense", distributed=True).compute(X)



# retrieving and printing inital centroids
centroids = init_result.centroids
print("Here's our centroids:\n\n\n", centroids, "\n")

centroids_filename = './models/kmeans_clustering_initcentroids_'+  str(d4p.my_procid()+1) + '.csv'

joblib.dump(centroids, centroids_filename)




# loading the initial centroids from a file
loaded_centroids = joblib.load(open(centroids_filename, "rb"))
print("Here is our centroids loaded from file:\n\n",loaded_centroids)





kmeans_result = d4p.kmeans(nClusters = 3, maxIterations = 5, assignFlag = True,
                           accuracyThreshold = 5.0e-6, gamma = 1.0).compute(X, init_result.centroids)




assignments = kmeans_result.assignments
print("Here is our cluster assignments for first 5 datapoints: \n\n", assignments[:5])
