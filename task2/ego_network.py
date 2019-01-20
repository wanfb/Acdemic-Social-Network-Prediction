import json
from pyecharts import Graph

def ego_network(author):
    with open("co-author.json", 'r') as f:
        ego_dic = json.load(f)
    with open("author_score_PageRank.json",'r') as f:
        auscore = json.load(f)
    nodes = [{'name':author, 'symbolSize':auscore[author]**0.5*1000}]
    links = []
    print(ego_dic[author].items())
    for item in ego_dic[author].items():
        if item[0] not in auscore.keys():
            nodes.append({'name': item[0], 'symbolSize': 5})
            links.append({"source": author, "target": item[0], 'value': item[1]})
        elif auscore[item[0]]**0.5*1000<5:
            nodes.append({'name': item[0], 'symbolSize': 5})
            links.append({"source": author, "target": item[0], 'value': item[1]})
        else:
            nodes.append({'name': item[0],  'symbolSize': auscore[item[0]]**0.5*1000})
            links.append({"source": author, "target": item[0], 'value': item[1]})

    for i in ego_dic[author].items():
        for j in ego_dic[i[0]].items():
            if j in ego_dic[author].items():
                links.append({"source": i[0], "target": j[0], 'value': i[1]})

    graph = Graph("Ego-network of %s"%author, width= 1200, height = 900)
    graph.add("", nodes, links,
              is_label_show=True,label_text_color='blue',
              graph_repulsion=500, is_rotatelabel=False, is_roam=True,graph_gravity=0.02)
    graph.render(author+".html")
    return ego_dic[author]

def main():
    ego_network('Li Fei-Fei')
    #ego_network(author="Kaiming He")
    #ego_network('Harald Haas')
    ego_network('Yanwei Fu')
    #ego_network('Zhongyu Wei')
    ego_network('Xiangyang Xue')
    name=input("请输入学者的姓名\n")
    ego_network(name)
if __name__ == '__main__':
    main()
