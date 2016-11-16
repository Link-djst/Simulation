import pygame, math, random, sys
import numpy as np
import random as r
from pygame.locals import *

WIDTH = 640
HEIGHT = 480
MAX_DISTANCE = math.sqrt(math.pow(WIDTH) + math.pow(HEIGHT))

class Mosquitoe(pygame.sprite.Sprite):
 "Returns: mosquitoe object"
 "Function: update, new_pos"
 "Atributes: vector"

 def __init__(self, vector, position):
  pygame.sprite.Sprite.__init__(self)
  self.image = pygame.Surface([10, 10])
  self.image = self.image.convert()
  self.image.fill((20,20,20))
  self.rect = self.image.get_rect()
  self.rect.x, self.rect.y  = position
  self.vector = vector
  "input layer"
  self.input0 = 0
  self.input1 = 0
  self.input2 = 0
  self.input3 = 0
  self.input4 = 0

 def update(self):
  self.rect = self.new_pos(self.rect, self.vector)

 def new_pos(self, rect, vector):
  "Vector with the direction and how much to move"
  (angle, z) = vector
  #print np.rad2deg(angle)
  (dx,dy) = (z*np.cos(angle), -z*np.sin(angle))
  #print (dx, dy)
  if (rect.centerx>0 and rect.centerx<WIDTH) and (rect.centery>0 and rect.centery<HEIGHT):
    #print "Im a good guy "
    return rect.move(dx,dy)
  else:
    return rect.move(0,0)

 def draw(self, surface):
  surface.blit(self.image, (self.rect.x, self.rect.y))

 def angle_between(self, object_to):
  dx = float(self.rect.centerx - object_to.rect.centerx)
  dy = float(self.rect.centery - object_to.rect.centery)
  rads = math.atan2(-dy,dx)
  #print np.rad2deg(rads)
  return rads

 def distance_between(self, object_to):
  dx = float(self.rect.centerx - object_to.rect.centerx)
  dy = float(self.rect.centery - object_to.rect.centery)
  z = np.sqrt(np.power(dx,2) + np.power(dy,2))
  return z

 def distance_between_food(self, list_of_food):
  "Reset Input Layer"
  self.input0 = MAX_DISTANCE
  self.input1 = MAX_DISTANCE
  self.input2 = MAX_DISTANCE
  self.input3 = MAX_DISTANCE
  self.input4 = MAX_DISTANCE
  for f in list_of_food:
   rads = self.angle_between(f)
   temp_distance = self.distance_between(f)
   print np.rad2deg(rads)
   print temp_distance
   if np.rad2deg(rads) < 15 and np.rad2deg(rads) > -15 and self.input2 > temp_distance:
    self.input2 = self.distance_between(f)
   elif np.rad2deg(rads) < 35 and np.rad2deg(rads) > 15 and self.input1 > temp_distance:
    self.input1 = self.distance_between(f)
   elif np.rad2deg(rads) < 45 and np.rad2deg(rads) > 35 and self.input0 > temp_distance:
    self.input0 = self.distance_between(f)
   elif np.rad2deg(rads) < -15 and np.rad2deg(rads) > -35 and self.input3 > temp_distance:
    self.input3 = self.distance_between(f)
   elif np.rad2deg(rads) < -35 and np.rad2deg(rads) > -45 and self.input4 > temp_distance:
    self.input4 = self.distance_between(f)

"Screen"
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('GANN')

"Fill background"
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

moscos = []

for i in range(30):
    moscos.append(Mosquitoe((r.randint(1,360), r.randint(2,3)), (r.randint(0,639), r.randint(0,476))))

"Init clock"
clock = pygame.time.Clock()

while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   sys.exit()
  elif event.type == KEYDOWN:
   if event.key == K_ESCAPE:
    sys.exit()

 screen.blit(background, (0, 0))

 for mosco in moscos:
  mosco.update()
  mosco.draw(screen)

 "60 fps"
 clock.tick(60)
 pygame.display.update()
