# CS1 Lab 4 load_graph File
# Ray Huang
# 11/9/17

from vertex import Vertex


def load_graph(text):
    vertex_dict = {}
    file = open(text, "r")
    for line in file:  # creates Vertex object from split, adds to dictionary as reference
        line.strip()
        x = line.split(";")
        y = x[2].split(",")
        v = Vertex(x[0], int(y[0]), int(y[1]))
        vertex_dict[x[0]] = v
    file.close()
    file2 = open(text,"r")  # adds adjacent vertices list to dictionary of object references
    for line in file2:
        line.strip()
        a = line.split(";")
        b = a[1].split(",")
        for n in b:
            vertex_dict[a[0]].adj_list.append(vertex_dict[n.strip()])
    file2.close()
    return vertex_dict



