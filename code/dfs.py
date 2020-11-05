from collections import deque
   
def dfs(graph, src_node,dest_node): 
        queue = []
        path=[]
        found=False
        queue.append(src_node)
        keys=list(graph)
        while(len(queue)!=0):
                  if queue[-1]==dest_node:
                    found=True
                    path.append(queue.pop())  
                    break
                  elif queue[-1] not in keys:
                     path.append(queue.pop()) 
                  elif  queue[-1] in keys:
                     V=queue[-1]
                     path.append(queue.pop())
                     for l  in range(len(graph[V])):
                        if  graph[V][l] not in path:
                         queue.append(graph[V][l])
        if found==True:
           print("DFS:Optimal path from {} to {} is {} after traversing: {} nodes".format(src_node,dest_node,path,len(path)))
           print('-'*50)
        elif found==False:
           print("DFS:Target {} is NOT reachable from source {}  using DFS".format(dest_node,src_node)) 
           print('-'*50) 
        del queue
