import re
from points import R2Point
from points import OrientationPredicate2D
from points import get_sorted_2D_points_list, get_sorted_2D_points_list_pointlist_arg , get_point_line_distance, get_line_ABC
from grahamscan import grahamscan,grahamplot
from convexhullutil import get_vertex_list_clockwise, read_2D_points_from_file_make_pointlist ,find_index_list 
import numpy as np
import matplotlib.pyplot as plt
import time 

start_time = time.time()

#part that reads from a textfile and makes list of points

pointlist = read_2D_points_from_file_make_pointlist()
pointlistcopy = pointlist.copy()

#make lexicographically ordered list of 2D points (smallest-to-largest)  
orderedlist = get_sorted_2D_points_list_pointlist_arg(pointlist)


# find 4 maximal points max x min x max y min y

leftmostpoint = orderedlist[0]
rightmostpoint = orderedlist[len(orderedlist)-1]
highestpoint = pointlist[0]
lowestpoint = pointlist[0]
for point in pointlist :
    if point.y > highestpoint.y :
        highestpoint = point
    if point.y < lowestpoint.y :
        lowestpoint = point

#if not unique, exit
if leftmostpoint == highestpoint or rightmostpoint == highestpoint or leftmostpoint == lowestpoint or rightmostpoint == lowestpoint or highestpoint == lowestpoint or rightmostpoint == leftmostpoint :
    print("the 4 points are not unique, terminating!")
    exit()


#divide in 4 areas each represented by 2 neighbouring maximal points left-top, left-bottom, right-top, right-bottom
#first top->left, then left->bottom, then bottom->right, then right->top
#find points to the right of their lines, positive orientation
#how to check if point is inside of the shape
#from the 4 previously defined lines, check if a given point has negative orientation from all 4

#what is the point with maximum distance from a line, from every point, draw a line that hits the previous line doing 90 degree angle
#could that be equivalent to maximum triangle space?

#trim down the points to the left of the lines
count = 0
for point in pointlist :
    if OrientationPredicate2D(highestpoint, leftmostpoint, point) == 1 and OrientationPredicate2D(leftmostpoint,lowestpoint,point) == 1 and OrientationPredicate2D(lowestpoint,rightmostpoint,point) == 1 and OrientationPredicate2D(rightmostpoint,highestpoint,point) == 1 :
        pointlist.remove(point)
        #print("Removed point")
        #print(point)
        count = count + 1
print("Trimmed points :")
print(count)
#y = c1x + c2
#topy = c1topx + c2
#lefty = c1leftx + c2
#c2 = topy - c1topx  !!!
#c1 = (lefty - c2)/leftx
#c1 = (lefty - topy - c1topx)/leftx
#c1 = lefty/leftx - topy/leftx - c1topx/leftx
#(topx/leftx +1)c1 = lefty/leftx - topy/leftx 
#c1 = (lefty/leftx - topy/leftx )/(topx/leftx +1) !!!

#y-c1x - c2 = 0 
#-c1x +y -c2 = 0
#Ax+By+ C = 0
#A = -c1
#B = 1
#C = -c2
c1 = []
c2 = []
A = []
B = []
C = []
#top, left, bottom, right
extremes = [highestpoint,leftmostpoint, lowestpoint, rightmostpoint]
print(extremes)
for i in range(0,4) :
    #later made a function that does that
    #c1.append((extremes[(i+1)%4].y/extremes[(i+1)%4].x - extremes[i].y/extremes[(i+1)%4].x )/(extremes[i].x/extremes[(i+1)%4].x +1))
    c1.append((extremes[(i+1)%4].y-extremes[i].y)/(extremes[(i+1)%4].x - extremes[i].x))
    c2.append((extremes[i].y - c1[i] * extremes[i].x))
    A.append(c1[i]*(-1))
    B.append(1)
    C.append(c2[i]*(-1))


def quickhull_method(extreme1,extreme2,Spointset,line_A,line_B,line_C) :
    #the extreme points are still in the Spointset
    if len(Spointset) == 0:
        return[(extreme1,extreme2)]
    else :
        max_distance = -1
        index = -1
        #print(len(Spointset))
        for i in range(0,len(Spointset)) :
            if max_distance < get_point_line_distance(Spointset[i],line_A,line_B,line_C) and OrientationPredicate2D(extreme1,extreme2,Spointset[i]) == -1:
                max_distance = get_point_line_distance(Spointset[i],line_A,line_B,line_C)
                print(max_distance, Spointset[i])
                index = i
        if(index == -1) :
            print(extreme1,extreme2)
            #for the small dataset, there are no points outside the top-left line, so what should the behavior be?
            print("No such point, returning extremes")
            return[(extreme1,extreme2)]
        Gamma = Spointset[index]
        M = []
        N = []
        for point in Spointset :
            if OrientationPredicate2D(extreme1, Gamma, point) == -1 :
                M.append(point)

            if OrientationPredicate2D(Gamma, extreme2, point) == -1 :
                N.append(point)
        #find A B C of new line
        print("For Extremes")
        print(extreme1)
        print(extreme2)
        print("Gamma is")
        print(Gamma)
        l1_ABC = get_line_ABC(extreme1,Gamma)
        l2_ABC = get_line_ABC(Gamma,extreme2)
        return quickhull_method(extreme1,Gamma,M,l1_ABC[0],l1_ABC[1],l1_ABC[2]) + quickhull_method(Gamma,extreme2,N,l2_ABC[0],l2_ABC[1],l2_ABC[2])
    
quadrantconvexhulls = []

for i in range(0,4) :
   quadrantconvexhulls = quadrantconvexhulls + quickhull_method(extremes[i],extremes[(i+1)%4],pointlist,A[i],B[i],C[i])
print(len(quadrantconvexhulls))
convexhull = get_vertex_list_clockwise(quadrantconvexhulls)
#this is a slow function but it should be fine for now
print(len(convexhull))
#print(convexhull)
#convexhull = list(dict.fromkeys(convexhull))
grahamplot(convexhull,pointlistcopy)
end_time = time.time()
plt.show()
#print(quadrantconvexhulls)
elapsed_time = end_time - start_time
print(f"Elapsed Time: {elapsed_time} seconds")