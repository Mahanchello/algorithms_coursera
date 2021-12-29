# Implement function, which performs a breadth-first search on a graph 
# and returns an array of objects describing each vertex.
# Example: do_bfs(graph, index)


# To solve this task we need to use queue data structure. 
# Create queue data structure 

class Queue: 
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        return self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return len(self.items) == 0   


def do_bfs(graph, index):
    bf_arr = []
    for i in range(len(graph)):
        bf_arr.append([])
        bf_arr[i] = {
            'predecessor': None,
            'distance': None
        }   
    bf_arr[index]['distance'] = 0
    queue = Queue()
    queue.enqueue(index)

    while(queue.isEmpty() == False):
        vertex = queue.dequeue()
        for i in range(len(graph[vertex])):
            neighbour = graph[vertex][i]
            if(bf_arr[neighbour]['distance'] == None):
                bf_arr[neighbour]['distance'] = 1 + bf_arr[vertex]['distance']
                bf_arr[neighbour]['predecessor'] = vertex

                queue.enqueue(neighbour)

    return bf_arr            

adjList = [
    [1],
    [0, 4, 5],
    [3, 4, 5],
    [2, 6],
    [1, 2],
    [1, 2, 6],
    [3, 5],
    []
    ]
bfsInfo = do_bfs(adjList, 3)
expectedRes = [{ 0: {'predecessor': 1, 'distance': 4}}, {1: {'predecessor': 4, 'distance': 3}}, {2: {'predecessor': 3, 'distance': 1}}, {3: {'predecessor': None, 'distance': 0}}, {4: {'predecessor': 2, 'distance': 2}}, {5: {'predecessor': 2, 'distance': 2}}, {6: {'predecessor': 3, 'distance': 1}}, {7: {'predecessor': None, 'distance': None}}]
for i in range(len(bfsInfo)):
    assert bfsInfo[i]['predecessor'] == expectedRes[i]['predecessor'] and bfsInfo[i]['distance'] == expectedRes[i]['distance']
# print(bfsInfo, 'bfsInfo')
for i in range(len(bfsInfo)):
    print("vertex " + str(i) + ": distance = " + str(bfsInfo[i]['distance']) + ", predecessor = " + str(bfsInfo[i]['predecessor']))



