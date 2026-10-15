import re
from points import R2Point
from points import get_line_ABC
from convexhullutil import read_2D_points_from_file_make_pointlist
import numpy as np
import matplotlib.pyplot as plt
from points import get_line_intersection,objective_f, are_equal
from points import restriction_is_met
from grahamscan import grahamplot


#first of all decide on a way to represent constraints
#All constraints ...<=...
#x1 + 3x2 -5<= 0
#x1 - x2 -3 <= 0
#-7x1 + 3x2 +1 <= 0
#4x1-9x2 -35 <= 0
#3x1 - 7x2 -32<= 0
#-2x1 + 5x2 -26<= 0 
#-x1 <= 0
#-x2 <= 0

#Lines in form Ax + By + C = 0 

rest_ABCs = [[1,3,-5],[1,-1,-3],[-7,3,1],[4,-9,-35],[3,-7,-32],[-2,5,-26]]
print(rest_ABCs)


#make a list of points representing the feasible region convex hull, initialize it by a clockwise box 
feasible_region = [R2Point(0,0),R2Point(100,0),R2Point(100,100),R2Point(0,100)] 
solution = feasible_region[2]
for constraint in rest_ABCs :
    cons_inters= []
    if len(feasible_region) == 0 :
        print("Feasible region is empty, terminating")
        exit()
    i = 0
    while i < len(feasible_region) :
        flag1= restriction_is_met(constraint,feasible_region[i])
        flag2= restriction_is_met(constraint,feasible_region[(i+1)%len(feasible_region)])
        if (flag1 == True and flag2 == True) or (flag1 == False and flag2 == False):
            i = (i+1)
            continue#do nothing 
        elif (flag1 == True and flag2 == False) or (flag1 == False and flag2 == True) :
            #add intersection point between vertices
            feasible_region.insert((i+1),get_line_intersection(get_line_ABC(feasible_region[i],feasible_region[(i+1)%len(feasible_region)]),constraint))
            cons_inters.append(feasible_region[i+1])
            i = (i+1)
            #so that it skips using the intersection point as a vertex in this loop
        i = i+1   
    #now remove all vertices that are out
    i = 0
    while i < len(feasible_region) : 
        if restriction_is_met(constraint,feasible_region[i]) == False :
            if are_equal(objective_f(solution), objective_f(feasible_region[i])) :
                 #this means the previous solution is now out, will look at the new line intersections
                 #print("Solution changed, previous solution was")
                 #print(solution, objective_f(solution))
                 if len(cons_inters) == 0 :
                    print("Feasible region is empty, terminating")
                    exit() 
                 solution = cons_inters[0]
                 for line_intersection in cons_inters :
                      if objective_f(line_intersection) > objective_f(solution) :
                           solution = line_intersection 
                      
            feasible_region.pop(i)
            i = i-1
        i = i+1
    print("Current solution and value :")
    print(solution, objective_f(solution))
    grahamplot(feasible_region,feasible_region)
    plt.show()
if len(feasible_region) == 0 :
        print("Feasible region is empty, terminating")
        exit()

print("Final Plot !")
print("Optimal solution is :")
print(solution, objective_f(solution))
grahamplot(feasible_region,feasible_region)
plt.show()



 
