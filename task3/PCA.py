from sklearn.decomposition import PCA
#import lightgbm as lgb
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pdb

#train_xs = pd.read_csv("data/raw/train_xs.csv")
train_xs = pd.read_csv("data/raw_paper/train_xs.csv", nrows = 2000)

#pca = PCA(n_components='mle')
pca = PCA(n_components=2)

pca.fit(train_xs)
print(pca.explained_variance_ratio_)
print(pca.get_covariance())

#X_pca = pca.transform(train_xs)

#plt.scatter(X_new[:, 0], X_new[:, 1],marker='o')
#plt.show()

