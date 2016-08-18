#Don't Edit This File.
#Please Install Python 3.2.5 and Pygame(pygame.org/wiki)
#Input your display size in variable 'width, height'.
width, height = 1366, 768
import pygame
from pygame.locals import *
pygame.init()
window = pygame.display.set_mode([yourdisplaysize])
window.fill(pygame.Color(255, 255, 255))
fps= pygame.time.Clock()
while True:
  for event in pygame.event.get():
    if event.type == MOUSEMOTION:
      mouseX, mouseY = event.pos
    if event.type == MOUSEBUTTONDOWN:
      window.fill(pygame.Color(255,255,255))
  radius = (abs(width/2 - mouseX)+abs(height/2 - mouseY))/2 + 1
  pygame.draw.circle(window,
                     pygame.Color(255, 0, 0),
                     (mouseX, mouseY),
                     radius, 1)
  pygame.display.update()
  fps.tick(30)
