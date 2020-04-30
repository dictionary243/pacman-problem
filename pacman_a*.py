import sys
import time
from functions import *
node_dict={ }#{[1,2]:1,[1,3]:2}
index_dict={ }#{1:[1,2],2:[1,3]}
data=[['#','#','#','#','#','#','#','#'],['#','-','-','-','-','-','-','#'],['#','-','#','#','#','-','-','#'],['#','-','#','*','#','-','-','#'],['#','-','-','-','#','-','-','#'],['#','-','#','#','#','-','-','#'],['#','p','-','-','-','-','-','#'],['#','#','#','#','#','#','#','#']]
path_matrix=[]

[node_dict,index_dict]=create_dictionary(data)
path_matrix= create_path_matrix(index_dict)

start=[6,1]
goal=[3,3]

dist_vector=djikistra(goal,path_matrix,node_dict)
print(dist_vector)
#print_it(data,dist_vector,node_dict)
path=solver(start,goal,node_dict,data,dist_vector)
print("path is :"+str(path))
