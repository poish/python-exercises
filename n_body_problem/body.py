import uuid

class Body:
    def __init__(self, position, velocity, mass, id = None):
        if not id:
            self.id = uuid.uuid4()
        else:
            self.id = id

        self.pos = position
        self.vel = velocity
        self.mass = mass

    def position():
        pass

    def velocity():
        pass

    def project(self, dP, dV):
        pass

    def reset(self):
        pass

    def __repr__(self):
        return f"body nr {self.id}"

    def __eq__(self, other):
        return self.id == other.id

    def copy(self):
        return Body(self.pos, self.vel, self.mass, self.id)
    
