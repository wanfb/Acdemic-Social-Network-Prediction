import pickle
from numpy import *

#将引用与文章配对，并赋值

data_num=48919
datafile=open('data_source.dat','rb')
data_list=[]
dic={}
for file_num in range(data_num):
    data=pickle.load(datafile)
    print(data)
    data_list.append(data)
    dic.update({data[6]: data[0]})

key=dic.keys()
save_pickle=open('data.dat','ab')

for row in range(data_num):
    ref=[]
    newdata=[]
    for quote in data_list[row][3]:
        if quote in key:
            ref.append(dic[quote])
    newdata=[data_list[row][0],data_list[row][1],data_list[row][2],ref,data_list[row][4],data_list[row][5],data_list[row][7],data_list[row][8]]
    print(newdata)
    pickle.dump(newdata, save_pickle)

