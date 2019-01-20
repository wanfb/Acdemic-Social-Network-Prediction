import json
import pickle
import networkx as nx

#读取数据
def read_data(flag,data_num):
    data_file=open('data.dat','rb')
    data_list=[]
    if flag==True:
        for file_num in range(data_num):
            data=pickle.load(data_file)
            print(data)
            data_list.append(data)
    return data_list

#创建合作作者
def co_author(data_num):
    data_list=read_data(1,data_num)
    coau={}
    for row in range(data_num):
        authors=data_list[row][1]
        for i in authors:
            for j in authors:
                if i == j :
                    continue
                else:
                    if i not in coau.keys():
                        coau[i] = {j:1}
                    elif j not in coau[i].keys():
                        coau[i][j] = 1
                    else:
                        coau[i][j] += 1
    print(coau)
    with open("co-author.json", 'w') as f1:
        json.dump(coau,f1)

#计算学者得分
def paper_score_pagerank_all(data_num):
    data_list = read_data(1, data_num)
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

def author_score(data_num):
    score_file=open('PageRank_score_all.json','r')
    score=json.load(score_file)
    data_list=read_data(1,data_num)
    author_score={}
    for row in data_list:
        key=str(row[0])
        if key in score.keys():
            for author in row[1]:
                if author in author_score.keys():
                    author_score[author]+=score[key]
                else:
                    author_score.update({author:score[key]})
    print(author_score)
    with open("author_score_PageRank.json", 'w') as f:
        json.dump(author_score,f)

def main():
    data_num=800000
    co_author(data_num)
    paper_score_pagerank_all(data_num)
    author_score(data_num)

if __name__ == '__main__':
    main()
