# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:13:44 2019

@author: austin.schrader
"""

from abc import ABCMeta, abstractmethod

# class declaration
class Jungle(metaclass=ABCMeta):
    def __init__(self, name="Unknown"):
        self.visitorName = name
    
    def welcomeMessage(self):
        print("Hello %s, Welcome to the Jungle" % self.visitorName)
        
    #abstractmethod 
    def scarySound(self):
        pass
        
        
        
        
        
        
class RateJungle(Jungle):
    def __init__(self, name, feedback):
        self.feedback = feedback
        
        # inheriting the constructor of the class
        super().__init__(name)
        
    def printRating(self):
        print("Thanks %s for your feedback" % self.visitorName)
        
        
        
        
    