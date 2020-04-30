import sys
import time
def create_dictionary(data):
    count=0
    node_dict={}
    index_dict={}
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j]!='#':
                node_dict[tuple([i,j])]=count
                index_dict[count]=[i,j]
                count+=1
    return [node_dict,index_dict]

def is_neighbour(node1,node2):
    x,y=node1
    a,b=node2
    if (x==a and (y==b+1 or y==b-1)) or (y==b and (x==a-1 or x==a+1)):
        return True
    else:
        return False

def create_path_matrix(index_dict):
    length=len(index_dict)
    path_matrix=[]
    for i in range(length):
        temp=[]
        for j in range(length):
            if is_neighbour(index_dict[i],index_dict[j]):
                temp.append(1)
            elif i==j:
                temp.append(0)
            else:
                temp.append(sys.maxint)
        path_matrix.append(temp)
    return path_matrix

def extract_min(lis,visited_node):
    min_index=0
    for i in range(len(lis)):
        if visited_node[i]==0:
            min_index=i
    for i in range(len(lis)):
        if lis[i]<lis[min_index] and visited_node[i]==0:
            min_index=i
    count = 0
    for i in range(len(lis)):
        if visited_node[i]==1:
            count+=1
    if count==len(lis):
        return sys.maxint
    else:
        return min_index


def djikistra(goal,path_matrix,node_dict):
    goal_index=node_dict[tuple(goal)]
    dist=path_matrix[goal_index]
    visited_node=[]
    for i in range(len(dist)):
        if i==goal_index:
            visited_node.append(1)
        else:
            visited_node.append(0)
    current_node=extract_min(dist,visited_node)
    while current_node!=sys.maxint :
        visited_node[current_node]=1
        for i in range(len(dist)):
            if dist[current_node]+path_matrix[current_node][i]<dist[i]:
                dist[i]=dist[current_node]+path_matrix[current_node][i]
        current_node=(extract_min(dist,visited_node))
    return dist

def print_it(data,dist_vector,node_dict):
    temp_data=[]
    for i in range(len(data)):
        temp=[]
        for j in range(len(data)):
            if data[i][j]!='#':
                temp.append(dist_vector[node_dict[tuple([i,j])]])
            else:
                temp.append('#')
        temp_data.append(temp)
    for i in range(len(temp_data)):
        print(" ".join(str(x) for x in temp_data[i]))

def generate_children(node,data):
    [a,b]=node
    #print(str(a)+str(b))
    children=[]
    pos=[[a,b-1],[a-1,b],[a,b+1],[a+1,b]]
    for [i,j] in pos:
        if(valid_node(i,j,data)):
            children.append([i,j])
    return children

def valid_node(i,j,data):
    length=len(data)
    if (data[i][j]!='#') and (i>=0) and (j>=0) and (i<length) and (j<length):
        return True
    return False

def f(node,dist_vector,node_dict,level):
    return h(node,dist_vector,node_dict)+level

def h(node,dist_vector,node_dict):
    return dist_vector[node_dict[tuple(node)]]

def solver(start,goal,node_dict,data,dist_vector):
    current_node=start
    level=0
    path=[current_node]
    while current_node!=goal:
        print("current node is :"+str(current_node))
        children=generate_children(current_node,data)
        print("neighbour is:"+str(children))
        time.sleep(2)
        min=f(children[0],dist_vector,node_dict,level)
        current_node=children[0]
        for child in children:
            value=f(child,dist_vector,node_dict,level)
            if value<min:
                min=value
                current_node=child
        level+=1
        path.append(current_node)
        print("choosen node is:"+str(current_node))
    return path
