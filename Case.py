# -*- coding: utf-8 -*-

""" Module stockant la classe Case du Jeu Vidéal """

#- Section importations ---------------------------------------------------------------------------
from utilitaire import *

#- Section classes --------------------------------------------------------------------------------
class Case:
    """ Permet des créer les cases du labyrinthe,\n
    Méthodes :
    - __init__(self, type, coord)
    - __str__(self)
    - changer_type(self, nouv_type)
    - afficher_grille(afficher=False)

    Attributs :
    - self.type  -> str définissant le type de la case ('mur', 'vide', 'sortie'...)
    - self.image -> image permettant de représenter la case sur l'écran
    - self.coord -> tuple de 2 int correspondants à l'abscisse et l'ordonnée de la case (EN PIXELS) """
    def __init__(self, type:str, coord:tuple):
        """ - type  -> type de la case ('mur', 'vide', 'sortie'...)
                - NOTE : les types existants sont définits dans un dictionnaire dans utilitaire.py -> DICO_TYPE
            - coord -> tuple de 2 int correspondants à l'abscisse et l'ordonnée de la case 
                - EXEMPLE : (x * COTE_CASE, y * COTE_CASE) où x et y sont des entiers correspondants à l'abscisse et l'ordonnée de la case DU JEU (pas en pixels) """
        self.coord = coord
        self.type  = type
        # Attribut une image à la case en fonction de son attribut self.type grâce à un dictionnaire
        for type_case, image_case in DICO_TYPE.items():
            if self.type == type_case:
                self.image = image_case

    def __str__(self) -> str: # Surtout utile pour debug
        """ Renvoie le type suivit des coordonnées de la case sous forme de tuple """
        return str((self.type, self.coord, self.image))

    def changer_type(self, nouv_type:str): # C'est comme dans __init__ mais on ne change pas les coordonnées
        """ Change le type de la case et donc son image par la suite, mais pas ses coordonées
        - nouv_type -> comme type lorsqu'on crée une case """
        self.type = nouv_type
        for type_case, image_case in DICO_TYPE.items():
            if self.type == type_case:
                self.image = image_case

    def afficher_grille(afficher=False):
        """ Affiche une grille montrant les cases du jeu,\n
        n'affiche rien par défaut, nécéssite d'appuyer sur la touche G """
        touche = pg.key.get_pressed()
        if touche[pg.K_g]:  # Permet d'afficher la grille quand G est pressé
            if afficher == True:
                afficher = False
            elif afficher == False:
                afficher = True

        # Affiche la grille si afficher est True
        if afficher:
            for x in range(0, WIDTH, COTE_CASE):
                for y in range(0, HEIGHT, COTE_CASE):
                    case = pg.Rect(x, y, COTE_CASE, COTE_CASE)
                    pg.draw.rect(FEN, GRIS, case, 1)