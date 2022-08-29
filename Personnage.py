# -*- coding: utf-8 -*-

""" Module stockant la classe Personnage du Jeu Vidéal """

#- Section importations ---------------------------------------------------------------------------
from utilitaire import *

import pygame as pg

#- Section classes --------------------------------------------------------------------------------
class Personnage:
    """ Définie le personnage,\n
    Méthodes : 
    - __init__(self, coord_apparition, vie)
    - afficher_vie(self)
    - deplacement(self, coord_cases_utiles)

    Attributs : 
    - self.perso -> hitbox du personnage
    - self.vie   -> nombre de points de vie du personnage """
    def __init__(self, coord_apparition:list, vie:int):
        """ - coord_apparition -> coordonées d'apparition du personnage dans une liste [x, y]
            - vie              -> nombre de points de vie du personnage lorsqu'il commence (ou recommence) un niveau """
        self.perso = pg.Rect(coord_apparition[0], coord_apparition[1], # Coordonnées d'apparition : x et y
                             COTE_CASE, COTE_CASE)                     # Taille de la hitbox      : longueur et hauteur
        self.vie = vie

    def afficher_vie(self):
        """ Affiche les points de vie du personnage sur la fenêtre,\n
        La barre de vie est un rectangle vert situé en bas à gauche de la fenêtre avec écrit "Barre de vie : " """
        pg.draw.rect(FEN, VERT,
            [3*COTE_CASE, 16.5*COTE_CASE, self.vie*COTE_CASE, COTE_CASE//3]) # La longueur dépend donc de la vie
        #   | abscisse  | ordonnée    | longueur          | hauteur

        FEN.blit(BARRE_DE_VIE, (3*COTE_CASE, 16*COTE_CASE))

    def deplacement(self, coord_cases_utiles:dict):
        """ Gère les déplacements du joueur grâce aux touches fléchées
        Fait en sorte que le joueur ne puisse pas sortir de l'écran ou
        rentrer dans un bloc dans lequel il ne doit pas rentrer
        - coord_cases_utiles -> liste contenant les coordonnées x et y en tuple
                              de chaque bloc utile, voir dans Jeu.__init__() pour tout voir """
        touche = pg.key.get_pressed()
        # GAUCHE
        if touche[pg.K_LEFT] and (self.perso.x - COTE_CASE) > -1: # Permet de ne pas sortir de l'écran
            if (self.perso.x - COTE_CASE, self.perso.y) not in coord_cases_utiles['blocs_durs']: # Ne rentre pas dans les blocs durs
                if (self.perso.x - COTE_CASE, self.perso.y) not in coord_cases_utiles['portes']['jaune'] and (self.perso.x - COTE_CASE, self.perso.y) not in coord_cases_utiles['portes']['verte'] and (self.perso.x - COTE_CASE, self.perso.y) not in coord_cases_utiles['portes']['rouge']:
                    self.perso.x -= COTE_CASE
                    if (self.perso.x, self.perso.y) in coord_cases_utiles['torches']:
                        self.vie -= 1
                    pg.time.delay(PERSO_VITESSE)
        # DROITE
        elif touche[pg.K_RIGHT] and (self.perso.x + COTE_CASE) < WIDTH:
            if (self.perso.x + COTE_CASE, self.perso.y) not in coord_cases_utiles['blocs_durs']:
                if (self.perso.x + COTE_CASE, self.perso.y) not in coord_cases_utiles['portes']['jaune'] and (self.perso.x + COTE_CASE, self.perso.y) not in coord_cases_utiles['portes']['verte'] and (self.perso.x + COTE_CASE, self.perso.y) not in coord_cases_utiles['portes']['rouge']:
                    self.perso.x += COTE_CASE
                    if (self.perso.x, self.perso.y) in coord_cases_utiles['torches']:
                        self.vie -= 1
                    pg.time.delay(PERSO_VITESSE)
        # HAUT
        elif touche[pg.K_UP] and (self.perso.y - COTE_CASE) > -1:
            if (self.perso.x, self.perso.y - COTE_CASE) not in coord_cases_utiles['blocs_durs']:
                if (self.perso.x, self.perso.y - COTE_CASE) not in coord_cases_utiles['portes']['jaune'] and (self.perso.x, self.perso.y - COTE_CASE) not in coord_cases_utiles['portes']['verte'] and (self.perso.x, self.perso.y - COTE_CASE) not in coord_cases_utiles['portes']['rouge']:
                    self.perso.y -= COTE_CASE
                    if (self.perso.x, self.perso.y) in coord_cases_utiles['torches']:
                        self.vie -= 1
                    pg.time.delay(PERSO_VITESSE)
        # BAS
        elif touche[pg.K_DOWN] and (self.perso.y + COTE_CASE) < HEIGHT:
            if (self.perso.x, self.perso.y + COTE_CASE) not in coord_cases_utiles['blocs_durs']:
                if (self.perso.x, self.perso.y + COTE_CASE) not in coord_cases_utiles['portes']['jaune'] and (self.perso.x, self.perso.y + COTE_CASE) not in coord_cases_utiles['portes']['verte'] and (self.perso.x, self.perso.y + COTE_CASE) not in coord_cases_utiles['portes']['rouge']:
                    self.perso.y += COTE_CASE
                    if (self.perso.x, self.perso.y) in coord_cases_utiles['torches']:
                        self.vie -= 1
                    pg.time.delay(PERSO_VITESSE)