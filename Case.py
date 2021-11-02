# -*- coding: utf-8 -*-

""" Module Stockant la classe Case du Jeu Vidéal """

#- Section importation ----------------------------------------------------------------------------
from fonctions import scale_image

import pygame as pg
import os # L'utilisation de ce module permet la compatibilité du jeu sur d'autres plateformes

#- Section constantes -----------------------------------------------------------------------------
COTE_CASE = 50

# Légende :                    pygame          os       nom dossier, nom image       Nouv. taille
# Redimensionne les images [             {            (                             )}           ]
CASE_VIDE     = scale_image(pg.image.load(os.path.join('Assets', 'case_vide.png'    )), COTE_CASE)
CASE_MUR      = scale_image(pg.image.load(os.path.join('Assets', 'mur.png'          )), COTE_CASE)
CASE_TELEPORT = scale_image(pg.image.load(os.path.join('Assets', 'teleporteur.png'  )), COTE_CASE)
CASE_SORTIE   = scale_image(pg.image.load(os.path.join('Assets', 'porte_sortie.png' )), COTE_CASE)

CLEF_JAUNE    = scale_image(pg.image.load(os.path.join('Assets', 'clef_jaune.png'   )), COTE_CASE)
CLEF_VERTE    = scale_image(pg.image.load(os.path.join('Assets', 'clef_verte.png'   )), COTE_CASE)
PORTE_JAUNE   = scale_image(pg.image.load(os.path.join('Assets', 'porte_jaune.png'  )), COTE_CASE)
PORTE_VERTE   = scale_image(pg.image.load(os.path.join('Assets', 'porte_verte.png'  )), COTE_CASE)

COFFRE_OUVERT = scale_image(pg.image.load(os.path.join('Assets', 'coffre_ouvert.png')), COTE_CASE)
COFFRE_FERME  = scale_image(pg.image.load(os.path.join('Assets', 'coffre_ferme.png' )), COTE_CASE)

TORCHE        = scale_image(pg.image.load(os.path.join('Assets', 'torche.png'       )), COTE_CASE)

#- Section classe ---------------------------------------------------------------------------------
class Case:
    """ Permet des créer les cases du labyrinthe,
    Méthodes  : __init__(self, type, coord)
    Attributs : self.type  -> str définissant le type de la case -> 'mur', 'vide', 'sortie'...
                self.coord -> tuple de 2 int correspondants à l'abscisse et l'ordonnée de la case
                self.image -> image permettant de représenter la case sur l'écran """
    def __init__(self, type, coord):
        """ type  : str définissant le type de la case -> 'mur', 'vide', 'sortie'...
            coord : tuple de 2 int -> (x*COTE_CASE, y*COTE_CASE) où x et y sont des entiers
                                      correspondants à l'abscisse et l'ordonnée de la case
            types existants : 'vide', 'mur', 'teleporteur', 'sortie', 'clef_jaune', clef_verte',
                              'porte_jaune', 'porte_verte', 'coffre_ferme', 'torche' """
        self.type = type
        self.coord = coord
        # Attribut une image à la case en fonction de son attribut self.type
        if self.type == None:
            self.image = None
        elif self.type == 'vide':
            self.image = CASE_VIDE
        elif self.type == 'mur':
            self.image = CASE_MUR
        elif self.type == 'teleporteur':
            self.image = CASE_TELEPORT
        elif self.type == 'sortie':
            self.image = CASE_SORTIE
        elif self.type == 'clef_jaune':
            self.image = CLEF_JAUNE
        elif self.type == 'clef_verte':
            self.image = CLEF_VERTE
        elif self.type == 'porte_jaune':
            self.image = PORTE_JAUNE
        elif self.type == 'porte_verte':
            self.image = PORTE_VERTE
        elif self.type == 'coffre_ferme':
            self.image = COFFRE_FERME
        elif self.type == 'torche':
            self.image = TORCHE