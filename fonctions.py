# -*- coding: utf-8 -*-

""" Module stockant toutes les fonctions du Jeu Vidéal """

#- Section importation ----------------------------------------------------------------------------
import pygame as pg

#- Section fonctions ------------------------------------------------------------------------------
def scale_image(image, facteur):
    """ Redimensionne la longueur et la hauteur d'une image
    par un facteur, l'image sera donc un carré, cela ne gêne pas encore 
    image   -> nom de l'image (case.png, torche.png)
    facteur -> nouvelle dimension de l'image """
    # L'idée est de mettre la taille de l'image à 0 puis d'ajouter le facteur
    taille = round(image.get_width()*0 + facteur), round(image.get_height()*0 + facteur)
    return pg.transform.scale(image, taille)