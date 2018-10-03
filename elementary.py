#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Alley Busick
# Student ID: 2293544
# Email: busick@chapman.edu
# Course: PYHS220/MATH220/CPSC220 Fall 2018
# Assignment: CW 5
###

import scipy

class Particle(object):

    #class constructor 
    def __init__(self, x, y, z):
        self.mass = (1.0)
        self.position = (x, y, z)
        self.momentum = (0.0, 0.0, 0.0)

    #method 1
    def impulse(self, px, py, pz):
        #increments each momentum value with indexing []
        incremented_momentum = (self.momentum[0]+px/self.mass,
                                self.momentum[1]+py/self.mass,
                                self.momentum[2]+pz/self.mass)
        # changes existing momentum (is this overriding?)
        self.momentum = incremented_momentum

    #method 2
    def move(self, dt):
        #p = m(v) -> v = p/m
        changed_position = (self.position[0]+self.momentum[0]*dt/self.mass,
                            self.position[1]+self.momentum[1]*dt/self.mass,
                            self.position[2]+self.momentum[2]*dt/self.mass)
        self.position = changed_position


class ChargedParticle(Particle):

    def __init__(self):
        super(ChargedParticle, self).__init__(x,y,z)
        self.charge = scipy.constant.e

class Electron(ChargedParticle):

    def __init__(self):
        super(Electron, self).__init__(x,y,z)
        self.mass = scipy.constants.electron_mass

class Proton(ChargedParticle):

    def __init__(self):
        super(Proton, self).__init__(x,y,z)
        self.mass = scipy.constants.proton_mass

