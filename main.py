# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:15:01 2019

@author: austin.schrader
"""

# import class 'Jungle' from jungleBook.py

from jungleBook import Jungle, RateJungle

def main():
    r = RateJungle("Meher", 3)
    
    r.printRating()
    
    r.welcomeMessage()
    
if __name__=='__main__':
    main()
    