import txaio
txaio.use_asyncio()

from vpython import *
# canvas(width=600,height=600,center=vector(0,12,0),background=color.white)
g=22.8 # acceleration due to gravity
bob=sphere(pos=vector(5,2,0),radius=0.5,color=color.blue)
pivot=vector(0,20,0)
roof=box(pos=pivot,size=vector(10,0.5,10),color=color.red)
rod=cylinder(pos=pivot,axis=bob.pos-pivot,radius=0.1,color=color.red)
t=0 # time 
dt=0.001 # time interval 
l=mag(bob.pos-pivot) # length of pendulum
cs=(pivot.y-bob.pos.y)/l # calculation of cos(theta) 
theta=acos(cs) # angle with vertical direction
vel=11.0 # angular velocity
while (t<100):
  rate(100) # maximum 100 calculations per second
  acc=-g/l*sin(theta) # updating of angular acceleration
  theta=theta+vel*dt # updating of angular position
  vel=vel+acc*dt # updating of angular velocity
  bob.pos=vector(l*sin(theta),pivot.y-l*cos(theta),0) # cal. position
  rod.axis=bob.pos-rod.pos # updating other end of rod of pendulum
  t=t+dt # updating time