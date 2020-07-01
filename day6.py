from typing import Tuple
import copy

with open("Inputs/6/input.txt", "r") as f:
    inp = f.read().splitlines()

class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        else:
            return False

points = []

for line in inp:
    sep = line.split(",")
    x = int(sep[0])
    y = int(sep[1][1:])
    points.append(Point(x,y))

def partA():
    finite_points = []

    for point in points:
        # a point extends forever if there exists no other point further in one of the cardinal directions
        # i.e. one of the values below remains false

        has_above = False
        has_below = False
        has_left  = False
        has_right = False

        for other_point in points:
            if other_point == point:
                continue

            if other_point.y > point.y:
                has_below = True
            elif other_point.y == point.y:
                has_below = False
                has_above = False
            else:
                has_above = True

            if other_point.x > point.x:
                has_right = True
            elif other_point.x == point.x:
                has_right = False
                has_left = False
            else:
                has_left = True

        if has_above and has_below and has_left and has_right:
            finite_points.append(point)

    for point in finite_points:
        largest_area = -1

        area = get_point_area(point)
        print(area)
        if largest_area == -1 or area > largest_area:
            largest_area = area

    print("Largest: " + str(largest_area))

def get_point_area(point: Point):
    # work in expanding loops around the point
    # loop until none in the current survey belong to point
    # do row then edge columns
    count = 0
    ring_num = 1

    while True:
        match = False
        for y in range(-ring_num, ring_num + 1):
            if y == ring_num or y == -ring_num:
                for x in range(-ring_num, ring_num + 1):
                    # test whole row
                    closest, ambig = get_closest_point(Point(x + point.x, y + point.y))
                    if closest == point and not ambig:
                        count += 1
                        match = True

            else: # only do extremes
                # test left
                closest, ambig = get_closest_point(Point(-ring_num + point.x, y + point.y))
                if closest == point and not ambig:
                    count += 1
                    match = True
                # test right
                closest, ambig = get_closest_point(Point(ring_num + point.x, y + point.y))
                if closest == point and not ambig:
                    count += 1
                    match = True

        if match:
            ring_num += 1
        else:
            break

    return count + 1 # include itself

def _get_manhattan(pointA: Point, pointB: Point) -> int:
    tracking_point = copy.deepcopy(pointA)
    distance = 0

    while tracking_point != pointB:
        if tracking_point.y < pointB.y:
            tracking_point.y += 1
            distance += 1
        elif tracking_point.y > pointB.y:
            tracking_point.y -= 1
            distance += 1

        if tracking_point.x < pointB.x:
            tracking_point.x += 1
            distance += 1
        elif tracking_point.x > pointB.x:
            tracking_point.x -= 1
            distance += 1

    return distance

def get_closest_point(location: Point) -> Tuple[Point, bool]:
    shortest_dists = []
    shortest_point = Point(0,0)
    for point in points:
        dist = _get_manhattan(location, point)
        if not shortest_dists or dist < min(shortest_dists):
            shortest_dists.append(dist)
            shortest_point = point

    if shortest_dists.count(min(shortest_dists)) > 1: # ambigious point
        return shortest_point, True

    return shortest_point, False

partA()