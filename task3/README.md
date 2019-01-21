# Task 3
The main idea to finish this task is `collaborative filtering`. Many thanks to [liyumeng](https://github.com/liyumeng/LinkPrediction)'s work. We changed many features based on this work and can achieve very high accuracy. For scholars' collaboration network and citation network, we generate 26 features and 22 features for paper citation network. LightGBM and XGBoost algorithms are used in our models as classifiers. 

To use the code in Task 3, you can run the following codes respectively to extract features from the three neworks.
* author_reference.py
* co_author.py
* paper_reference.py

We also provide some tools to evaluate the performance of the model, to further reduce the dimension of features, and to change the classifier as you like. 
* evaluate.py
* PCA.py
* xgb.py

Here we show the feature importance of scholars' collaboration network.
<img src="https://github.com/wanfb/Acdemic-Social-Network-Prediction/blob/master/pictures/feature-importance.JPG" width = "600" height = "400" align=center />
