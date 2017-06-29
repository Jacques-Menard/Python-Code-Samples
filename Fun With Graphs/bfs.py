from queue1210 import *
from basicgraph import *

#####
#
# classic Breadth First Search
#
# See, e.g., 
#

def bfs(graph, startNode):
    for n in graph.nodes:
        n.setStatus('unseen')
    startNode.setStatus('seen')
    print("Initializing queue with: ", startNode.name)
    queue = Queue()
    queue.enqueue(startNode)
    while queue.size() != 0:
        print(queue)
        currentNode = queue.dequeue()
        print("removed {} from queue. Processing neighbors".format(currentNode.name))
        for node in graph.neighborsOf(currentNode):
            if node.getStatus() == 'unseen':
                node.setParent(currentNode)
                node.setStatus('seen')
                queue.enqueue(node)
        currentNode.setStatus('processed')

