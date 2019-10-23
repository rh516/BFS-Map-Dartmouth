# CS1 Lab 4 breadth first search function
# Ray Huang
# 11/14/17

from collections import deque


def bfs(start, end): # creates queue, adds vertices from adj_list, creates backpointer dictionary, constructs path
    back_dict = {}
    back_dict[start] = None
    q = deque()
    q.append(start)
    while len(q) != 0:
        vertex = q.popleft()
        if vertex.name == end.name:
            path = [vertex]
            while back_dict[end]!= None:
                path.append(back_dict[end])
                end = back_dict[end]
            return path
        else:
            for v in vertex.adj_list:
                if v not in back_dict:
                    back_dict[v] = vertex
                    q.append(v)
    return []






