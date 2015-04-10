graph = {'A':set(['B','C']),
         'B':set(['A','D','E' ]),
         'C':set(['A','F' ]),
         'D':set(['B' ]),
         'E':set([
                  'B','F' ]),
         'F':set(['C', 'E','G']),
         'G':set(['F']),
         }

def DFS(graph,start):
    "it use stack"
    import pdb; pdb.set_trace()
    visited, stack = set(),[start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

#print DFS(graph,'A')

def dfs_rec(graph,start,visited=None,counter=None,visited_track=None):
    print "Visited", visited, start
    if visited is None:
        visited = set()
        counter = 1
        visited_track = set()
    
    visited.add(start)
    visited_track.add((start,counter))
    counter +=1
    for next in (graph[start] - visited):
        print "Value of this loop", graph[start] - visited
        print "in loop",next
        dfs_rec(graph,next,visited,counter,visited_track)
    return visited,visited_track


def dfs_path(graph,start,goal):
    import pdb; pdb.set_trace()
    stack = [(start,[start])]
    final = []
    while stack:
        (vertex,path ) = stack.pop()
        for next_val in graph[vertex] -set(path):
            if next_val == goal:
                final.append(path + [next_val]) 
            else:
                stack.append((next_val, path +  [next_val]))
    return final
print dfs_path(graph,'A','F')




