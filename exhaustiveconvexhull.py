import re
from points import R2Point
from points import OrientationPredicate2D
from convexhullutil import get_vertex_list_clockwise
from convexhullutil import read_2D_points_from_file_make_pointlist
import numpy as np
import matplotlib.pyplot as plt
import time

#part that reads from a textfile and makes list of points
start_time = time.time()
pointlist = read_2D_points_from_file_make_pointlist()


#after reading the points, will now check orientation to determine which edges to keep exhaustively
numberofpoints = len(pointlist)
listofedges = []
for point1 in pointlist :
    for point2 in pointlist :
        count = 0
        for point3 in pointlist :
            count = count + OrientationPredicate2D(point1,point2,point3)
        if count*(-1) == numberofpoints-2 :
            if (point1,point2) not in listofedges:
                listofedges.append((point1,point2))

#here we have a list of all the edges involved
vertexlist = get_vertex_list_clockwise(listofedges)
convexhull = []
for vertex in vertexlist :
    convexhull.append(vertex)
#there is one edge remaining
#print(listofedges[0])   
print(convexhull)
print(len(convexhull))
xcords = []
ycords = []
#split points into cords to print them
for thepoint in convexhull :
    xcords.append(thepoint.x)
    ycords.append(thepoint.y)
#will add the first point a second time to get the correct (closed-circular) plot
xcords.append(convexhull[0].x) 
ycords.append(convexhull[0].y)
xcordarray = np.array(xcords)
ycordarray = np.array(ycords)
plt.plot(xcordarray, ycordarray, marker = 'o')

#will plot both in one 
xlist = []
ylist = []
for point in pointlist :
    xlist.append(point.x)
    ylist.append(point.y)
#these arrays contain the entire set of points given
xcordarray2 = np.array(xlist)
ycordarray2 = np.array(ylist)
plt.plot(xcordarray2,ycordarray2, 'o')
end_time = time.time()
plt.show()
elapsed_time = end_time - start_time
print(f"Elapsed Time: {elapsed_time} seconds")

