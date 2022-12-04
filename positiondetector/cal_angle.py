import math


def dot(vA, vB):
    return vA[0] * vB[0] + vA[1] * vB[1]


def calcAngle(lineA, lineB):
    # Get nicer vector form
    vA = [(lineA[0][0] - lineA[1][0]), (lineA[0][1] - lineA[1][1])]
    vB = [(lineB[0][0] - lineB[1][0]), (lineB[0][1] - lineB[1][1])]
    # Get dot prod
    dot_prod = dot(vA, vB)
    # Get magnitudes
    magA = dot(vA, vA) ** 0.5
    magB = dot(vB, vB) ** 0.5
    # Get cosine value
    cos_ = dot_prod / magA / magB
    # Get angle in radians and then convert to degrees
    angle = math.acos(dot_prod / magB / magA)
    # Basically doing angle <- angle mod 360
    ang_deg = math.degrees(angle) % 360

    if ang_deg - 180 >= 0:
        # As in if statement
        return 360 - ang_deg
    else:

        return ang_deg



ertexType = "same start point; order 1"
            #X, Y    X Y coords
lineA = ((1,1.5),(2,2)) #DE
lineB = ((1,1.5),(2.5,0.5)) #DF
print(calcAngle(lineA, lineB))
#flip lines order
vertexType = "same start point; order 2"
lineB = ((1,1.5),(2,2)) #DE
lineA = ((1,1.5),(2.5,0.5)) #DF
print(calcAngle(lineA, lineB))

vertexType = "same end point; order 1"
lineA = ((2,2),(1,1.5)) #ED
lineB = ((2.5,0.5),(1,1.5)) #FE
print(calcAngle(lineA, lineB))
#flip lines order
vertexType = "same end point; order 2"
lineB = ((2,2),(1,1.5)) #ED
lineA = ((2.5,0.5),(1,1.5)) #FE
print(calcAngle(lineA, lineB))

vertexType = "one line after another - down; order 1"
lineA = ((2,2),(1,1.5)) #ED
lineB = ((1,1.5),(2.5,0.5)) #DF
print(calcAngle(lineA, lineB))
#flip lines order
vertexType = "one line after another - down; order 2"
lineB = ((2,2),(1,1.5)) #ED
lineA = ((1,1.5),(2.5,0.5)) #DF
print(calcAngle(lineA, lineB))

vertexType = "one line after another - up; line order 1"
lineA = ((1,1.5),(2,2)) #DE
lineB = ((2.5,0.5),(1,1.5)) #FD
print(calcAngle(lineA, lineB))
#flip lines order
vertexType = "one line after another - up; line order 2"
lineB = ((1,1.5),(2,2)) #DE
lineA = ((2.5,0.5),(1,1.5)) #FD
print(calcAngle(lineA, lineB))