# Acdemic-Social-Network-Prediction
This is the final project of Social Network Mining in Fudan University

This project is finished by Fangbin Wan, Yihao Xu and Baolong Yang. 
Xu is in charge of the Task 1 and Task 2;
Wan is in charge of Task 3;
The visualization part is done by Yang.

We are appreciated to your generous comments and suggestions about our work.

# Task Review

The total project is divided into three tasks. The dataset we ultilized is DBLP. It collects information of paper published on journals and conference about computer.

#### Task 1 (Community Discovery)
Design clustering algorithms or community mining algorithms to cluster all the papers in the data set. Use visualize tools to show all fields and highlight the most influential scholars in each field.

#### Task 2 (Ego-network)
Show the ego-network of any input scholar. 

#### Task 3 (Link Prediction)
Model social relationships among scholars, like predicting the cooperation relationship or citation relationship within shcolars.

# Task 1
For Task 1, we use `Louvain` algorithm for community discovery. Louvain algorithm based on Modularity, which describes the closeness within communities. We reserve the communities that have more than 500 papers. The results can be seen as follows.

To use the code in task 1

#### 1. install requirements: 
* python-3.6;
* networkx-2.2;
* numpy-1.15.4;
* wordcloud-1.5.0;
* matplotlib-3.0.2;
* scipy-1.2.0;
* unittest-1.1.0

#### 2. Run the following files in order:
* data_washing_to_dat-1;
* check_reference-2;
* relationship-3;
* pylouvain-4;
* community_analysis-5;
* author_analysi-6

#### 3. Result visualization
<img src="https://github.com/wanfb/Acdemic-Social-Network-Prediction/blob/master/pictures/community%20_discovery.jpg" width = "600" height = "400" align=center />

Here is the word cloud of computer vision.

<img src="https://github.com/wanfb/Acdemic-Social-Network-Prediction/blob/master/pictures/word_cloud.jpg" width = "400" height = "200" align=center />

# Task 2
For Task 2, we show the ego-network of a scholar based on his(her) cooperation relationship with other scholars. Here is the ego-network of Feifei Li.

To use the code in task 1

#### 1. install requirements: 
* python-3.6;
* networkx-2.2;
* numpy-1.15.4;
* matplotlib-3.0.2;
* scipy-1.2.0;
* pyecharts-0.5.11

#### 2. Run the following files in order:
* data_washing_to_dat-1;
* check_reference-2;
* author_data-3;
* ego_network;
* community_analysis-5;
* author_analysi-6

#### 3. Result visualization
<img src="https://github.com/wanfb/Acdemic-Social-Network-Prediction/blob/master/pictures/ego-network.JPG" width = "600" height = "400" align=center />

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
