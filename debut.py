from pygame import *
from graphics_isn import *

def getLevel(P):
    value = None
    if P.x<305 or P.x>595:
        return None
    else:
        if P.y>190 and P.y<245:
            value=1
        elif P.y>270 and P.y<325:
            value=2
        elif P.y>353 and P.y<408:
            value=3
    return value

def ObtenirLevel():
    level = None
    while level==None:
        level=getLevel(wait_clic())
    return level

def menu_start(pygame):
    window = pygame.display.get_surface()
    img = pygame.image.load("Images/menu_demmarage.jpg").convert()
    window.blit(img, (0, 0))
    return ObtenirLevel()