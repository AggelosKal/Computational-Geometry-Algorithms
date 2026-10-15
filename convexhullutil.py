import re
from points import R2Point
from points import are_equal

#used in exhaustive 
def get_vertex_list_clockwise(listofedges) :    
    arbitrary_edge = listofedges[0]
    vertexlist = []
    vertexlist.append(arbitrary_edge[0])
    vertexlist.append(arbitrary_edge[1])
    previous_end_point = arbitrary_edge[1]
    listofedges.pop(0)
    while len(listofedges) > 1 :
        for i in range(0,len(listofedges)):
            if listofedges[i][0] == previous_end_point :
                vertexlist.append(listofedges[i][1])
                previous_end_point = listofedges[i][1]
                listofedges.pop(i)
                break
    return vertexlist

def read_2D_points_from_file_make_pointlist() :
    datafile = open("200random2Dpoints.txt", "r")
    listoflines = datafile.readlines()
    datafile.close()
    pointlist = []
    for line in listoflines:
        stripped_line = line.strip()
        #print(stripped_line)
        regex_result = re.split("\s", stripped_line)
        #regex_result = re.findall(r'[+-]?[1-9][0-9]*[.][0-9]*[1-9]|[+-]?[0-9][1-9]*|0|[+-]?0[.][0-9]*[1-9]' , stripped_line)
        #print(regex_result)
        x_cord = float(regex_result[0])
        y_cord = float(regex_result[1])
        p = R2Point(x_cord, y_cord)
        pointlist.append(p)
    return pointlist

def find_index_list(my_list,element) :
    for ind, item in enumerate(my_list) :
        #will only check the x values since list has unique x values anyway
        if are_equal(item.x,element.x) :
            return ind
    print("Element was not found in list.")
    exit()

