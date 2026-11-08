---
title: Projet Python
---

# Projet Python : Mini-Maze (petit labyrinthe)

<link rel="stylesheet" href="../../assets/style.css" />


## Séance 1 : Découverte

Pour réaliser notre jeu, nous allons utiliser le langage Python, et plus particulièrement la bibliothèque Pyxel, déjà installée sur Thonny.

Le but de cette séance est de comprendre et manipuler plusieurs éléments importants de cette bibliothèque.

Chaque semaine, nous améliorerons le code en ajoutant plusieurs fonctionnalités pour obtenir, au final, un jeu ressemblant à un classique du jeu vidéo : <a href="https://fr.wikipedia.org/wiki/Pac-Man" target="_blank">Pac-Man</a>.

## Pyxel : l’essentiel à connaître avant de coder

Pyxel est une bibliothèque Python spécialisée dans la création de **jeux rétro 2D**.

Un jeu Pyxel repose toujours sur la même structure.

```python
import pyxel # import de la bibliothèque pyxel pour coder votre jeu

def update():
    """
    logique du jeu (calculs, déplacements, collisions)
    """
    pass

def draw():
    """
    affichage à l’écran
    """
    pyxel.cls(0)

pyxel.init(128, 128, title="Mon jeu") # crée la fenêtre du jeu, ici une fenêtre de 128 par 128 pixel, avec pour titre "Mon jeu"

pyxel.run(update, draw) # lance la boucle du jeu, avec en paramètre les fonctions de jeu et de dessin
```

Avec : 

- **import pyxel** : importe la bibliothèque pyxel dans votre script Python
- **def update()** : crée la fonction qui s'occupera des mécaniques de votre jeu ( *« le personnage avance de 1 », « on a appuyé sur la flèche gauche », « le score augmente »* ), on ne dessine rien ici : on prépare seulement ce qui va se passer.
- **def draw()** : crée la fonction où l’on affiche. On efface l’écran, puis on dessine le texte, les formes, le personnage, aux positions calculées par update. On n’y calcule rien : on dessine seulement ce qu’on a décidé.
- **pyxel.init(128, 128, title="Mon jeu")** : On l’écrit une seule fois, au début. Elle ouvre la fenêtre du jeu et lui donne sa taille, avec ici un nom "Mon jeu".
- **pyxel.run(update, draw)** : C’est le bouton « Démarrer ». Pyxel répète en boucle, **30 fois par seconde** : update, puis draw, puis update, puis draw, et ainsi de suite, jusqu’à la fermeture de la fenêtre. On lui donne les noms des deux fonctions, **sans parenthèses**, car c’est Pyxel qui les appellera lui-même.

## Tester du code Pyxel

Voici un petit programme Pyxel pour tester le fonctionnement expliqué précédemment : 

```python
import pyxel

pyxel.init(128, 128, title="Afficher du texte")

def update():
    pass

def draw():
    pyxel.cls(0)
    pyxel.text(70, 70, "Bonjour !", 7)

pyxel.run(update, draw)
```

1. Lancer le script précédent sur Thonny, et répondre aux questions du rapport. 

<a href="./Rapport_1.odt" >Rapport.odt</a>

## Variable globale

Une **variable globale** en Python est une variable **définie en dehors de toute fonction ou classe**, ce qui lui confère **une portée étendue à l'ensemble du module ou du script**.  Elle peut être **lue par n'importe quelle fonction**, mais pour être modifiée depuis l'intérieur d'une fonction, elle doit être explicitement déclarée avec le mot-clé **global**. 

Voici un autre programme, à tester lui également :

```python
import pyxel

pyxel.init(128, 128, title="Chronomètre de 60 secondes")

compteur = 0
nombre = 0

def update():
    global compteur, nombre

    compteur += 1

    if compteur >= 30:
        compteur = 0
        nombre = ( nombre + 1 )  % 60

def draw():
    pyxel.cls(0)
    
    pyxel.text(pyxel.width//3, pyxel.height//3, "Chronometre:", 3)
    pyxel.text(pyxel.width//2, pyxel.height//2, str(nombre), 3)
    
pyxel.run(update, draw)

```

2. Expliquer le fonctionnement de ce code sur le rapport :
- Ce que vous voyez quand vous lancez le code (une fois la fenêtre ouverte);
- Quelle fonction permet l'affichage sur la fenêtre ?
- Quelle fonction permet le changement observé ;
- Que se passerait-il si on supprimer la variable globale ?

## A vous de jouer !

Comme premier code de ce projet, je vous demande de réaliser le même "jeu" qu'afficher au tableau (redemander au professeur si celui-ci a oublié d'afficher le jeu). Le programme terminé, il sera à ajouter à votre rapport et à envoyer avant le prochain cours de projet.

Pour cela vous aurez besoin de : 
- `pyxel.text(x,y,text,couleur)` ;
- `pyxel.line(x1,y1,x2,y2,couleur)` ; 
- `pyxel.rect(x,y,largeur,hauteur,couleur)` ;
- une ou plusieurs variables globales.