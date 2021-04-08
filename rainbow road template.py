import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time
mc = minecraft.Minecraft.create()
pos = mc.player.getPos()

def SetRoad():
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y-1, pos.z, 35,1)#orange
    #pinky purple
    #sky blue
    #yellow
    #green
    #pink
    #black
    #grey
    #blue
    #purple
#mc.postToChat("Watch out for disco blocks")
while True:
    
