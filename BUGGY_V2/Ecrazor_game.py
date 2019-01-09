#!/usr/bin/env python
from __future__ import print_function
from matplotlib.pyplot import *
from numpy import *
from numpy.random import *

from math import * # For real cos instead of array cos from numpy...

print('\n\nGet the most of targets within the shortest time. Controls are up,down,left,right keys, zoom with +,- and stop with ESC.\n\n')

bExit, scale = 0, 50

x = array([0,0,0,10]).reshape(4,1)
u = array([0,0]).reshape(2,1)
dt = 0.05
t = 0

# This function should be called when a key is pressed.
def on_key(event):
    # Global variables to share with other functions.
    global u, bExit, scale
    # Actions to do depending on the key pressed.
    #print('You pressed', event.key, event.xdata, event.ydata)
    if event.key == 'escape':
        bExit = 1
    if event.key == 'up':
        u = array([0,10]).reshape(2,1)
    if event.key == 'down':
        u = array([0,-10]).reshape(2,1)
    if event.key == 'left':
        u = array([10,0]).reshape(2,1)
    if event.key == 'right':
        u = array([-10,0]).reshape(2,1)
    if event.key == '+':
        scale = scale*0.9
    if event.key == '-':
        scale = scale/0.9

def f(x,u):
    xdot = array([x[3]*cos(x[2]),
                  x[3]*sin(x[2]),
                  u[0],
                  u[1]]).reshape(4,1)
    return xdot

def draw_tank(x):
    M = array([[1,-1,0,0,-2,-2,0,0,-1,1,0,0,3,3,0],
               [-2,-2,-2,-1,-1,1,1,2,2,2,2,1,1,-1,-1],
               ones(15)])
    M = dot(array([[cos(x[2]),-sin(x[2]),x[0]],[sin(x[2]),cos(x[2]),x[1]],[0,0,1]]),M)
    plot(M[0].flatten(),M[1].flatten(),'b')

ion() # Turn the interactive mode on.

# Create a figure that will use the function on_key() when a key is
# pressed.
fig = figure('Ecrazor game')
cid = fig.canvas.mpl_connect('key_press_event',on_key)
        
targets = 0
target = scale*rand(2,1)

while (bExit == 0):
    x = x+f(x,u)*dt
    clf()
    axis('square')
    axis([-scale,scale,-scale,scale])
    draw_tank(x)

    plot(target[0],target[1],'rs',ms=10)
    if ((target[0]-2.5 < x[0])&(x[0] < target[0]+2.5)&(target[1]-2.5 < x[1])&(x[1] < target[1]+2.5)):
        targets = targets+1
        target = scale*rand(2,1)
   
    # Wait a little bit and refresh the figure.
    pause(0.001)
    t = t+dt

score = 100*targets/t

print('\n\nTargets catched :',targets,', total time = ',t,' s, score = ',score,'\n\n')
