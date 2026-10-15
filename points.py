import re
import numpy as np
from heapsort import heapsort 

class R2Point :
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def __str__(self) :
        return f"({self.x},{self.y})"
    
    def __repr__(self) :
        return f"PointObj(x = {self.x}, y = {self.y})"
    

def are_equal(value1, value2) :
    tol = 0.0000000001
    return (value1 < value2 + tol and value1 > value2 - tol)

def OrientationPredicate2D(p1,p2,p3) :
    n_array = np.array([[1,p1.x,p1.y],[1,p2.x,p2.y],[1,p3.x,p3.y]])
    det = np.linalg.det(n_array)
    #changed equality to a tolerance-inequality
    if are_equal(det,0) :
        #print("Collinear")
        return 0
    elif det > 0 :
        #print("Counter-Clockwise")
        return 1
    elif det < 0 :
        #print("Clockwise")
        return -1

#point1 = R2Point(3.1, 2)
#print(point1)
#point2 = R2Point(10,20)
#point3 = R2Point(25,85)
#a = OrientationPredicate2D(point1,point2,point3)


def checkifcollinear(p1,p2,p3) :
    #checks if 3 points are in the same line by determining whether the area of their triangle is 0, returns true if colinear
    n_array = np.array([[p1.x -p2.x ,p1.x - p3.x],[p1.y-p2.y,p1.y - p3.y]])
    det = np.linalg.det(n_array)
    areaoftri= det/2
    #changed equality to a tolerance-inequality
    if are_equal(areaoftri,0) :
        return True
    else :
        return False
    
def checkallifcollinear(plist,p3) :
    #combinations without repetition
    for i in range(0,len(plist)) :
                for j in range(i+1,len(plist)) :
                    if(checkifcollinear(plist[i],plist[j],p3) == True) :
                        return True
    return False
    #only returns False if passed all checks none were True 

#takes as input points in tuple form, sorts (heapsort method), then returns an equivalent list of points as objects instead of tuples
def get_sorted_2D_points_list(tuplelist) :
    sortedtuplelist = heapsort(tuplelist)
    sortedpointlist = []
    for tuple in sortedtuplelist :
          point = R2Point(tuple[0],tuple[1])
          sortedpointlist.append(point)
    return sortedpointlist


def get_sorted_2D_points_list_pointlist_arg(pointlist) :
    tuplelist = []
    for point in pointlist :
     tuplelist.append((point.x,point.y))
    sortedtuplelist = heapsort(tuplelist)
    sortedpointlist = []
    for tuple in sortedtuplelist :
          point = R2Point(tuple[0],tuple[1])
          sortedpointlist.append(point)
    return sortedpointlist
    
def get_point_line_distance(the_point, line_A, line_B, line_C) :
    return abs(line_A * the_point.x + line_B * the_point.y + line_C) / ((line_A** 2 + line_B ** 2) ** 0.5) 

#Ax + By + C = 0 , returns list with A B C constants, takes two 2D points
def get_line_ABC(point1, point2) :
    #equal x case for vertical lines
    if are_equal(point2.x-point1.x , 0) :
        #x = K, vertical line
        A = 1
        B = 0
        C = point1.x * (-1)
        return [A,B,C]
    c1 = (point2.y-point1.y)/(point2.x-point1.x)
    c2 = point1.y - c1 * point1.x
    A = c1 * (-1)
    B = 1
    C = c2 * (-1)
    return [A,B,C]          

def get_line_intersection(l1,l2) :
    #l has a b c in a list
    #lines a1x+b1y+c1 = 0 and a2x+b2y+c2 = 0
    #x = (b1c2-b2c1)/(a1b2-a2b1)
    #y = (a2c1-a1c2)/(a1b2-a2b1)
    if are_equal(l1[0]*l2[1]-l2[0]*l1[1] , 0) :
        print("No solution")
        exit()

    return R2Point((l1[1]*l2[2]-l2[1]*l1[2])/(l1[0]*l2[1]-l2[0]*l1[1]) , (l2[0]*l1[2]-l1[0]*l2[2])/(l1[0]*l2[1]-l2[0]*l1[1]))

#returns true when restriction is met by given point
#maybe test if it has issues with floating points

def objective_f(point):
    return 5 * point.x + 12 * point.y


def restriction_is_met(l,point):
    #or is the equal part of the inequality adjusted for floats just to be sure
    return (l[0]*point.x+l[1]*point.y + l[2] < 0 or  are_equal(l[0]*point.x+l[1]*point.y + l[2] , 0))


def read_2D_points_from_file_make_tuplelist() :
    datafile = open("25random2Dpoints.txt", "r")
    listoflines = datafile.readlines()
    datafile.close()
    tuplelist = []
    for line in listoflines:
        stripped_line = line.strip()
        #print(stripped_line)
        regex_result = re.split("\s", stripped_line)
        #regex_result = re.findall(r'[+-]?[1-9][0-9]*[.][0-9]*[1-9]|[+-]?[0-9][1-9]*|0|[+-]?0[.][0-9]*[1-9]' , stripped_line)
        #print(regex_result)
        x_cord = float(regex_result[0])
        y_cord = float(regex_result[1])
        p = (x_cord, y_cord)
        tuplelist.append(p)
    return tuplelist

def get_y_sorted_2D_points_list_pointlist_arg(pointlist) :
    #this function is a slight edit of the other function that sorts using x cord
    tuplelist = []
    for point in pointlist :
     tuplelist.append((point.y,point.x))
    sortedtuplelist = heapsort(tuplelist)
    sortedpointlist = []
    for tuple in sortedtuplelist :
          point = R2Point(tuple[1],tuple[0])
          sortedpointlist.append(point)
    return sortedpointlist

def leq(value1, value2) :
    return (value1 < value2 or are_equal(value1,value2))

def beq(value1, value2) :
    return (value1 > value2 or are_equal(value1,value2))

