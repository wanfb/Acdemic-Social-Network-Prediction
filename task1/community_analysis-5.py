import pickle
import csv
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import json

def read_data(flag,data_num,community_num):
    community_data=open('community.dat','rb')
    data_file=open('data.dat','rb')
    data_list=[]
    if flag==True:
        for file_num in range(data_num):
            data=pickle.load(data_file)
            print(data)
            data_list.append(data)
    community_list=[]
    for file_num in range(community_num):
        data=pickle.load(community_data)
        print(data)
        community_list.append(data)
    return community_list,data_list

#create worldcloud
def wordcloud(text,name,stopwords):
    wc = WordCloud(background_color="#E7EDD8", max_words=200, stopwords=stopwords)
    wc.generate(text)
    plt.figure(figsize=(10,10))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.title(name, loc='Center', fontsize=14)
    savename='wordcloud/'+name+'.png'
    plt.savefig(savename, dpi=300)
    plt.close()

#check abstract
def check_abstract(data_num,community_num,name,stopwords):
    community_list,data_list=read_data(1,data_num,community_num)
    for i in range(community_num):
        title_list = ''
        abstract_list=''
        for paper in community_list[i]:
            title=data_list[paper-1][7]
            title_list+=title
            abstract=data_list[paper-1][6]
            abstract_list+=abstract
        wordcloud(title_list,name[i]+'_title',stopwords)
        wordcloud(abstract_list,name[i]+'_abstract',stopwords)

#create cummunities
def create_cummunities(data_num,community_num,name):
    community_list, data_list = read_data(1, data_num, community_num)
    relationship_file = open('relationship.csv', 'r',encoding='utf-8')
    relationship_data = csv.reader(relationship_file)
    rela=[]
    for relationship in relationship_data:
        rela.append([int(relationship[0]),int(relationship[1])])
    for i in range(community_num):
        community=community_list[i]
        community_name=name[i]
        #写关系表
        writefile_name='community/'+community_name+'_relationship.csv'
        writefile=open(writefile_name,'w',newline='')
        writer=csv.writer(writefile)
        for relationship in rela:
            if relationship[0] in community and relationship[1] in community:
                relationship=[str(relationship[0]),str(relationship[1])]
                writer.writerow(relationship)
                print(relationship)
        #写引用表
        dic={}
        filename='community/'+community_name+'.json'
        file=open(filename,'w')
        for paper in data_list:
            if paper[0] in community:
                dic.update({paper[0]:[]})
                for item in paper[3]:
                    if item in community:
                        dic[paper[0]].append(item)
        json.dump(dic, file)

#relationship between cummnunities
def community_relation(data_num,community_num,name):
    community_list, data_list = read_data(0, data_num, community_num)
    relationship_file = open('relationship.csv', 'r', encoding='utf-8')
    relationship_data = csv.reader(relationship_file)
    rela = []
    for relationship in relationship_data:
        rela.append([int(relationship[0]), int(relationship[1])])
    writefile=open('community_relation.csv','w',newline='')
    writer = csv.writer(writefile)
    writer.writerow([' ']+name)
    matrix = [[0] * community_num] * community_num
    for i in range(community_num):
        for j in range(community_num):
            count=0
            for relationship in rela:
                if relationship[0] in community_list[i] and relationship[1] in community_list[j]:
                    count+=1
            print(count)
            matrix[i][j]=count
        writer.writerow([name[i]]+matrix[i])

def main():
    name = ['Ad hoc', 'Design Automation', 'Information Retrieval ', 'Mobile Computing', 'MIMO', 'Recommender System', 'Computer Security', 'Software Engineering ', 'Computer networks', 'Communication ', 'Computer Vision', 'Distributed System', ' Machine Learning', 'Wireless Sensor', 'Social Network', 'Algorithm', ' Data Mining', 'Web Service', 'Computer Graphics', 'Decision Making', 'Cognitive Radio', 'Compresive Sensing', 'Image Processing','Bioinformatics']
    community_num=24
    data_num=48919
    stopwords=list(STOPWORDS)
    stopwords+=['work','many','application','algorithms','first','second','three','two','one','image','test','function','problem','Systems','solution','systems','system','algorithm','Algorithm','network','propose','Model','methods','design','different','results','result','show','time','proposed','technique','using','based','model','data','analysis','problem','method','use','used','paper','performance','application','new','two','one','information','approach','multi','set','present','provide']
    check_abstract(data_num, community_num,name,stopwords)
    #create_cummunities(data_num,community_num,name)
    #community_relation(data_num,community_num,name)

if __name__ == '__main__':
    main()


