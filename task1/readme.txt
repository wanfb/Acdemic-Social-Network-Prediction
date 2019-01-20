requirements: python-3.6,networkx-2.2 ,numpy-1.15.4,wordcloud-1.5.0,matplotlib-3.0.2,scipy-1.2.0,unittest-1.1.0

run order:
data_washing_to_dat-1:选取所需数据
check_reference-2:留选数据集内的引用关系
relationship-3：制作引用关系表
pylouvain-4:louvain算法
community_analysis-5:社区划分结果分析
author_analysi-6：影响力作者分析

运行方法：将原始数据解压后放在task1目录下，然后按次序运行以上文件

