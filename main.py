import numpy as np

def findPrincessLocation(n,grid):
    for y in range(0,n):
        for x in range(0,n):
           character =  grid[y][x]
           if(character == "p"):
               return [x,y]

def findBotLocation(n,grid):
    for y in range(0,n):
        for x in range(0,n):
           character =  grid[y][x]
           if(character == "m"):
               return [x,y]               

def displayPathtoPrincess(n,grid):
    princesslocation = findPrincessLocation(m,grid)
    botLocation = findPrincessLocation(m,grid)

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)