from zk import *
import math
import random


def collideDirectionJudge(spriteA,spriteB):
    Colide_direct = 0
    # A hit B from top
    if abs(spriteA.getPosition()[1] - spriteB.getPosition()[0]) <= 3:
        Colide_direct = 1
    # A hit B from bottom
    elif abs(spriteA.getPosition()[0] - spriteB.getPosition()[1]) <= 3:
        Colide_direct = 2

    elif abs(spriteA.getPosition()[0] - spriteB.getPosition()[1]) > 3:
        # A hit B from left
        if spriteA.getPosition()[2] < spriteB.getPosition()[2]:
            Colide_direct = 3 # or 4
        # A hit B from right
        else:
            Colide_direct = 4
    
    # print("spriteA.top =" ,spriteA.getPosition()[0])
    # print("spriteA.bottom =" ,spriteA.getPosition()[1])
    # print("spriteB.top =" ,spriteB.getPosition()[0])
    # print("spriteB.bottom =" ,spriteB.getPosition()[1])

    return Colide_direct

def collide_check(item, targetGroup):
    col_balls = []
    for each in targetGroup:
        distance = math.sqrt(math.pow(item.rect.center(0) - each.rect.center[0]), 2) + \
                   math.sqrt(math.pow(item.rect.center(1) - each.rect.center[1]), 2)
    if distance <= (item.rect.width + each.rect.width) / 2:
        col_balls.append(each)

    return col_balls



