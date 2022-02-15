import numpy as np

class Vec2(np.ndarray):

    def __init__(self, x, y):
        super().__init__((2,np.float32))

    def x(self):
        return self[0]
    
    def y(self):
        return self[1]



vec = Vec2(2,7)

print(a)
print(type(a))