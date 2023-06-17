# -*- coding: utf-8 -*-
"""
Created on Mon May 15 10:07:13 2023

@author: Raghavendra
"""

class Animal:
         classification1 = "mammal"
         classification2 = "Reptiles"
         classification3 = "Birds"
         def fun(self):
            print ("Human is a classifcation of ",self.classification1)
            print ("snake is a classifcation of ",self.classification2)
            print ("Dove is a classifcation of ",self.classification3)
A = Animal()
print(A.classification1)
A.fun()