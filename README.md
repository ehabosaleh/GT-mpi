# GT-mpi
For PC with 4-cores processor we harness each core to find the optimal path in a tree or graph. All cores share the graph, starting node and target node, but each one uses different search algorithm. We utilized three cores to run the search algorithms and one core to emerge the elapsed time it takes for each core to reach the target node.
The used uninformed search algorithms are:
## Depth First Search (DFS.py)
It is a recursive algorithm because for each possible path it traverse all the node in each path till it reaches the deepest node before moving to the next path. It used the Stack data structured to store the path and it needs less memory and time to reach the target node from the starting node. The main disadvantage of using DFS is that it might search deeper and deeper in infinite loop.
## Depth Limited Search (DLS.py)
DLS algorithm presents a new version of DFS algorithm as it uses the same implementaion steps but with given predetermined depth which used to consider that there is no possible solution further. This given limit solves the infinite loop drwaback of the DFS algorithm. 
## Bridth First Search (BLS.py)
This is the most common used uninformed search algorithm for traversing a tree or a graph. Instead of the recursive traversing, it traverses through the graph breadthwise, level after level until it reaches the target node

## License
[MIT](https://choosealicense.com/licenses/mit/)
