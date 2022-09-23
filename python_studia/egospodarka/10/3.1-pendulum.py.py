from vpython import *
#GlowScript 2.9 VPython
display(width=600,height=600,center=vector(0,12,0),background=color.white)
g=9.8 # acceleration due to gravity
bob=sphere(pos=vector(5,2,0),radius=0.5,color=color.blue)
pivot=vector(0,20,0)
roof=box(pos=pivot,size=vector(10,0.5,10),color=color.green)
rod=cylinder(pos=pivot,axis=bob.pos-pivot,radius=0.1,color=color.red)