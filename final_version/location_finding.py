#!/bin/python3
from collision_avoidance import CollisionAvoidance
from explorerhat import motor


class LocationFinding:
    def __init__(self, ebd):
        self.collision_avoidance = CollisionAvoidance(ebd)
        self.emergency_break_driver = ebd

    def find_location(self):
        pass
