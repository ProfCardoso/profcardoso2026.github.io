---
title: Initialisation à Python
---

<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<link rel="stylesheet" href="../../assets/style.css" />

# Les listes en compréhensions

## Création d’une liste en compréhension

La syntaxe générale d’une liste en compréhension est la suivante :  

```python
L = [ expression for élément in séquence if condition ]
```
avec :  
- expression : l’expression à évaluer pour chaque élément de la séquence 
- élément : la variable qui prend la valeur de chaque élément de la séquence 
- séquence : séquence d’éléments sur laquelle la compréhension de la liste est appliqué
- condition : ( optionnelle ) une condition qui filtre les éléments de la séquence

On souhaite étudier la liste suivante :

```python
L = [n**3 for n in range(5)]
```

<details>
  <summary style="cursor: pointer; font-weight: bold;"><u>Quelle est la valeur de L ? 🤔</u></summary>
  <div style="margin-top: 10px;">
    <p>L est une liste contenant les 5 premières puissance de 3.</p>
    <code>L = [0, 1, 8, 27, 64] </code>
  </div>
</details>

  
---

> ## Applications
>
> ### 🖋️ Application I : Exercice sur feuille
>
> Voici plusieurs listes écritent en compréhension, écrire le résultat de ces listes :
> 1. liste_une = [ x for x in range(0,15,2) ]
>
> 2. liste_deux = [ 2**y for y in range(4) ]
>
> 3. liste_trois = [ z for z in ['N','S','I'] ]
> 
> ### 🐍 Application II : Quelques listes ...
>
> 1. Écrire une fonction qui créer une liste composée d'un nombre voulu de 0, donné en paramètre. Cette liste devra avoir deux versions, une créée par liste par itération, une autre créée par compréhension.
>
> 2. Écrire une fonction `decompte(départ,fin)` qui créer une liste effectuant un décompte de 1 en 1, avec le point de départ et le point d'arrivée donnés en paramètre. Cette liste devra avoir deux versions, une créée **par itération**, une autre créée **en compréhension**.
>
> Exemple :
>
```
>>> decompte(10,0):
[10,9,8,7,6,5,4,3,2,1,0]
```
>
> **Bonus**: écrire une version du décompte qui changera tous les nombres pair en chaîne de caractère

___

# Liste de liste ( ou tableau de tableau )

Comme vous avez pu le constater, une liste peut contenir plusieurs type de données, mais elle peut aussi contenir d’autre liste, on appelle ça des **listes de listes**, ou encore des **matrices** ( souvent utilisé en mathématique ).

Voici un exemple de liste de listes, testez la:

```python
L = [0,0,0,0]
M = [L,L,L,L]
print(M)
```

## Quelques notions 

Voici une autre matrice :

```
m = [ [1,4,2], 
      [2,5,3], 
      [6,7,3] ]
```

Cette matrice m est de **largeur** de 3 et de **hauteur** 3, et est composée d’entiers. Elle a 3 **lignes** et 3 **colonnes**, organisé comme ceci :  
En partant de haut en bas :

- Première ligne : 1,4,2
- Deuxième ligne : 2,5,3
- Troisième ligne : 6,7,3

En partant de gauche à droite :

- Première colonne : 1,2,6
- Deuxième colonne : 4,5,7
- Troisième colonne : 2,3,3

Si l’on veut accéder à un élément particulier de cette matrice, on utilisera la notation des **« doubles crochets »** :  

```python
m [ indice ligne ] [ indice colonne ]
```

De manière identique, les lignes et colonnes commencent par l’indice 0.

> ## Applications
>
> ### 🖋️ Application I : 
>
> Voici une matrice :
>
```python
li = [["a", "b", "c", "d"],
      [1, 2, 3, 4],
      ["I", "II", "III", "IV"]]
```
>
> 1) Quel est le contenu de la variable définie par : `v1 = li[0]` ?
>
> 2) Quel est le contenu de la variable définie par : `v2 = v1[1]` ?
>
> 3) Quel est le contenu de la variable définie par : `v3 = li[0][1]` ?
>
> 4) Quel est le contenu de la variable définie par : `v4 = li[1][0]` ?
>
> ### 🖋️ Application II : Modification de liste de listes
>
> On considère la liste de liste suivante : 
```python
li = [[0, 0, 0], [0, 0, 0]]
```
>
> Écrire les lignes de code qui permettent de modifier un à un les éléments de cette liste pour qu'elle devienne : `[[10, 20, 30], [100, 200, 300]]`
> 
> ### 🐍 Application III : Les jours de la semaine, le retour
>
> On considère la liste de listes suivante :
> 
```python
li = [["lundi", "monday"],
      ["mardi", "tuesday"],
      ["mercredi", "wednesday"],
      ["jeudi", "thursday"],
      ["vendredi", "friday"],
      ["samedi", "saturday"],
      ["dimanche", "sunday"]]
```
>
> Proposer un programme qui permet d'obtenir l'affichage suivant :
>
```
lundi -> monday
mardi -> tuesday
...
```
>
> ### Application IV : Damier
>
> Vous souhaitez écrire une fonction pour créer des damiers pour plusieurs jeux de plateau, comme les échecs ou les dames. 
>
> Ecrire la fonction `damiers(x,y)`, qui prend le nombre de ligne x et de colonne y du damier, et qui renvoi une liste de liste comprenant un enchainement de cases noires (0 ou "N") et blanches (1 ou "B").
>
> Exemple :
>
```python
>>> damiers(5,5)
[[0,1,0,1,0],
 [1,0,1,0,1],
 [0,1,0,1,0],
 [1,0,1,0,1],
 [0,1,0,1,0]]
```
>
> Vous pourrez tester l'affichage de votre damier grâce à cette bibliothèque python, nommée matplotlib :

```python
import matplotlib.pyplot as plt


def damiers(x,y):
    pass                               # A remplacer par votre code

damier = damiers(5,5)   		           # Création du damier

plt.imshow(damier, cmap="gray")        # 0 = noir, 1 = blanc
plt.axis("off")                        # cache les axes
plt.show()
```

>
> ### Application V : Le labyrinthe 
>
> On considère la grille de labyrinthe suivante où les 1 correspondent à des murs et les 0 à des passages.
>
```python
labyrinthe = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 1, 1, 0, 1, 1, 1, 0, 1],
              [1, 0, 0, 0, 1, 0, 0, 0, 1],
              [1, 0, 1, 1, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1, 1, 1, 1]]
```
> En utilisant le caractère `"█"` et le caractère `" "`, proposer un script qui affiche proprement le labyrinthe :
>
```
██████████████████
                ██
██████  ██████  ██
██      ██      ██
██  ██████████████
██                
██████████████████
```
>
> Remarque : Ce genre de labyrinthe pourrait vous être utile pour modéliser celui du projet pac man ... 
>
> **Bonus :**  
> a/ Voici le même labyrinthe mais avec un point de départ et d'arrivé : 
>
```python
labyrinthe = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
              ["D", 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 1, 1, 0, 1, 1, 1, 0, 1],
              [1, 0, 0, 0, 1, 0, 0, 0, 1],
              [1, 0, 1, 1, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, "A"],
              [1, 1, 1, 1, 1, 1, 1, 1, 1]]
```
> En utilisant le caractère `"D"` et le caractère `"A"`, proposer un script qui affiche proprement le labyrinthe :
>
```
██████████████████
D               ██
██████  ██████  ██
██      ██      ██
██  ██████████████
██               A
██████████████████
```
>
> b/ Ajouter un pion `"P"`, dont le but est d'avancer de la case départ `"D"` à la case arrivé `"A"`. Le pion ne pourra pas marcher sur les murs ( case `"█"` ). Pour ce faire, vous demanderez à l'utilisateur une direction (haut, bas, gauche, droite) tant que le pion n'est pas sorti du labyrinthe.
>
