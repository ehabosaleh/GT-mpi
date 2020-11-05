from collections import deque
def bfs(graph, src_node,dest_node): 
        queue = deque()
        que =deque()
        path=[]
        found=False
        queue.append(src_node)
        keys=list(graph)
        if queue[0]==dest_node:
          path.append(queue.popleft())
        else:
         while(found==False):
           que=queue.copy()
           for j in range(len(que)):
                  if que[j]==dest_node:
                    found=True
                    path.append(queue.popleft())  
                    break
                  elif que[j] not in keys:
                     path.append(queue.popleft()) 
                  elif que[j] in keys:
                     for l  in range(len(graph[que[j]])):
                        if graph[que[j]][l] not in queue and graph[que[j]][l] not in path:
                          queue.append(graph[que[j]][l])
                     path.append(queue.popleft())
           if len(queue)==0:
                 break;            
        if found==True:
           print("BFS:Optimal path from {} to {} is {} after traversing: {} nodes".format(src_node,dest_node,path,len(path)))
           print('-'*50)
        elif found==False:
           print("BFS:Target {} is NOT reachable from source {} using BFS".format(dest_node,src_node)) 
        del queue
        del que
        
