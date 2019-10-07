# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:08:17 2019

@author: austin.schrader
"""

# class declaration
class Jungle:
    # constructor with default values
    def __init__(self, name="Unknown"):
        self.visitorName = name
        
    def welcomeMessage(self):
        print("Hello %s, Welcome to the Jungle" % self.visitorName)
        
# create object of class Jungle
j = Jungle("Meher")
j.welcomeMessage()

k = Jungle()
k.welcomeMessage()
