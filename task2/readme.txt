requirements: python-3.6,networkx-2.2 ,numpy-1.15.4，matplotlib-3.0.2,scipy-1.2.0,pyecharts-0.5.11

run order:
data_washing_to_dat-1:选取所需数据
check_reference-2:留选数据集内的引用关系
author_data-3:计算作者得分和合作关系
ego_network:创建自我中心网络

运行方法：将原始数据解压后放在task2目录下，然后按次序运行以上文件

