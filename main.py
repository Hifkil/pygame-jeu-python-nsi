""" Jeu vidéo de labyrinthe utilisant pygame pour un DM en NSI
Auteurs : Harry, Corentin """

#- Section importations et initialisations --------------------------------------------------------
import pygame as pg
import os

pg.init() # Initialise les modules de pygame, on ne les utilises pas encore

#- Section constantes -----------------------------------------------------------------------------
WIDTH, HEIGHT = 1000, 600
COULEUR=(73, 13, 99)
fen = pg.display.set_mode((WIDTH, HEIGHT))
MAP = "Map.txt"
FPS=60
PPRINCIPAL=pg.image.load(os.path.join('Assets','hitcircle.png'))
PPRINCIPAL=pg.transform.rotate(PPRINCIPAL,180)
#- Section des classes ----------------------------------------------------------------------------
class Personnage:
    """ Définie le personnage """
    def __init__(self):
        self.vie = 3


class Case:
    """ Gère les cases du jeu """
    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y

    def type_case(self):
        """ Permet de savoir quel est le type d'une case """
        pass
    
    def deplacement(self):
        intpu=pg.key.get_pressed()
        if intpu[pg.K_UP]:
            

class Jeu:
    """ Permet de jouer lol """
    def __init__(self):
        pass

    def affiche(self):
        """ :) """
        pass

    def dessin_win(self):
        fen.fill(COULEUR)
        fen.blit(PPRINCIPAL,(140,140))
        pg.display.update()   

    def demarre(self):
        """ Démarre une partie """
        pg.display.set_caption("Jeu Vidéal")
        clock= pg.time.Clock()
        running = True  
        while running:
            clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            Jeu.dessin_win(self)



#- Section principale -----------------------------------------------------------------------------
if __name__ == '__main__': # Permet de ne pas lancer le jeu si on importe le jeu en tant que module
    partie = Jeu()
    partie.demarre()
    # partie.dessin_win()
    pg.quit()
