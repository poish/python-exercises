import math

class Vector:
    pass

class System:
    def __init__(self):
        self.bodies = []

    def addBody(self, pos, vel, mass):
        pass

    def force(self, body):

        total = Vector()
        
        for q in self.bodies:
            if b == q:
                return Vector(0,0)

            displacement = q - b
            magnitude = q.mass * b.mass / math.pow(displacement.mag(), 2)

            total += displacement.unit() * magnitude                
                    

deltaP = [None] * 4
deltaV = [None] * 4
dt, vel, b = 0


class System:
    pass
