import csv
import pickle
from scipy.sparse import dok_matrix
import numpy as np
#创造邻接矩阵与关系对用表

datafile=open('data.dat','rb')
csvfile = open("relationship.csv", "w", encoding='utf-8',newline='')
writer=csv.writer(csvfile)
writefile=open("matrix.dat",'wb')

#title=['source','target']
#writer.writerow(title)

#read_data
data_num=48919
data_list=[]
for file_num in range(data_num):
    data=pickle.load(datafile)
    print(data)
    data_list.append(data)

for row in range(data_num):
    for quote in data_list[row][3]:
        relationship=[row+1,quote]
        print(relationship)
        writer.writerow(relationship)

S = dok_matrix((data_num,data_num), dtype=np.float32)
for row in range(data_num):
    for quote in data_list[row][3]:
        S[row,quote-1]=1
matrix=dok_matrix.tocoo(S)
pickle.dump(matrix,writefile)
