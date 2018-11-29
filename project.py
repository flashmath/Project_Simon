from graphics_isn import *
from random import *

def distance(P):
    '''
    Détermine la distance au centre de la fenêtre
    :param P: Point du clique
    :return: retourne la distance
    '''
    return sqrt((P.x-450)**2+(P.y-300)**2)


def getColor(P):
    '''
    Détermine la couleur sous la souris
    :param P: Point du clique
    :return: retourne la couleur si elle existe sinon rien
    '''
    value = None
    dis=distance(P)
    if dis<125 or dis>250:
        return None
    else :
        if P.x<450:
            if P.y<300:
                return green
            else:
                return red
        else:
            if P.y<300:
                return yellow
            else:
                return blue

def ObtenirColor():
    '''
    Atteint un clique correct jusqu'à la bonne couleur
    :return: couleur cliquer
    '''
    color = None
    while color==None:
        color=getColor(wait_clic())
    return color

def joueSon(c):
    if c==green:
        F="green.wav"
    elif c==blue:
        F="blue.wav"
    elif c==red:
        F="red.wav"
    else:
        F="yellow.wav"
    play_sound(F)

def sequence(D):
    '''
    Ajoute un élément à la séquence de couleurs
    :param D: séquence d'origine
    :return: nouvelle séquence
    '''
    couleurs = [red,green,blue,yellow]
    element=choice(couleurs)
    D.append(element)
    return D

def AffichageFixe():
    # Initialisation de la fenêtre graphique
    O=Point(450,300)
    draw_fill_sector(O,250,0,pi/2,red)
    draw_fill_sector(O,250,pi/2,pi,green)
    draw_fill_sector(O,250,pi,3*pi/2,yellow)
    draw_fill_sector(O,250,3*pi/2,2*pi,blue)
    draw_fill_circle(O,125,black)
    return 0

def affichageBase(couleur):
    O = Point(450, 300)
    draw_fill_rectangle(O, 900, 600, black)
    AffichageFixe()
    draw_fill_circle(O, 100, couleur)
    return 0

def afficheJeu(D):
    affichageBase(D[0])
    joueSon(D[0])
    return 0

def affichePerdu(D):
    return 0

def Tour(D):
    D=sequence(D)
    afficheJeu(D)
    i=0
    perdu = False
    while (i<len(D)) and not perdu:
        couleur = ObtenirColor()
        perdu=couleur!=D[i]
        i+=1
    if perdu:
        affichePerdu(D)
    else:
        Tour(D)

def game():
    D=sequence([])
    Tour(D)

def main():
    init_graphic(900,600,"Simon")

    game()
    #color = ObtenirColor()
    #joueSon(color)
    #draw_fill_circle(Point(450,300),125,color)

    wait_escape()
    return 0

main()