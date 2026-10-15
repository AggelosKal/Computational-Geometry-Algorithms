import re

def read_2D_constraints_from_file_make_list() :
    datafile = open("6random2Dconstraints.txt", "r")
    listoflines = datafile.readlines()
    datafile.close()
    conlist = []
    for line in listoflines:
        stripped_line = line.strip()
        #print(stripped_line)
        regex_result = re.split("\s", stripped_line)
        #regex_result = re.findall(r'[+-]?[1-9][0-9]*[.][0-9]*[1-9]|[+-]?[0-9][1-9]*|0|[+-]?0[.][0-9]*[1-9]' , stripped_line)
        #print(regex_result)
        A_cord = float(regex_result[0])
        B_cord = float(regex_result[1])
        C_cord = float(regex_result[2])
        p = [A_cord,B_cord,C_cord]
        conlist.append(p)
    return conlist