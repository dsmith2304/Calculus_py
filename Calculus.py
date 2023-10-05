#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      danny
#
# Created:     05/10/2023
# Copyright:   (c) danny 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class Vector:
    x: float
    y: float
    z: float
    xv: float
    yv: float
    zv: float
    sizex: float
    sizey: float
    sizez: float
    mass: float
    gravity: float

    def __init__(self,x,y,z,xv,yv,zv,sx,sy,sz,mass,gravity):
        self.x=x
        self.y=y
        self.z=z
        self.xv=xv
        self.yv=yv
        self.zv=zv
        self.sizex=(sx/2)
        self.sizey=(sy/2)
        self.sizez = (sz/2)
        self.mass=mass
        self.gravity = gravity

    def calcAtTime(self,time,magnitude):
        xd = self.x + self.xv*time
        yd = self.y + self.yv*time
        zd = self.z + self.zv*time

        return(xd*magnitude,yd*magnitude,zd*magnitude)

    def calcAtTimeAccelGrav(self,time,acceleration,magnitude):
        xd = (self.x + self.xv)* time#pow(acceleration,time)
        tempYv= self.yv-((self.mass * self.gravity)*time)
        yd = (self.y + tempYv)* time#pow(acceleration,time)
        zd = (self.z + self.zv)* time#pow(acceleration,time)

        return(xd*magnitude,yd*magnitude,zd*magnitude)

    def calcAtTimeAccel(self,time,acceleration,magnitude):
        xd = (self.x + self.xv)* pow(acceleration,time)
        yd = (self.y + self.yv)* pow(acceleration,time)
        zd = (self.z + self.zv)* pow(acceleration,time)

        return(xd*magnitude,yd*magnitude,zd*magnitude)

    def isWithinRange(primary,primaryCalc,secondary,secondaryCalc):

        xUnitsSize = primary.sizex + secondary.sizex
        yUnitsSize = primary.sizey + secondary.sizey
        zUnitsSize = primary.sizez + secondary.sizez

        xDistance = primaryCalc[0] - secondaryCalc[0]
        yDistance = primaryCalc[1] - secondaryCalc[1]
        zDistance = primaryCalc[2] - secondaryCalc[2]
        if(xUnitsSize >= abs(xDistance) and yUnitsSize >= abs(yDistance) and zUnitsSize >= abs(zDistance)):
            return True
        else:
            return False

    def calcSpeed(time,acceleration,primary,secondary):
        #
        #
        vOneSpeed = ((abs(primary.xv) + abs(primary.yv) + abs(primary.zv)) / 3)* pow(acceleration,time)
        vTwoSpeed = ((abs(secondary.xv) + abs(secondary.yv) + abs(secondary.zv)) / 3)* pow(acceleration,time)
        #
        return vOneSpeed+vTwoSpeed

    def calcVectors(primary, secondary,time,acceleration,magnitude):
        for i in range(1,time):

            calcPrimary = primary.calcAtTimeAccel(i,acceleration,magnitude)
            calcSecondary= secondary.calcAtTimeAccel(i,acceleration,magnitude)
            print("time index "+str(i))
            if(Vector.isWithinRange(primary,calcPrimary,secondary,calcSecondary) == True):

                print("hit at primary"+ str(primary.calcAtTimeAccel(i,acceleration,magnitude)) + " With a speed of "+str(Vector.calcSpeed(i,acceleration,primary,secondary)))
                print("hit at secondary"+ str(secondary.calcAtTimeAccel(i,acceleration,magnitude)) + " With a speed of "+str(Vector.calcSpeed(i,acceleration,primary,secondary)))

            else:
                print("Primary: " + str(primary.calcAtTimeAccel(i,acceleration,magnitude)))
                print("Secondary: " + str(secondary.calcAtTimeAccel(i,acceleration,magnitude)))

            print()
def main():
    v = Vector(1,0.5,0,8.2,8.2,0.5,0.07,0.07,0.07,0.15,9.6)
    t = Vector(1,0.5,0,8.15,8.25,0.5,0.07,0.07,0.07,0.15,9.6)
    print(v.calcAtTimeAccelGrav(1,1,1))
    print(v.calcAtTimeAccelGrav(2,1,1))
    print(v.calcAtTimeAccelGrav(3,1,1))
    print(v.calcAtTimeAccelGrav(4,1,1))
    print(v.calcAtTimeAccelGrav(5,1,1))
    print(v.calcAtTimeAccelGrav(6,1,1))
    print(v.calcAtTimeAccelGrav(6.0335,1,1))
    Vector.calcVectors(v,t,11,1.3,1)

if __name__ == '__main__':
    main()
