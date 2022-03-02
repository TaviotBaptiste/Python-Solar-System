#-----------------------------
# Elève : TAVIOT Baptiste
# Classe : LP DIM
# Fonctions :
#   - Clique gauche sur une planète: 
#     - Permet de supprimer les planètes
#   - Clique gauche dans le vide: 
#     - Affiche la liste des planètes
#   - Clique droite : 
#     - Permet de créer une planète (random(RGB))
# 
# Ce qu'il fallait faire
# Contraintes et règlescommunes :
#   - [FAIT] Réalisation graphiques sous pygame
#   - [FAIT] Données structurées =les planètes doivent être représentées dans unev vstructure (classe, dictionnaire, ...)
#   - [FAIT][Respecté Dans L'ensemble] Les proportions ne sont pas toutes à respecter (en particulier la taille du soleil)
#   - [FAIT][Planètes Du Système Solaire] Le système solaire peut être fictif
#   - [FAIT] Les planètes doivent être différenciées (couleur, sprite...)
# Sujet court :
#   - [FAIT] Les vitesses doivent être proportionnelles (plus rapide à proximité du soleil)
#   - [FAIT] Les trajectoires peuvent être circulaires et non elliptiques
#   - Interaction aux choix :
#     - [FAIT] Le clic sur une planète la supprime
#     - [FAIT][Ajouter Une planète aléatoirement] Le clic dans le vide ajoute une planète
#     - autre :
#         - [FAIT]Console ( Nom planètes, Nombre de planète)
#
#
#
#-----------------------------

import pygame
import sys
import math
from math import dist, pi
import random
from pygame.locals import *
from os import system

pygame.init()

# ---BackGround Image---
stars = pygame.image.load("stars.jpg")


# ---Taille de la fenêtre / Titre---
size = width, height = 1000, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Evaluation TAVIOT Baptiste - Sujet Court")

# ---Clock---
clock = pygame.time.Clock()

# ---Constante (Couleurs)---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SUN = (255, 255, 0)
MERCURE = (255,128,0)
VENUS = (204,102,0)
TERRE = (102, 178, 255)
MARS =(255,51,51)
JUPITER = (255,178,102)
SATURNE = (255,204,153)
URANUS = (153,255,255)
NEPTUNE = (0,102,104)

# ---Class---
class PLANET:
  def __init__(self,x,y,type, size, distance,angle = 0, speed = 0, color=WHITE):
    self.x = x
    self.y = y
    self.type = type
    self.size = size
    self.distance = distance
    self.speed = speed
    self.angle = angle
    self.color = color

  def isMercure(self):
    return self.type == "isMercure"
  def isVenus(self):
    return self.type == "isVenus"
  def isTerre(self):
    return self.type == "isTerre"
  def isMars(self):
    return self.type == "isMars"
  def isJupiter(self):
    return self.type == "isJupiter"
  def isSaturne(self):
    return self.type == "isSaturne"
  def isUranus(self):
    return self.type == "isUranus"
  def isNeptune(self):
    return self.type == "isNeptune"


# ---Initialisation Variable---
i = 7
angle = 0
speed = 500
#Position soleil
position = size[0]//2, size[1]//2
#Nom des planètes généré avec le clique droit
namePlanet = [
  "Sasuke",
  "Dark Henri",
  "GotGot",
  "Hop",
  "HOP",
  "Aléatoire",
  "Planete",
  "JeanDylanDeLaValliere",
  "20/20",
  "Saphire",
  "Cristal",
  "Rubis",
  "Jacky",
  "Bricorama",
  "Saint-Félicien",
  "LesDésDeMonsieurDamas"]

planets = [
  PLANET(0,0,"isMercure",10,8,speed=speed,color=MERCURE),
  PLANET(0,0,"isVenus", 12,7,speed=speed,color=VENUS),
  PLANET(0,0,"isTerre",15,6,speed=speed,color=TERRE),
  PLANET(0,0,"isMars", 8,5,speed=speed,color=MARS),
  PLANET(0,0,"isJupiter",28,4,speed=speed,color=JUPITER),
  PLANET(0,0,"isSaturne",25,3,speed=speed,color=SATURNE),
  PLANET(0,0,"isUranus",21,2,speed=speed,color=URANUS),
  PLANET(0,0,"isNeptune",21,1.9,speed=speed,color=NEPTUNE)]


    #-----------------------------------------------------FONCTIONS
#Compter le nombre de planète total
def getNumberOfPlanet(planets):
    count = 0
    for planet in planets:
        count += 1
    return count

#Supprimer une planète
def deletePlanet(planet):

    system("clear")
    print("Il vous reste ", getNumberOfPlanet(planets), " Planete(s)")
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]

    for planet in planets:
      sqx = (x - planet.x)**2
      sqy = (y - planet.y)**2

      if math.sqrt(sqx + sqy) < planet.size:
        planets.remove(planet)
      else:
        print("Vous n'avez pas supprimé la planete : " + planet.type)

    #-----------------------------------------------------While
play = True
while play:
    mouseX,mouseY = pygame.mouse.get_pos()
    pos = (mouseY/height)*random.randint(1,10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEMOTION:
              mouse = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            #DELETE
            if event.button == 1:
              deletePlanet(planet)
            if event.button==3:
              i += 1
              planets.insert(i,PLANET(
                                    x = mouseX,
                                    y = mouseY,
                                    type = namePlanet[random.randint(0,len(namePlanet)-1)],
                                    size = random.randint(5,40),
                                    distance=pos,
                                    speed=60,
                                    color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))))
              pygame.display.update()
        if event.type == pygame.KEYUP:
            print(event.key, event.unicode, event.scancode)
            if event.key == pygame.K_ESCAPE: 
                play = False
    #-----------------------------------------------------MOVE

    # BackGround Etoile
    screen.fill((0 ,0,0))

    for planet in planets:
        planet.speed += (pi/speed)*planet.distance
        planet.x = int(size[0]//2 + size[1]//planet.distance*math.sin(planet.speed + 2 * pi))
        planet.y = int(size[1]//2 + size[1]//planet.distance*math.cos(planet.speed + 2 * pi))

    #-----------------------------------------------------DISPLAY  
    # Sun 
    pygame.draw.circle(screen, SUN, position, 50, 0)  
    # Planètes 
    for planet in planets:
        pygame.draw.circle(screen, planet.color, (planet.x, planet.y), planet.size, 0) 
    
  
    clock.tick(60)  
    pygame.display.flip()  