# CS1 Lab 4 Map Vertex Class
# Ray Huang
# 11/9/17

from cs1lib import *

VERTEX_RAD = 7


class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.adj_list = []

    def draw_vertex(self, r, g, b):
        disable_stroke()
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, VERTEX_RAD)

    def draw_edge(self, object2, r, g, b):
        enable_stroke()
        set_stroke_width(4)
        set_stroke_color(r, g, b)
        draw_line(self.x, self.y, object2.x, object2.y)

    def is_pressed(self, x, y):  # checks if mouse is pressed and is placed in vertex
        return is_mouse_pressed() and self.in_square(x, y)

    def in_square(self, x, y):  # checks if mouse is placed on vertex
        if mouse_x() <= x + VERTEX_RAD and mouse_x() >= x - VERTEX_RAD and mouse_y() <= y + VERTEX_RAD and mouse_y() >= y - VERTEX_RAD:
            return True

    def __str__(self):  # prints name of place, coordinates of location, and adjacent locations (no brackets)
        list_string = ""
        for i in self.adj_list:
            list_string = list_string + str(i.name) + ", "
        list_string = list_string[:len(list_string) - 2]
        return str(self.name) + "; " + " Location: " + str(self.x) + " , " + str(self.y) + "; " + " Adjacent Vertices: " + list_string