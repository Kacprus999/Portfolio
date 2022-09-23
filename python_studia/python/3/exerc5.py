import numpy as np

f = open("populacje.txt")

tab1 = np.loadtxt(f)
rows,columns = tab1.shape

#firstpart
argcolmax = np.argmax(tab1, axis=0)
print("Zadanie 1 \n")
print("Best fox year was: ", int(tab1[argcolmax[1],0]))
print("Best rabbit year was: ", int(tab1[argcolmax[2],0]))
print("Best carrot year was: ", int(tab1[argcolmax[3],0]))

#secondpart
argrowmax = np.argmax(tab1,axis=1)
print("\n\nZadanie 2 \n")
for row in range(0,rows):
    if argrowmax[row] == 3: 
        print("In ",int(tab1[row,0])," year carrots had highest pop")
    elif argrowmax[row] == 2:
        print("In ",int(tab1[row,0])," year rabbits had highest pop")
    elif argrowmax[row] == 1:
        print("In ",int(tab1[row,0])," year foxes had highest pop")

#thirdpart
print("\n\nZadanie 3 \n")
for row in range(0,rows):
    if (np.sum(tab1,1)[row]-tab1[row,0]) > 100000:
         print("In ",int(tab1[row,0])," year pop was greater than 100 000")