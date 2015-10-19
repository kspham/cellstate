__author__ = 'nadya'
import math
import mst

class Point:
    def __init__(self, sample_name, coordinates):
        self.name = sample_name
        self.coords = coordinates

def standard_normalization(points, _):
    for point in points:
        length = math.sqrt(sum([x * x for x in point.coords])) / 10000
        point.coords = [float(x) / length for x in point.coords]

def binary_normalization(points, cutoff):
    for point in points:
        point.coords = [int(x > cutoff) for x in point.coords]

def read_points(filename):
    with open(filename, 'r') as file:
        sample_names = file.readline().split()[1:]
        points = [Point(name, []) for name in sample_names]
        line = file.readline()
        while line:
            coordinates = line.split()[1:]
            for i in range(len(points)):
                points[i].coords.append(int(coordinates[i]))
            line = file.readline()
    return points

def cell_state(input_file, normalization, cutoff, distance_metric):
    points = read_points(input_file)
    normalization(points, cutoff)
    return mst.mst(points, distance_metric)


"""mst1 = cell_state("data/data.txt", standard_normalization, None, mst.euclidean_distance)
mst2 = cell_state("data/data.txt", binary_normalization, 500, mst.euclidean_distance)
common = 0
for edge in mst1:
    if edge in mst2:
        common += 1
print(common)""




