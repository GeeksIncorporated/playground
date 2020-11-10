#-*-coding:utf8-*-
#qpy:pygame
"""
Pygame support is builtin from QPython >= 2.4.0
"""

import sys
import pygame
from pygame.locals import *

pygame.init()
# Resolution is ignored on Android
surface = pygame.display.set_mode((640, 480))
# Only one built in font is available on Android
myfont = pygame.font.SysFont("DejaVuSans", 64)
label = myfont.render("Hello, world!", 1, (255, 255, 255))
clock = pygame.time.Clock()

while True:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
    # Framelimiter
    clock.tick(60)
    surface.fill((0, 0, 0))
    surface.blit(label, (0, 0))
    pygame.display.flip()
    

from collections import defaultdict
import time
from pprint import pprint
import sys

M = defaultdict(lambda: defaultdict(int))
cursor = [0,0]
print = lambda *x: True
pprint = lambda *x: True

def go_right (n):
    global cursor
    x, y = cursor
    for i in range (n):
        M[y][x+i] += 1
    x += n
    cursor = [x,y]
    
    
def go_left (n):
    global cursor
    x, y = cursor
    for i in range (n):
        M[y][x-i] += 1
    x -= n
    cursor = [x,y]
    
def go_up (n):
    global cursor
    x, y = cursor
    for i in range (n):
        M[y+i][x] += 1
    y += n
    cursor = [x,y]
    
def go_down (n):
    global cursor
    x, y = cursor
    for i in range (n):
        M[y-i][x] += 1
    y -= n
    cursor = [x,y]
    
dirs = {'R': go_right,
    'L': go_left,
    'D': go_down,
    'U': go_up}
    
def parse (wire):
    global cursor
    cursor = [0,0]
    for s in wire:
        d,n = s[0],int(s[1:])
        dirs[d](n)

def show (M):
    MH = 0
    MW = 0
    for y in M:
        for x in M[y]:
            MW = max(MW,x)
        MH = max(MH,x)

    T =[[0 for i in range (10)] for i in range (10)]
    for i in range (10):
        for j in range (10):
            T[i][j]=M[i][j]
    

    

def solve (w1, w2):
    global M
    M = defaultdict(lambda: defaultdict(int))
    w1=w1. split (',')
    w2=w2. split (',')
    parse (w1)
    parse (w2)
    show (M)
    min_d = (9999999,)
    for x in M:
        for y in M[x]:
            r = M[x][y]
            if r>1 and (x,y)!=(0,0):
                print (min_d)
                min_d = (min(min_d[0], 
                	   abs(x)+abs(y)),x,y)
    print (min_d)
 

#wire1="R8,U5,L5,D3"
#wire2="U7,R6,D4,L4"
#solve(wire1, wire2)

wire1="R75,D30,R83,U83,L12,D49,R71,U7,L72"
wire2="U62,R66,U55,R34,D71,R55,D58,R83"
solve(wire1, wire2)

#wire1="R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
#wire2="U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
#solve (wire1, wire2)

