
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
if(__name__ == '__main__') :
    start_time = time.time()
    pointlist = read_2D_points_from_file_make_pointlist()

def grahamscan(pointlist) :
    #make lexicographically ordered list of 2D points (smallest-to-largest)  
    tuplelist = []
    for point in pointlist :
        tuplelist.append((point.x,point.y))
    orderedlist = get_sorted_2D_points_list(tuplelist)

    Lupper = []
    Lupper.append(orderedlist[0])
    Lupper.append(orderedlist[1])
    for i in range(2,len(orderedlist)) :
        Lupper.append(orderedlist[i])
        while (len(Lupper)>2 
        and OrientationPredicate2D(Lupper[-1],Lupper[-2],Lupper[-3]) != 1) :
            Lupper.pop(-2)
    Llower = []
    Llower.append(orderedlist[-1])
    Llower.append(orderedlist[-2])
    for i in range(len(orderedlist)-3,-1,-1) :
        Llower.append(orderedlist[i])
        while (len(Llower)>2 
        and OrientationPredicate2D(Llower[-1],Llower[-2],Llower[-3]) != 1) :
            Llower.pop(-2)

    Llower.pop(0)
    Llower.pop()
    L = Lupper+Llower
    #clockwise order
    return L 

def grahamplot(convexhull,pointlist) :
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
    #plt.show()


if(__name__ == '__main__') :
    convexhull = grahamscan(pointlist)
    end_time = time.time()
    print(len(convexhull))
    print(convexhull)
    grahamplot(convexhull,pointlist)
    plt.show()
    elapsed_time = end_time - start_time
    print(f"Elapsed Time: {elapsed_time} seconds")

