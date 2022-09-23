from cmath import sin
import matplotlib.pyplot as plt
from vpython import *
import txaio

txaio.use_asyncio()

scene.caption = """To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate. 
Swietny opis bardzo potrzebny 
"""

T = 0
tArr = [0]
dt = 0.001
g = 9.8
l = 10
angle = 5
vel = 1.0
angleArr = [angle]

while T < 100:
    acc = -g / l * sin(angle)
    angle = angle + vel * dt
    vel = vel + acc * dt
    T = T+dt
    tArr.append(T)
    angleArr.append(angle)

plt.plot(tArr, angleArr)
plt.show()


rod=cylinder(pos=vector(-60,0,0),size=vector(140,10,10),radius=0.2,color=color.blue)
ball = sphere (color = color.red, radius = 4)
mass = 0.5
ball.pos = vector (-60,0,0)
T = 0
dt = 0.1

while True:
    rate(200)
    ball.pos.x = ball.pos.x + mass*dt
    print(ball.pos.x)
    if ball.pos.x > 80:
        mass = mass*-1
    if ball.pos.x < -60:
        mass = mass * -1