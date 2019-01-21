import xgboost as xgb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import cross_val_score

x_train = np.array(pd.read_csv("data/raw_coauthor2/train_xs.csv"))
x_test = np.array(pd.read_csv("data/raw_coauthor2/test_xs.csv"))
y_train = np.array(pd.read_csv('data/raw_coauthor2/training_set.txt',
                      sep=' ', usecols=[2], header=None))[:, 0]
y_test = np.array(pd.read_csv('data/raw_coauthor2/testing_set_label.txt',
                     sep=' ', usecols=[2], header=None))[:, 0]
gbm = xgb.XGBClassifier().fit(x_train, y_train)
prediction = gbm.predict(x_test)
# MAE = np.average(np.abs(np.subtract(pre, y_test)))
# print(MAE)
scores = cross_val_score(gbm, x_train, y_train, cv=3, scoring='roc_auc')
print(scores.mean())
