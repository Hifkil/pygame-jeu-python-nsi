# -*- coding: utf-8 -*-

""" Module stockant toutes les constantes et fonctions du Jeu Vidéal """

#- Section importations ---------------------------------------------------------------------------
import pygame as pg
import os
import sys

pg.init() # Initialise les modules de pygame

#- Section fonctions ------------------------------------------------------------------------------
def scale_image(image:pg.Surface, facteur:int) -> pg.Surface: # Utilisé uniquement dans ce fichier pour l'instant
    """ Redimensionne la longueur et la hauteur d'une image par un facteur\n
    l'image sera donc un carré, cela ne gêne pas encore\n
    - image   -> nom de l'image (case.png, torche.png)\n
    - facteur -> nouvelle longueur et hauteur de l'image (en pixels)\n
    EXEMPLE : scale_image(pg.image.load(os.path.join('Assets', 'joueur.png')), COTE_CASE) """
    # L'idée est de mettre la taille de l'image à 0 puis d'ajouter le facteur
    taille = round(image.get_width()*0 + facteur), round(image.get_height()*0 + facteur)
    return pg.transform.scale(image, taille)

#- Section constantes -----------------------------------------------------------------------------
COTE_CASE = 40

LONGUEUR_MAP = 28 # En cases
HAUTEUR_MAP  = 17

WIDTH, HEIGHT = LONGUEUR_MAP*COTE_CASE, HAUTEUR_MAP*COTE_CASE
FEN = pg.display.set_mode((WIDTH, HEIGHT))
FPS = 60

PERSO_VITESSE = 125 # En millisecondes
PV_DEBUT = 3        # Nombre de points de vie lorsque le personnage commence le jeu ou recommence un niveau en mourant

MAP_1 = os.path.join('Assets', 'Map_1.txt')
MAP_2 = os.path.join('Assets', 'Map_2.txt')
MAP_3 = os.path.join('Assets', 'Map_3.txt')
MAP_4 = os.path.join('Assets', 'Map_4.txt')
MAP_5 = os.path.join('Assets', 'Map_5.txt')

MAPS  = [MAP_1, MAP_2, MAP_3, MAP_4, MAP_5]

# Charge les images :          pygame          os       nom dossier, nom image       Nouv. taille
# Redimensionne les images [             {            (                             )}           ]
JOUEUR        = scale_image(pg.image.load(os.path.join('Assets', 'joueur.png'       )), COTE_CASE)

CASE_VIDE     = scale_image(pg.image.load(os.path.join('Assets', 'case_vide.png'    )), COTE_CASE)
MUR           = scale_image(pg.image.load(os.path.join('Assets', 'mur.png'          )), COTE_CASE)
CASE_TELEPORT = scale_image(pg.image.load(os.path.join('Assets', 'teleporteur.png'  )), COTE_CASE)
SORTIE        = scale_image(pg.image.load(os.path.join('Assets', 'porte_sortie.png' )), COTE_CASE)
PORTE_GRISE   = scale_image(pg.image.load(os.path.join('Assets', 'porte_grise.png'  )), COTE_CASE)

CLEF_JAUNE    = scale_image(pg.image.load(os.path.join('Assets', 'clef_jaune.png'   )), COTE_CASE)
CLEF_VERTE    = scale_image(pg.image.load(os.path.join('Assets', 'clef_verte.png'   )), COTE_CASE)
CLEF_ROUGE    = scale_image(pg.image.load(os.path.join('Assets', 'clef_rouge.png'   )), COTE_CASE)
PORTE_JAUNE   = scale_image(pg.image.load(os.path.join('Assets', 'porte_jaune.png'  )), COTE_CASE)
PORTE_VERTE   = scale_image(pg.image.load(os.path.join('Assets', 'porte_verte.png'  )), COTE_CASE)
PORTE_ROUGE   = scale_image(pg.image.load(os.path.join('Assets', 'porte_rouge.png'  )), COTE_CASE)

COFFRE_OUVERT = scale_image(pg.image.load(os.path.join('Assets', 'coffre_ouvert.png')), COTE_CASE)
COFFRE_FERME  = scale_image(pg.image.load(os.path.join('Assets', 'coffre_ferme.png' )), COTE_CASE)

TORCHE        = scale_image(pg.image.load(os.path.join('Assets', 'torche.png'       )), COTE_CASE)

liste_images = [JOUEUR, CASE_VIDE, MUR, CASE_TELEPORT, SORTIE, PORTE_GRISE,
                CLEF_JAUNE, CLEF_VERTE, CLEF_ROUGE, PORTE_JAUNE, PORTE_VERTE, PORTE_ROUGE,
                COFFRE_OUVERT, COFFRE_FERME, TORCHE]

# Conversion des images, je sais plus pourquoi mais c'est mieux
for i in liste_images:
    i.convert()

# symbole (dans le fichier texte) -> type
DICO_CARACTERE = {'#':'mur', ' ':'vide', '+':'teleporteur', '*':'coffre_ferme', '$':'coffre_ouvert', '!':'torche',
                  'j':'clef_jaune', 'v':'clef_verte', 'J':'porte_jaune', 'V':'porte_verte',
                  'r':'clef_rouge', 'R':'porte_rouge',
                  'D':'porte_depart', '|':'sortie', '.':'depart'}
# type -> image
DICO_TYPE = {None:None, 'mur':MUR, 'vide':CASE_VIDE, 'teleporteur':CASE_TELEPORT,
             'coffre_ferme':COFFRE_FERME, 'coffre_ouvert':COFFRE_OUVERT, 'torche':TORCHE,
             'clef_jaune':CLEF_JAUNE, 'clef_verte':CLEF_VERTE, 'porte_jaune':PORTE_JAUNE, 'porte_verte':PORTE_VERTE,
             'clef_rouge':CLEF_ROUGE, 'porte_rouge':PORTE_ROUGE,
             'porte_depart':PORTE_GRISE, 'sortie':SORTIE, 'depart':CASE_VIDE}

# Couleurs R    V    B
VERT   = (111, 210, 46)
GRIS   = (128, 128, 128)
VIOLET = (138, 25, 158)
NOIR   = (0, 0, 0)

POLICE_VIE   = pg.font.SysFont('chalkduster.ttf', COTE_CASE//2) # On definit la police (nom de la police, taille de la police)
BARRE_DE_VIE = POLICE_VIE.render('Barre de vie :', True, VERT) # On met le texte et la couleur

POLICE_FIN = pg.font.SysFont('chalkduster.ttf', COTE_CASE*2)
TEXTE_FIN  = POLICE_FIN.render('Bravo, tu as terminé le jeu !', True, VIOLET)