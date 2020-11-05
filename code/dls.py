from collections import deque
def dls(graph, src_node,dest_node,maxDepth): 
        queue = []
        path=[]
        found=False
        queue.append(src_node)
        level={}
        level[src_node]=0
        keys=list(graph)
        while((len(queue)!=0)):
                  if queue[-1]==dest_node:
                    found=True
                    path.append(queue.pop())  
                    break
                  elif queue[-1] not in keys:
                    path.append(queue.pop())               
                  elif queue[-1] in keys:  
                    if level[queue[-1]]< maxDepth-1:
                     V=queue[-1]
                     path.append(queue.pop())
                     for l  in range(len(graph[V])):
                        if graph[V][l] not in path: 
                         level[graph[V][l]]=level[V]+1
                         queue.append(graph[V][l])
                    else:
                       path.append(queue.pop())
        if found==True:
           print("DLS:Optimal path from {} to {} is {}. \n At level:{}.\n After traversing: {} nodes".format(src_node,dest_node,path,level[dest_node],len(path)))
           print('-'*50)
        elif found==False:
           print("DLS:Target {} is NOT reachable from source {},within depth= {} levels ".format(dest_node,src_node,maxDepth)) 
           print('-'*50)
        del queue
     
