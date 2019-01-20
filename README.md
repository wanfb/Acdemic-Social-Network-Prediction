# Acdemic-Social-Network-Prediction
This is the final Project of Social Network Mining in Fudan University

This project is finished by Fangbin Wan, Yihao Xu and Baolong Yang. Xu is in charge of the Task 1 and Task 2, Wan is in charge of Task 3 and the visualization part is done by Yang.

Your generous comments and suggestions about our work is appreciated.

# Task Review

The total project is divided into three tasks. The dataset we ultilized is DBLP. It collects information of paper published on journals and conference about computer.

### Task 1 (Community Discovery)
Design clustering algorithms or community mining algorithms to cluster all the papers in the data set. Use visualize tools to show all fields and highlight the most influential scholars in each field.

### Task 2 (Ego-network)
Show the ego-network of any input scholar. 

### Task 3 (Link Prediction)
Model social relationships among scholars, like predicting the cooperation relationship or citation relationship within shcolars.

# Task 1
For Task 1, we use `Louvain` algorithm for community discovery. Louvain algorithm based on Modularity, which describes the closeness within communities. We reserve the communities that have more than 500 papers. The results can be seen as follows.
![](https://github.com/wanfb/Acdemic-Social-Network-Prediction/raw/master/pictures/community discovery.jpg)  
