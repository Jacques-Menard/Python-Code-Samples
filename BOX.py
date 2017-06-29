# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 09:57:09 2017

@author: jmenard
"""

class Box(object):
    def __init__(self, centerX = 0.0, centerY = 0.0, centerZ = 0.0, width = 1.0, height = 1.0, depth = 1.0):
        self.centerX=centerX
        self.centerY=centerY
        self.centerZ=centerZ
        self.width=width
        self.height=height
        self.depth=depth
    def setCenter(self, x, y, z):
        self.centerX=x
        self.centerY=y
        self.centerZ=z
    def setWidth(self,width):
        self.width=width
    def setHeight(self,height):
        self.height=height
    def setDepth(self,depth):
        self.depth=depth
    def volume(self):
        return self.width*self.height*self.depth
    def surfaceArea(self):
        return (2*self.depth*self.width)+(2*self.height*self.width)+(2*self.height*self.depth)
    def overlaps(self, otherBox):
        #check above
        if(self.centerY+self.height*(1/2)<otherBox.centerY-otherBox.height*(1/2)):
            return False
        #check below
        if(otherBox.centerY+otherBox.height*(1/2)<self.centerY-self.height*(1/2)):
            return False
        #check to the right of        
        if (self.centerX+self.width*(1/2)<otherBox.centerX-otherBox.width*(1/2)):
            return False
        #check to the left of
        if (otherBox.centerX+otherBox.width*(1/2)<self.centerX-self.width*(1/2)):
            return False        
        #check behind
        if(self.centerZ+self.depth*(1/2)<otherBox.centerZ-otherBox.depth*(1/2)):
            return False
        #check infront
        if(otherBox.centerZ+otherBox.depth*(1/2)<self.centerZ-self.depth*(1/2)):
            return False        
        return True
    def contains(self, otherBox):
        #check above
        if(self.centerY+self.height*(1/2)<otherBox.centerY+otherBox.height*(1/2)):
            return False
        #check below
        if(otherBox.centerY-otherBox.height*(1/2)<self.centerY-self.height*(1/2)):
            return False
        #check to the right of        
        if (self.centerX+self.width*(1/2)<otherBox.centerX+otherBox.width*(1/2)):
            return False
        #check to the left of
        if (otherBox.centerX-otherBox.width*(1/2)<self.centerX-self.width*(1/2)):
            return False        
        #check behind
        if(self.centerZ+self.depth*(1/2)<otherBox.centerZ+otherBox.width*(1/2)):
            return False
        #check infront
        if(otherBox.centerZ-otherBox.width*(1/2)<self.centerZ-self.depth*(1/2)):
            return False        
        return True        
        
    def __repr__(self):
        return str(self.width)+'-by-'+str(self.height)+'-by-'+str(self.depth)+'3D box with center at({}, {}, {})'.format(self.centerX, self.centerY, self.centerZ)

def testBox():
    box1 = Box(10.0, 5.0, 0.0, 2.0, 1.0, 1.0)
    box2 = Box(0, 0, 0, 3.5, 2.5, 1.0)
    
    if(box1.volume() != 2.0):
        print("Test Failed output of box1.volume() should be 2.0")
        return False
    if(box2.surfaceArea() != 29.5):
        print("Test Failed output of box2.surfacearea() should be 29.5")
        return False
    if(box1.overlaps(box2) != False):
        print("Test Failed box2 shouldn't overlap box1")
        return False
    box1.setCenter(2.75,0,0)
    if(box1.overlaps(box2) != True):
        print("Test Failed box2 should overlap box1")
        return False
    box3=Box(0,0,0)
    if(box2.contains(box3) !=True):
        print("Test Failed box2 should contain box3")
        return False
    box4=Box(10.0, 5.0, 0.0, 2.0, 1.0, 1.0)
    if(box4.contains(box3) != False):
        print("Test Failed box4 shouldn't contain box3")
        return False
    print("All tests passed")