##
## Anubis Engine
##
## Window Class
## v.0.0.1.0
##
## Used as a main, easily addressable window that
## wraps the pygame methods into multiple better
## methods that will be addressed by nodes once
## the nodes system is implemented.  The window
## class is also perpetual, so resolution and
## more can be changed dynamically without having
## to worry about changing the variable.
##

##Necessary imports
import pygame
import sys

class Window():
    def __init__(self, resolution, framerate):

        ##
        ## Main Window Class
        ##
        ## Takes two parameters:
        ##
        ## - resolution:
        ##   Type: Tuple
        ##   Usage: Defines the resolution of the window
        ##
        ## - framerate:
        ##   Type: Integer
        ##   Usage: Defines the refresh rate of the window
        ##   Notes: Can be set to None to refresh at maximum rate
        ##

        self.resolution = resolution
        self.framerate = framerate

        self.windowObject = pygame.display.set_mode(self.resolution)
        self.clockObject = pygame.time.Clock()
        
        self.active = True
        self.trueFPS = None

        self.tickEvents = []

    def getEvents(self):
        

    def mainLoop(self):

        ##
        ## Main Window Class Loop
        ##
        ## Takes no Parameters
        ##

        while(self.active == True):
            
            pygame.display.update()
            
            if(self.framerate != None):
                self.clockObject.tick(self.framerate)
            else:
                self.clockObject.tick()

            self.trueFPS = self.clockObject.get_fps()

            
