import random
import numpy as np
from points import R2Point
from points import checkifcollinear
from points import checkallifcollinear








#MAIN START

datafile = open("200random2Dpoints.txt", "w")
#will now create 100 random 2D points and store them in the file 
acceptedpoints = []
for i in range(0,200):
    #decide on a fair generator
    #part that makes sure it won't make any lines with the other ones
    linecheckpassed = False
    while linecheckpassed == False :
        xcord = random.random() + random.randint(0,199)
        ycord = random.random() + random.randint(0,199)
        p3 = R2Point(xcord,ycord)
        if(len(acceptedpoints) < 2) :
            acceptedpoints.append(p3)
            linecheckpassed = True
        else :
           if checkallifcollinear(acceptedpoints,p3) == False :
                acceptedpoints.append(p3)
                linecheckpassed = True
            #here the point passed the check, it is not colinear with any previous points



for point in acceptedpoints :
     datafile.write(f'{point.x:.6f} {point.y:.6f}\n')
datafile.close()
