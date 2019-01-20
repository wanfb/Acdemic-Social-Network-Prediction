import json
import pickle

#将原始数据进行清洗并转化为dat格式

def washing_data(path):
    new=open(path+'/data_source.dat','ab')
    #keys = ['order','authors', 'n_citation', 'references', 'venue', 'year', 'id']
    i=1
    for j in range(4):
        with open(path + '\dblp-ref-'+str(j)+'.json', "r", encoding='utf-8') as origin:
            for line in origin.readlines():
                try:
                    jsonData = json.loads(line)
                    if 'references' in jsonData.keys() and 'authors' in jsonData.keys() and 'venue' in jsonData.keys() and 2006 <= jsonData['year'] <= 2015 and jsonData['venue']!="" and jsonData['n_citation']>100 and 'abstract' in jsonData.keys():
                        values = [i,jsonData['authors'], jsonData['n_citation'], jsonData['references'], jsonData['venue'],jsonData['year'], jsonData['id'],jsonData['abstract'],jsonData['title']]
                        print(values)
                        pickle.dump(values,new)
                        i=i+1
                except UnicodeError as u:
                    continue

path='D:\social net\dblp-ref'
washing_data(path)