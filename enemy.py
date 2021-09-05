import pygame
import random
import sys
from game_settings import *

vec = pygame.math.Vector2


class Enemy:
    def __init__(self, app, pos, number):
        self.app = app
        self.grid_pos = pos
        
        self.pix_pos = self.get_pix_pos()
        self.radius = int(self.app.cell_width//2.3)
        self.number = number
        self.colour = self.set_colour()
        self.green = GREEN

        self.target = None
   
    def update(self):
        pass

      

    def draw(self):
        pygame.draw.circle(self.app.screen, self.colour,
                           (int(self.pix_pos.x), int(self.pix_pos.y)), self.radius)


    def get_pix_pos(self):
        return vec((self.grid_pos.x*self.app.cell_width)+TOP_BOTTOM_BUFFER//2+self.app.cell_width//2,
                   (self.grid_pos.y*self.app.cell_height)+TOP_BOTTOM_BUFFER//2 +
                   self.app.cell_height//2)

    def set_colour(self):
        if self.number == 0:
            return VIOLET
        if self.number == 1:
            return WHITE
        if self.number == 2:
            return GREEN
        if self.number == 3:
            return BLUE

    
