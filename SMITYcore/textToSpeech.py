#
# Script created by Theodore Economides (Θεόδωρος Οικονομίδης)
#

## Sources :
##      https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
##      https://pyttsx3.readthedocs.io/en/latest/engine.html

import pyttsx3
from SMITY.SMITYcore.printToGUI import print2gui
from SMITY.SMITYcore.singleton import Singleton


class Text2Speech(metaclass=Singleton):
    __engine = None


    def __init__(self, rate=125, volume=1.0):
        ## ------------------------------------------------------
        ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
        ## ------------------------------------------------------

        self.__engine = pyttsx3.init()  # object creation

        # ----- RATE -----

        self.__engine.setProperty('rate', rate)  # setting up voice rate

        # ----- VOLUME -----

        self.__engine.setProperty('volume', volume)  # setting up volume level

    def speak(self, toSay):
        ## ------------------------------------------------------
        ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
        ## ------------------------------------------------------

        ##
        ## Prints to GUI what is going to be said. Then begins to say it.
        ##

        print2gui('S.M.I.T.Y. : ', toSay)

        self.__engine.say(toSay)

        self.__engine.runAndWait()
        # Stops the current utterance and clears the command queue.
        self.__engine.stop()

