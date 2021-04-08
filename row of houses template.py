"""

This blog is based on the original house an article from issue 68 of the
Magpi Magazine which you can buy here
https://www.raspberrypi.org/magpi/issues/68/


link download for free from here.

https://www.raspberrypi.org/magpi-issues/MagPi68.pdf


The article is on page 54.  It was written by an man called Steve Martin who you
can access on Twitter here:

http://twitter.com/0x90_Bug

Without digging too deep it seems as though he helps
run/ attends the Cotswold Jam. This is an excellent tutorial in how to get started
with Python and Minecraft. I have slightly modified and extended the code to work with
the Micro:bit. This version creates a 3-4 storey version which creates 2 sides of a "road".
It is buggy as the right handside faces the wrong way.  

Extended by @ChrisPenn84

"""




#!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block
#import microbit
import random

# Connect to Minecraft
mc = Minecraft.create()
Colours_List = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
Walls = 4

def Build_House_Full(x,y,z):
    # Determine the Player's current position.
    #x,y,z = mc.player.getTilePos()

    width = 5
    height = 3
    depth = 6

    # Create a hollow shell made of bricks.
    mc.setBlocks(x, y, z+3, x+width, y+height, z+3+depth,35,random.choice(Colours_List))#block.BRICK_BLOCK.id)
    mc.setBlocks(x+1, y, z+4, x+width-1, y+height-1, z+2+depth, block.AIR.id)

    # Set the floor.
    mc.setBlocks(x-1, y-1, z+2, x+1+width, y-1, z+4+depth,35,random.choice(Colours_List))#block.COBBLESTONE.id)


    # Add Windows.
    mc.setBlocks(x+3, y+1, z+3, x+4, y+2, z+3, block.GLASS.id)
    mc.setBlocks(x+2, y+1, z+3+depth, x+3, y+2, z+3+depth, block.GLASS.id)
    mc.setBlocks(x, y+1, z+5, x, y+2, z+7, block.GLASS.id)
    mc.setBlocks(x+width, y+1, z+5, x+width, y+2, z+7, block.GLASS.id)

    # Add a Roof.
    for i in range(int(width/2) + 1):
        mc.setBlocks(x+i, y+height+i, z+3, x+i, y+height+i, z+3+depth, 53, 0)
        mc.setBlocks(x+width-i, y+height+i, z+3, x+width-i, y+height+i, z+3+depth, 53, 1)
        # Gable ends.
        if (int(width/2) - i > 0):
            mc.setBlocks(x+1+i, y+height+i, z+3, x+width-i-1, y+height+i, z+3,35, random.choice(Colours_List))#block.BRICK_BLOCK.id, 0)
            mc.setBlocks(x+1+i, y+height+i, z+3+depth, x+width-i-1, y+height+i, z+3+depth,35,random.choice(Colours_List)) #block.BRICK_BLOCK.id, 1)


def Build_House(x,y,z,Bottom):
    # Determine the Player's current position.
    #x,y,z = mc.player.getTilePos()

    width = 5
    height = 3
    depth = 6

    # Create a hollow shell made of bricks.
    mc.setBlocks(x, y, z+3, x+width, y+height, z+3+depth,35,random.choice(Colours_List))#block.BRICK_BLOCK.id)
    mc.setBlocks(x+1, y, z+4, x+width-1, y+height-1, z+2+depth, block.AIR.id)

    # Set the floor.
    mc.setBlocks(x-1, y-1, z+2, x+1+width, y-1, z+4+depth,35,random.choice(Colours_List))#block.COBBLESTONE.id)

    if Bottom == True:
        # Add a Door.
        mc.setBlock(x+1, y, z+3, block.DOOR_WOOD.id, 0)
        mc.setBlock(x+1, y+1, z+3, block.DOOR_WOOD.id, 8)

    # Add Windows.
    mc.setBlocks(x+3, y+1, z+3, x+4, y+2, z+3, block.GLASS.id)
    mc.setBlocks(x+2, y+1, z+3+depth, x+3, y+2, z+3+depth, block.GLASS.id)
    mc.setBlocks(x, y+1, z+5, x, y+2, z+7, block.GLASS.id)
    mc.setBlocks(x+width, y+1, z+5, x+width, y+2, z+7, block.GLASS.id)

    
#code goes below 

