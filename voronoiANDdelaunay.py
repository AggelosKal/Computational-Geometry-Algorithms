import re
from points import R2Point
from points import OrientationPredicate2D
from points import get_sorted_2D_points_list
from points import read_2D_points_from_file_make_tuplelist
from convexhullutil import get_vertex_list_clockwise
from convexhullutil import read_2D_points_from_file_make_pointlist
import numpy as np
import matplotlib.pyplot as plt
import time

from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d

tuplelist = np.array(read_2D_points_from_file_make_tuplelist())

the_delaunay = Delaunay(tuplelist)
the_voronoi = Voronoi(tuplelist)
voronoi_plot_2d(the_voronoi)
plt.show()

plt.triplot(tuplelist[:, 0], tuplelist[:, 1], the_delaunay.simplices)
plt.scatter(tuplelist[:, 0], tuplelist[:, 1], color='r')
plt.show()

voronoi_plot_2d(the_voronoi)
plt.triplot(tuplelist[:, 0], tuplelist[:, 1], the_delaunay.simplices)
plt.scatter(tuplelist[:, 0], tuplelist[:, 1], color='r')
plt.show()

#the complexity for voronoi and delaunay is O(nlogn) where n is the number of points we have, 
#one is the dual graph of the other
#O(nlogn) is very scaleable so a large number of points is not a problem