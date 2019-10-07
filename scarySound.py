# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:21:50 2019

@author: austin.schrader
"""

from jungleBook import Jungle

class Animal(Jungle):
    def scarySound(self):
        print("Animals are running away due to the scary sounds")

class Bird(Jungle):
    def scarySound(self):
        print("Birds are flying away due to the scary sounds")
        
class Insect(Jungle):
    def scarySound(self):
        print("Insects do not care about scary sound.")