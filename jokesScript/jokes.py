"""
Created on Sat Mar 27 13:08:39 2021

@author: manolispolymeneris
"""

import pyjokes #Imports random joke generator library

def jokes():

    for i in range(9, 105): #Runs the list with jokes
        joke = pyjokes.get_joke() #Generates a joke
        print(joke) #Prints the joke
        
        return 0

jokes()
