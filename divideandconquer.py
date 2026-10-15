import re
from points import R2Point
from points import OrientationPredicate2D, are_equal
from points import get_sorted_2D_points_list, get_sorted_2D_points_list_pointlist_arg
from grahamscan import grahamscan,grahamplot
from convexhullutil import get_vertex_list_clockwise, read_2D_points_from_file_make_pointlist ,find_index_list 
import numpy as np
import matplotlib.pyplot as plt
import time

#part that reads from a textfile and makes list of points
start_time = time.time()
pointlist = read_2D_points_from_file_make_pointlist()

#make lexicographically ordered list of 2D points (smallest-to-largest)  
orderedlist = get_sorted_2D_points_list_pointlist_arg(pointlist)
#check if all x coordinates are unique
tol = 0.000000001
for i in range(1,len(orderedlist)) :
    if orderedlist[i].x - orderedlist[i-1].x >= 0-tol and orderedlist[i].x - orderedlist[i-1].x <= 0+tol :
        print("x coordinates need to be unique, terminating")
        exit()

Blen = len(orderedlist)//2
Alen = len(orderedlist) - Blen
A = []
for i in range(0, Alen) :
    A.append(orderedlist[i])
B = []
for i in range(Alen, len(orderedlist)) :
    B.append(orderedlist[i])

#find upper bridge
#find convex hull of A B

#the result from grahamscan is in clockwise order so I reverse the lists to get counterclockwise
conA = grahamscan(A)
conA.reverse()
conB = grahamscan(B)
conB.reverse()
sortedconA = get_sorted_2D_points_list_pointlist_arg(conA)
sortedconB = get_sorted_2D_points_list_pointlist_arg(conB)
#rightmost A
rightmostpointA = sortedconA[len(sortedconA)-1]
#print(rightmostpointA)

#i = conA.index(rightmostpointA)
i = find_index_list(conA,rightmostpointA)
#get index of rightmost point in A
#  
#leftmost B
leftmostpointB = sortedconB[0] 
#print(leftmostpointB)
#j = conB.index(leftmostpointB)
j = find_index_list(conB, leftmostpointB)
#get index of leftmost point in B

changeflag = True
while(changeflag == True) :
    changeflag = False
    #use modulo to make sure it doesn't go out of bounds
    #if it finds one result different from the previous one, it means they are not all in the same subspace anymore 
    #print((i+1)%(len(conA)))
    #print(len(conA))
    previous_orientation = OrientationPredicate2D(conA[i%(len(conA))],conA[(i+1)%(len(conA))],conB[j%(len(conB))]) 

    for count in range(0,len(conA)-2) :
        if previous_orientation != OrientationPredicate2D(conA[i%(len(conA))],conA[(i+1)%(len(conA))],conA[(i+2+count)%(len(conA))]) :
            i = (i+1)
            changeflag = True
            break
        previous_orientation = OrientationPredicate2D(conA[i%(len(conA))],conA[(i+1)%(len(conA))],conA[(i+2+count)%(len(conA))])


    previous_orientation = OrientationPredicate2D(conB[j%(len(conB))],conB[(j-1)%(len(conB))],conA[i%(len(conA))]) 
    for count in range(0,len(conB)-2) :
        if previous_orientation != OrientationPredicate2D(conB[j%(len(conB))],conB[(j-1)%(len(conB))],conB[(j-2-count)%(len(conB))]) :
            j = (j-1)
            changeflag = True
            break
        previous_orientation = OrientationPredicate2D(conB[j%(len(conB))],conB[(j-1)%(len(conB))],conB[(j-2-count)%(len(conB))])
UpperBridge = (conA[i%(len(conA))],conB[j%(len(conB))]) 

#Now to find lower bridge
leftmostpointA = sortedconA[0]
rightmostpointB = sortedconB[len(sortedconB)-1]
#conA.reverse()
#i = find_index_list(conA,rightmostpointA)
#i = find_index_list(conA,leftmostpointA)
i = find_index_list(conA,rightmostpointA)

#get index of leftmost point in A
#  
#leftmost B
#j = find_index_list(conB, leftmostpointB)
#j = find_index_list(conB, rightmostpointB)
#get index of rightmost point in B
j = find_index_list(conB, leftmostpointB)

changeflag = True
while(changeflag == True) :
    changeflag = False
    #use modulo to make sure it doesn't go out of bounds
    #if it finds one result different from the previous one, it means they are not all in the same subspace anymore 

    previous_orientation = OrientationPredicate2D(conA[i%(len(conA))],conA[(i-1)%(len(conA))],conB[j%(len(conB))]) 
    for count in range(0,len(conA)-2) :
        if previous_orientation != OrientationPredicate2D(conA[i%(len(conA))],conA[(i-1)%(len(conA))],conA[(i-2-count)%(len(conA))]) :
            i = i-1
            changeflag = True
            break
        previous_orientation = OrientationPredicate2D(conA[i%(len(conA))],conA[(i-1)%(len(conA))],conA[(i-2-count)%(len(conA))])


    previous_orientation = OrientationPredicate2D(conB[j%(len(conB))],conB[(j+1)%(len(conB))],conA[i%(len(conA))]) 
    for count in range(0,len(conB)-2) :
        if previous_orientation != OrientationPredicate2D(conB[j%(len(conB))],conB[(j+1)%(len(conB))],conB[(j+2+count)%(len(conB))]) :
            j = j+1
            changeflag = True
            break
        previous_orientation = OrientationPredicate2D(conB[j%(len(conB))],conB[(j+1)%(len(conB))],conB[(j+2+count)%(len(conB))])
LowerBridge = (conA[i%(len(conA))],conB[j%(len(conB))]) 
grahamplot(conA,A)
grahamplot(conB,B)
plt.show()
print("Upper Bridge :")
print(UpperBridge)
print("Lower Bridge :")
print(LowerBridge)
#print(conA)
print(conB)

#Begin from the leftmostpoint of ConA, add to ConFused until you reach upper bridge 1 
#Continue adding from upperbridge 2 clockwise until you reach lower bridge 2
#From lower bridge 2 go to lower bridge 1 and keep adding points until you reach leftmostpoint

convexhull = []
i = find_index_list(conA,leftmostpointA)
flag = False
while flag == False :
    #print(i)
    convexhull.append(conA[i])
    if conA[i].x >= UpperBridge[0].x-tol and conA[i].x <= UpperBridge[0].x+tol and conA[i].y >= UpperBridge[0].y-tol and conA[i].y <= UpperBridge[0].y+tol :
        flag = True
        continue
    i = (i-1)%len(conA)

j = find_index_list(conB,UpperBridge[1])
flag = False
while flag == False :
    convexhull.append(conB[j])
    if conB[j].x >= LowerBridge[1].x-tol and conB[j].x <= LowerBridge[1].x+tol and conB[j].y >= LowerBridge[1].y-tol and conB[j].y <= LowerBridge[1].y+tol:
        flag = True
        continue
    j = (j-1)%len(conB)

i = find_index_list(conA,leftmostpointA)
k = find_index_list(conA,LowerBridge[0])
flag = False
while flag == False :
    if conA[k].x >= leftmostpointA.x-tol and conA[k].x <= leftmostpointA.x+tol and conA[k].y >= leftmostpointA.y-tol and conA[k].y <= leftmostpointA.y+tol:
        flag = True
        continue
    convexhull.append(conA[k])
    k = (k-1)%len(conA)

print("Length of convexhull :")
print(len(convexhull))
#print(convexhull)
#will plot both in one 
xlist = []
ylist = []
for point in convexhull :
    xlist.append(point.x)
    ylist.append(point.y)
#these arrays contain the entire set of points given
xcordarray2 = np.array(xlist)
ycordarray2 = np.array(ylist)
plt.plot(xcordarray2,ycordarray2, 'o')
end_time = time.time()
plt.show()

grahamplot(convexhull,pointlist)
plt.show()
elapsed_time = end_time - start_time
print(f"Elapsed Time: {elapsed_time} seconds")








