import pickle
import csv
from operator import itemgetter
import numpy as np
import networkx as nx
import json

def read_data(flag,data_num,community_num):
    community_data=open('community.dat','rb')
    data_file=open('data.dat','rb')
    data_list=[]
    if flag==True:
        for file_num in range(data_num):
            data=pickle.load(data_file)
            #print(data)
            data_list.append(data)
    community_list=[]
    for file_num in range(community_num):
        data=pickle.load(community_data)
        #print(data)
        community_list.append(data)
    return community_list,data_list

def paper_score_pagerank_all(data_num, community_num):
    community_list, data_list = read_data(1, data_num, community_num)
    G = nx.DiGraph()
    score = {}
    for paper in data_list:
        if paper[3]!=[]:
            id=paper[0]
            for ref in paper[3]:
                G.add_edge(id, ref)
    score = nx.pagerank(G)
    out = open('PageRank_score_all.json', 'w', encoding='utf-8')
    json.dump(score, out)

def paper_score_pagerank(name,dic):
    G = nx.DiGraph()
    for paper in dic.items():
        if paper[1]!=[]:
            id=paper[0]
            for ref in paper[1]:
                G.add_edge(id, ref)
    score = nx.pagerank(G)
    filename='community/'+name+'PageRank_score.json'
    out = open(filename, 'w', encoding='utf-8')
    json.dump(score, out)
    return score

def author_dic(datalist,community):
    authordic={}
    for paper in community:
        author_list=datalist[paper-1][1]
        for author in author_list:
            key=authordic.keys()
            if author in key:
                number=authordic[author][0]
                papers=authordic[author][1]
                number+=1
                papers.append(paper)
                authordic.update({author:[number,papers]})
            else:
                papers=[paper]
                authordic.update({author:[1,papers]})
    return authordic

def save_author(dic,name):
    filename='author/'+name+'_authorlist.dat'
    file=open(filename,'wb')
    for item in dic:
        pickle.dump(item,file)

def get_top_author(datalist,community,community_name,top_num,list):
    authordic=author_dic(datalist,community)
    save_author(authordic,community_name)
    score=paper_score_pagerank(community_name,list)
    au_score={}
    for data in authordic.items():
        au_score.update({data[0]:0})
        for paper in data[1][1]:
            if paper in score.keys():
                au_score[data[0]]+=score[paper]
    author_order=sorted(au_score.items(),key=itemgetter(1),reverse=True)
    top = []
    j = 0
    for item in author_order:
        top.append(item)
        j += 1
        if j >= top_num:
            break
    return top,authordic

def top_author_mapping(data_num,community_num,name,top_num):
    community_list, data_list = read_data(1, data_num, community_num)
    csvfile=open('top_authors.csv','w',encoding='utf-8',newline='')
    writefile=open('top_author.dat','wb')
    writer = csv.writer(csvfile)
    for i in range(community_num):
        id=name[i]
        openname='community/'+id+'.json'
        jsonfile=open(openname,'r')
        dic=json.load(jsonfile)
        top,authordic=get_top_author(data_list,community_list[i],id,top_num,dic)
        #save top author list
        author_list=[id]
        for item in top:
            author_list.append(item[0])
        writer.writerow(author_list)
        pickle.dump(author_list, writefile)
        #create matrix between top authors
        filename = 'community/' + id + '_relationship.csv'
        relafile = open(filename,'r',encoding='utf-8-sig')
        reader=csv.reader(relafile)
        rela=[]
        for row in reader:
            rela.append(row)
        relafile.close()
        shape=(top_num,top_num)
        matrix = np.zeros(shape,dtype=np.int)
        for line in rela:
            for ii in range(top_num):
                author = top[ii][0]
                left = authordic[author][1]
                if int(line[0]) in left:
                    for jj in range(top_num):
                        quoted = top[jj][0]
                        right= authordic[quoted][1]
                        if int(line[1]) in right:
                            matrix[ii][jj]+=1
        #write the result
        #print(matrix)
        fname='top_author/'+id+' top_author.csv'
        top_matrix=open(fname,'w',encoding='utf-8',newline='')
        pencil=csv.writer(top_matrix)
        authors=[' ']
        for l in range(top_num):
            authors.append(top[l][0])
        pencil.writerow(authors)
        for k in range(top_num):
            line=[top[k][0]]
            for h in range(top_num):
                line.append(matrix[k][h])
            pencil.writerow(line)
        #print(matrix)

def main():
    name = ['Ad hoc', 'Design Automation', 'Information Retrieval ', 'Mobile Computing', 'MIMO', 'Recommender System',
            'Computer Security', 'Software Engineering ', 'Computer networks', 'Communication ', 'Computer Vision',
            'Distributed System', ' Machine Learning', 'Wireless Sensor', 'Social Network', 'Algorithm', ' Data Mining',
            'Web Service', 'Computer Graphics', 'Decision Making', 'Cognitive Radio', 'Compresive Sensing',
            'Image Processing', 'Bioinformatics']
    #name = ['Ad hoc', 'Computer Security', 'Information Retrieval ', 'Mobile Computing', 'MIMO', 'Recommender system', 'Computer graphics', 'Robotics', 'Computer networks', 'Communication ', 'Computer Vision', 'Distributed System', ' Machine Learning', 'Wireless Sensor', 'Social Network', 'Neural Networks', ' Data Mining', 'Web Service', 'Cryptography', 'Decision Making', 'Cognitive Radio', 'Compresive Sensing', 'Image Processing','Bioinformatics']
    community_num=24
    data_num=48919
    top_num=30
    #paper_score_pagerank_all(data_num, community_num)
    top_author_mapping(data_num,community_num,name,top_num)

if __name__ == '__main__':
    main()