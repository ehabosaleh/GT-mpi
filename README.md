# GT-mpi
For PC with 4-cores processor we harness each core to find the optimal path in a tree or graph. All cores share the graph, starting node and target node, but each one uses different search algorithm. We utilized three cores to run the search algorithms and one core to emerge the elapsed time it takes for each core to reach the target node.
The used uninformed search algorithms are:
## Depth First Search (DFS.py)
It is a recursive algorithm because it traverses all the nodes in a possible path utill it reaches the deepest node before it moves to the next path. DFS uses the Stack data structured to store the path and it needs less memory and time to reach the target node from the starting node. The main disadvantage of using DFS is that it might search deeper and deeper in an infinite loop. Figure below shows the order in which nodes are expanded when we use DFS algorithm.
<src=https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Depth-first-tree.svg/1024px-Depth-first-tree.svg.png" width="200" height="200">
## Depth Limited Search (DLS.py)
DLS algorithm presents a new version of DFS algorithm as it uses the same implementation steps but with given predetermined depth which used to consider that there is no possible solution further. This given limit solves the infinite loop drawback of the DFS algorithm. 
## Bridth First Search (BFS.py)
This is the most common used uninformed search algorithm for traversing a tree or a graph. Instead of the recursive traversing, it traverses through the graph breadthwise, level after level until it reaches the target node. The used data structure is First In First Out (FIFO).
Figure below shows the order in which nodes are expanded when we use BFS algorithm. 
![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Breadth-first-tree.svg/1024px-Breadth-first-tree.svg.png)

## License
[MIT](https://choosealicense.com/licenses/mit/)
