import re
from points import R2Point
from points import OrientationPredicate2D
from points import get_sorted_2D_points_list
from convexhullutil import get_vertex_list_clockwise
from convexhullutil import read_2D_points_from_file_make_pointlist
import numpy as np
import matplotlib.pyplot as plt
import time

#part that reads from a textfile and makes list of points
start_time = time.time()
pointlist = read_2D_points_from_file_make_pointlist()

minpoint = pointlist[0]
#find leftmost point
position = 0
minposition = position
for point in pointlist :
    if point.x < minpoint.x :
        minpoint = point
        minposition = position
    elif point.x == minpoint.x and point.y < minpoint.y :
        minpoint = point
        minposition = position
    position = position + 1
leftmost_point = minpoint

confirmed_points = []
confirmed_points.append(leftmost_point)
pointlistclone = pointlist.copy()
pointlistclone.pop(minposition)
#print(pointlist)
#print(pointlistclone)
#made a clone of point list to pop leftmost element firs to make sure initial u is not leftmost
pointlistclone2 = pointlist.copy()
#made a second clone since I will pop points from the original, I keep this one for the plot



u = pointlistclone[0]
r = leftmost_point
while (u != leftmost_point) :
    for t in pointlist :
        #print(r)
        #print(u)
        #print(t)
        #print(OrientationPredicate2D(r,u,t))
        if OrientationPredicate2D(r,u,t) == -1 or (OrientationPredicate2D(r,u,t) == 0 and r!=t)  :
            u = t
    if (u == leftmost_point):
        break
    else :
        r = u
        print(r)
        pointlist.remove(r)
        confirmed_points.append(r)

convexhull = confirmed_points
xcords = []
ycords = []
#split points into cords to print them
print(len(convexhull))
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
for point in pointlistclone2 :
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
    



