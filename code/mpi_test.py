from dls import dls
from bfs import bfs
from dfs import dfs
from mpi4py import MPI
import time
import random as rn
comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()

def random_graph(vertex_num,edge_num_vertex):
       graph={}
       for l in range(vertex_num):
         key=l
         lst=list(graph)   
         graph[key]=[] 
         for k in range(edge_num_vertex+1):
              node=rn.randint(key,vertex_num)
              if node not in graph[key]:
                graph[key].append(node)
       return graph
       
if rank==0:
   t=[]
   graph=random_graph(1000,4)
   print(graph)
   for i in range(1,size):
     comm.send(graph,dest=i,tag=1)
   for i in range(1,size):
     data=comm.recv(source=i,tag=1)
     t.append(data)

   print("BFS executing time in core 1 is: {} ms".format(t[0]*1000))
   print("DFS executing time in core 2 is: {} ms".format(t[1]*1000))
   print("DLS executing time in core 3 is: {} ms".format(t[2]*1000))

if rank==1:
  data_1=comm.recv(source=0,tag=1)
  t1=time.process_time()
  bfs(data_1,list(data_1)[0],data_1[list(data_1)[-1]][0])
  t2=time.process_time()
  comm.send((t2-t1),dest=0,tag=1)

if rank==2:
  data_2=comm.recv(source=0,tag=1)
  t1=time.process_time()
  dfs(data_2,list(data_2)[0],data_2[list(data_2)[-1]][0])
  t2=time.process_time()
  comm.send((t2-t1),dest=0,tag=1)

if rank==3:
  depth=100
  data_3=comm.recv(source=0,tag=1)
  t1=time.process_time()
  dls(data_3,list(data_3)[0],data_3[list(data_3)[-1]][0],depth)
  t2=time.process_time()
  comm.send((t2-t1),dest=0,tag=1)
