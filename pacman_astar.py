import sys
import time
from demo_grid import *
data=[['#','#','#','#','#','#','#','#'],['#','-','-','-','-','-','-','#'],['#','-','#','#','#','-','-','#'],['#','-','#','*','#','-','-','#'],['#','-','-','-','#','-','-','#'],['#','-','#','#','#','-','-','#'],['#','p','-','-','-','-','-','#'],['#','#','#','#','#','#','#','#']]
length=8
class Node:
    root=None
    def __init__(self,parent,level,a,b):
        self.parent=parent
        self.level=level
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
                self.children[k]=Node(self,(self.level)+1,i,j)
            k+=1

    def valid_node(self,i,j):
        if (data[i][j]!='#') and (i>=0) and (j>=0) and (i<length) and (j<length) and ([i,j] not in visited_node):
            return True
        return False

    def fval(self,goal):
        return self.h(goal)+self.g()
    def h(self,goal):
        return abs(self.x-goal[0])+abs(self.y-goal[1])
    def g(self):
        return self.level

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

def solver(frontier,goal):
    visited_node_list=[]
    while frontier!=[]:
            current_node=frontier[0]
            current_node.generate_children()
            for child in current_node.children:

                if child !=None and [child.x,child.y]==goal:
                    return child
                if child != None and (child  not in visited_node_list) :
                    frontier.append(child)
            visited_node_list.append(current_node)
            frontier=frontier[1:]
            frontier.sort(key = lambda k:k.fval(goal),reverse=False)

start=[6,1]
goal=[3,3]
visited_node=[]
root=Node(None,0,start[0],start[1])
frontier=[root]
goal_node=solver(frontier,goal)
path=[]
cur=goal_node
while cur.parent !=   None:
    path.append(list([cur.x,cur.y]))
    cur=cur.parent
path.reverse()
#DataPrint(data)
print(path)
pacman_viewer(path=path,data=data)
