from scipy import spatial as scisp
import numpy as np

with open("Inputs/6/input.txt", "r") as f:
    inp = f.read().splitlines()

_manhattan = 1

points = []

# split points
x_left_edge = -1
x_right_edge = -1
y_top_edge = -1
y_bottom_edge = -1

for line in inp:
    sep = line.split(",")
    x = int(sep[0])
    y = int(sep[1][1:])

    points.append([x,y])

    if x_left_edge == -1 or x < x_left_edge:
        x_left_edge = x
    if x_right_edge == -1 or x > x_right_edge:
        x_right_edge = x
    if y_top_edge == -1 or y < y_top_edge:
        y_top_edge = y
    if y_bottom_edge == -1 or y > y_bottom_edge:
        y_bottom_edge = y

tree = scisp.KDTree(points)
dist, index = tree.query([0,4], k = 2, p = _manhattan)

arrayx = x_right_edge - x_left_edge
arrayy = y_bottom_edge - y_top_edge
nodes = np.zeros([arrayy, arrayx], dtype=int)

for x in range(x_left_edge, x_right_edge):
    for y in range(y_top_edge, y_bottom_edge):
        dist, index = tree.query([x,y], k = 2, p = _manhattan)

        if len(set(dist)) >= 1:
            nodes[y - y_top_edge, x - x_left_edge] = index[0]
        else:
            nodes[y - y_top_edge, x - x_left_edge] = -1

_, counts = np.unique(nodes, return_counts=True)
print(max(counts))