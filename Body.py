import numpy as np
from numpy import ndarray
class Body:

    def __init__(self, init_pos:ndarray, init_vel:ndarray, mass):
        self.pos = np.array(init_pos)
        self.vel = np.array(init_vel)
        self.mass = mass

    def update(self, pos, vel) :
        self.pos = self.pos + pos
        self.vel = self.vel + vel

