
def collideDirectionJudge(spriteA,spriteB):
    Colide_direct = 0
    # A hit B from top
    if abs(spriteA.getPosition()[1] - spriteB.getPosition()[0]) <= 5:
        # print("ball.bottom in if =" ,ball.getPosition()[3])
        Colide_direct = 1
    # A hit B from bottom
    elif abs(spriteA.getPosition()[0] - spriteB.getPosition()[1]) <= 5:
        Colide_direct = 2

    elif abs(spriteA.getPosition()[0] - spriteB.getPosition()[1]) > 5:
        # A hit B from left
        if spriteA.getPosition()[2]<spriteB.getPosition()[2]:
            Colide_direct = 3 # or 4
        # A hit B from right
        else:
            Colide_direct = 4

    return Colide_direct