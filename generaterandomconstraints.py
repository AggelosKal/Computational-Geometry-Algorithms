import random

#MAIN START

datafile = open("6random2Dconstraints.txt", "w")
#will now create 6 random 2D constraints and store them in the file 
acceptedconstraints = []
for i in range(0,6):
    #decide on a fair generator
    #part that makes sure it won't make any lines with the other ones
    Acord = random.random() + random.randint(0,19)
    Bcord = random.random() + random.randint(0,19)
    Ccord = (random.random() + random.randint(0,19))*(-1)
    acceptedconstraints.append((Acord,Bcord,Ccord))
        



for con in acceptedconstraints :
     datafile.write(f'{con[0]:.0f} {con[1]:.0f} {con[2]:.0f}\n')
datafile.close()
