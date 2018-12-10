from graphics_isn import *
from random import *

O = Point(450,300)
D=[];

def clear_score():
    text = "Score : "
    posx = 20
    posy = hauteur_texte(text, 12) + 10
    draw_fill_rectangle(Point(60, posy), 200, 30, black)

def aff_score(score):
    clear_score()
    posx = 20
    text = "Score : "
    posy = hauteur_texte(text,12)+10
    aff_pol(text+str(score),12,Point(posx,posy),white)

def aff(text):
    h = hauteur_texte(text,12)
    l = largeur_texte(text,12)
    posx=(900-l)//2
    aff_pol(text,12,Point(posx,20),white)

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
                return yellow
        else:
            if P.y<300:
                return red
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
    affichageBase(color)
    joueSon(color)
    attendre(500)
    affichageBase(black)
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

def loadImages(D):
    D.append(pygame.image.load("Images/base.jpg").convert())
    D.append(pygame.image.load("Images/green.jpg").convert())
    D.append(pygame.image.load("Images/red.jpg").convert())
    D.append(pygame.image.load("Images/blue.jpg").convert())
    D.append(pygame.image.load("Images/yellow.jpg").convert())
    return D

def AffichageFixe(D):
    # Initialisation de la fenêtre graphique
    global O
    window = pygame.display.get_surface()
    window.blit(D[0], (0, 0))
    #draw_fill_sector(O,250,0,pi/2,red)
    #draw_fill_sector(O,250,pi/2,pi,green)
    #draw_fill_sector(O,250,pi,3*pi/2,yellow)
    #draw_fill_sector(O,250,3*pi/2,2*pi,blue)
    #draw_fill_circle(O,125,black)
    return 0

def affichageBase(Img,couleur):
    global O
    #draw_fill_circle(O, 100, couleur)
    window = pygame.display.get_surface()
    if couleur==black:
        window.blit(Img[0],(0,0))
    elif couleur==green:
        window.blit(Img[1], (0, 0))
    elif couleur==red:
        window.blit(Img[2], (0, 0))
    elif couleur==blue:
        window.blit(Img[3], (0, 0))
    elif couleur==yellow:
        window.blit(Img[4], (0, 0))
    return 0

def afficheJeu(Img,D):
    for k in D:
        affichageBase(Img,k)
        joueSon(k)
        attendre(2000)
        affichageBase(Img,black)
        attendre(500)
    return 0

def affichePerdu(D):
    aff("Perdu")
    afficheJeu(D)

def Tour(Img,D):
    aff_score(len(D))
    D=sequence(D)
    afficheJeu(Img,D)
    i=0
    perdu = False
    while (i<len(D)) and not perdu:
        couleur = ObtenirColor()
        perdu=couleur!=D[i]
        i+=1
    if perdu:
        #affichePerdu(D)
        return len(D)-1
    else:
        attendre(2000)
        return Tour(D)

def game():
    #D=sequence([])
    #D=sequence([blue,yellow])
    Img=loadImages([])
    AffichageFixe(Img)
    D=[]
    score=Tour(Img,D)
    #aff("Score = "+str(score))

def main():
    init_graphic(900,600,"Simon")

    game()
    #color = ObtenirColor()
    #joueSon(color)
    #draw_fill_circle(Point(450,300),125,color)

    wait_escape()
    return 0

main()