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

def main():        
    # create object of class Jungle
    j = Jungle("Meher")
    j.welcomeMessage()
    
    k = Jungle()
    k.welcomeMessage()

# standard boilerplate to set 'main' as starting function
if __name__=='__main__':
    main()
    
