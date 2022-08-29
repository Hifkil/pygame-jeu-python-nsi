# pygame-jeu-python-nsi

Jeu de case par case en python utilisant le module pygame | Projet de NSI

Pour lancer le jeu, ouvrez main.py et lancer le jeu.
Instructions pour créer une nouvelle map / niveau

Pour créer une map :
- Insérer un fichier texte dans le dossier 'Assets'
- Ajouter une constante MAP_x dans le fichier utilitaire.py menant vers
  le fichier et l'insérer dans la liste MAPS en se fiant aux autres constantes MAP

---------------------------------------------------------------------------------------------------
Légende :
- # -> mur
-   -> vide
- + -> téléporteur (inutilisé)
- * -> coffre fermé
- $ -> coffre ouvert
- ! -> torche
- D -> porte départ (grise)
- | -> porte sortie (marron)
- . -> point d'apparition du joueur

    - j -> clef jaune
    - v -> clef verte
    - r -> clef rouge

    - J -> porte jaune
    - V -> porte verte
    - R -> porte rouge

---------------------------------------------------------------------------------------------------
Exemple du niveau 2  :

#D##########################
#.                        !#
#########################  #
#                          #
##### #################### #
#!#                   R !# #
#v######### ###########  # #
#J#   #   #   ####   ### # #
#   #   # # ## j#  #  ##*# #
######### # #  ### ## #### #
#           #       #    # #
#V#### ################# ###
#r#                      #|#
#J######################## #
#           !!!            *
############################
