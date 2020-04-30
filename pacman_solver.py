import time

data=[['#','#','#','#','#','#','#','#'],['#','-','-','-','-','-','-','#'],['#','-','#','#','#','-','-','#'],['#','-','#','*','#','-','-','#'],['#','-','-','-','#','-','-','#'],['#','-','#','#','#','-','-','#'],['#','p','-','-','-','-','-','#'],['#','#','#','#','#','#','#','#']]
visited_node=[]
length=8
class Node:
    root=None
    def __init__(self,parent,level,a,b,address):
        self.parent=parent
        self.level=level
        self.add=address
        self.x=a
        self.y=b
        self.children=[None,None,None,None] #lchild,uchild,rchild,dchild
        visited_node.append([self.x,self.y])

    def generate_children(self):
        a=self.x
        b=self.y
        pos=[[a,b-1],[a-1,b],[a,b+1],[a+1,b]]
        k=0
        position=["l","u","r","d"]
        for [i,j] in pos:
            if(self.valid_node(i,j)):
                self.children[k]=Node(self,(self.level)+1,i,j,self.add+position[k])
            k+=1
    def valid_node(self,i,j):
        if (data[i][j]!='#') and (i>=0) and (j>=0) and (i<length) and (j<length) and ([i,j] not in visited_node):
            return True
        return False

def DataPrint(data):
    for i in range(length):
        print(" ".join(str(x) for x in data[i] ))
        time.sleep(0.5)

def data_shuffle(current_pos,ch):
    data[current_pos[0]][current_pos[1]]='-'
    current_pos=position_from_char(current_pos,ch)
    data[current_pos[0]][current_pos[1]]='p'
    return [current_pos,data]

def position_from_char(pos,c):
    if c=="d":
        return [pos[0]+1,pos[1]]
    elif c=="u":
        return [pos[0]-1,pos[1]]
    elif c=="l":
        return [pos[0],pos[1]-1]
    else:
        return [pos[0],pos[1]+1]
start=[6,1]
goal=[3,3]
root=Node(None,0,start[0],start[1],"")
current_node_list=[root]
visited_node_list=[]
while current_node_list!=[]:
        current_node=current_node_list[0]
        current_node.generate_children()
        for child in current_node.children:
            if child != None:
                current_node_list.append(child)
        visited_node_list.append(current_node)
        current_node_list=current_node_list[1:]
result=""
for child in visited_node_list:
    if [child.x,child.y] == goal:
        result=child.add
DataPrint(data)
current_pos=start
for ch in result:
    print("        |              "+"\n        |              "+"\n        |              "+"\n        |              "+"\n        v             ")
    time.sleep(0.5)
    [current_pos,data]=data_shuffle(current_pos,ch)
    DataPrint(data)
