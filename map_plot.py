# CS1 Lab 4 map_plot
# Ray Huang
# 11/14/17

from cs1lib import *
from load_graph import load_graph
from bfs import bfs

draw_background = True
start = None
v_dict = load_graph("Data/dartmouth_graph.txt")


def background():  # draws background
    img = load_image("Data/dartmouth_map.png")
    draw_image(img, 0, 0)


def draw():
    global draw_background, start_chosen, start
    if draw_background:  # draws background once, stops
        background()
        draw_background = False
    for key in v_dict:  # draws vertices and edges in blue
        vertex = v_dict[key]
        vertex.draw_vertex(0, 0, 1)
        for item in vertex.adj_list:
            vertex.draw_edge(item, 0, 0, 1)
    for key in v_dict:  # chooses start, end, draws them in red, executes BFS, draws path from BFS in red
        vertex = v_dict[key]
        if vertex.is_pressed(vertex.x, vertex.y):
            start = vertex
        if start != None:
            start.draw_vertex(1, 0, 0)
            if vertex.in_square(vertex.x, vertex.y) and vertex.name != start.name:
                end = vertex
                if end != None:
                    end.draw_vertex(1, 0, 0)
                    path = bfs(start, end)
                    prev = None
                    for v in path:
                        if prev != None:
                            v.draw_edge(prev, 1, 0, 0)
                        prev = v


start_graphics(draw, width=1012, height=811)

