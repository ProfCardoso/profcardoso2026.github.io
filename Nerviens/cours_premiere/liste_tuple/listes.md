---
title: Initialisation à Python
---

<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<link rel="stylesheet" href="../../assets/style.css" />

# Les listes

Dans nos révisions du langage Python, nous avions vu certains types de variables simples: `int` (entiers), `float` (nombres à virgule flottante), `bool` (booléen) et `str` (chaîne de caractères). Nous allons maintenant voir des **types construits** qui sont des collections d’objets de type simple assemblés dans ce que l’on appelle une structure de données.  

Le premier exemple de type construit s'appelle le tableau. En Python, le terme “liste” est souvent utilisé pour désigner un tableau, d'ailleurs ce dernier a comme type `list`.  
Un tableau est une structure de données qui permet de stocker plusieurs valeurs (nombres, chaînes, booléens, etc.) dans une seule variable, et d’y accéder grâce à leur position (indice).

Les listes sont des **séquences** : elles sont ordonnées et itérables.  

Les listes sont **mutables** : elles peuvent être modifiées après leur création.  

Les listes sont **hétérogènes** : elles peuvent contenir tous les types d'objets.  

## Généralités
### Création d'une liste
Les listes s'écrivent avec des crochets [ ]. Les éléments sont séparés par des virgules.

*Exemple :*

```python
liste1 = [12, 8, -9, 9.5, 3]
liste2 = ['a', 'b', 'c', 'd']
liste3 = []  #Une liste peut être vide
liste4 = list()  #Une liste peut être vide
```

### Longueur d'une liste

`len(liste)` :	Renvoie le nombre d'élément dans la liste, c'est-à-dire la longueur de la liste.  

### Récupération d'un élément d'une liste

`liste[i]` avec i ≥ 0 :	Renvoie le ième élément de liste en partant du début, le premier élément ayant l'indice 0.  
`liste[i]` avec i < 0 :	Renvoie le ième élément de liste en partant de la fin, le dernier élément ayant l'indice -1.

*Exemple :*

```python
liste = ['a', 'b', 'c', 'd']
elt_A = liste[1]  #La variable elt_A contient maintenant 'b'
elt_B = liste[-2]  #La variable elt_B contient 'c'
```

### Ajout d'un élément à une liste

**• Ajout d'un élément à l'aide de la méthode `append(...)`**  

`liste.append(x)` :  Modifie `liste` en ajoutant l’élément x après le dernier élément.

**• Remarque : ajout d'un élément par concaténation**

Il est possible d'utiliser l'opérateur + entre deux listes :

`l1 + l2` : Renvoie une **nouvelle** liste qui contient les éléments de l1 avec à la suite ceux de l2.

Avec cet opérateur, on ajoute un élément à la liste avec le code suivant :

`liste = liste + [x]` : Modifie liste en ajoutant l’élément x après le dernier élément.

> #### 🖋️ Application I : Les jours de la semaine
>
> 1. Écrire la ligne de code qui permet de créer la variable `jours_semaine`, une liste contenant les jours de la semaine sans le dimanche.
>
> 2. Compléter avec la ligne de code qui permet de récupérer et stocker le premier élément de cette liste dans la variable `premier_jour`. Ajouter la ligne de code qui permet d'afficher le contenu de la variable `premier_jour`.
>
> 3. Compléter avec la ligne de code qui permet d'ajouter "dimanche" à la liste `jours_semaine`.
>
> 4. Compléter avec la ligne de code qui permet de remplacer l'élément **"mardi"** par **"tuesday"**.
>
> 5. Compléter avec la ligne de code qui affiche le nombre d'élément de la liste `jours_semaine`.
>
> 6. Compléter avec la ligne de code qui permet d'afficher le 3ème jour de la semaine, c'est-à-dire mercredi.
>

##  Parcours d'une liste avec for ... in ...

### Utilisation de for pour parcourir les éléments

*Exemple : affichage des 10 premiers nombres entiers*

```python
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for elt in liste:   #elt est une variable qui prend successivement les valeurs de la liste
    print(elt, "^2"," = ", elt**2, sep="")
```

### Utilisation de for pour parcourir les indices

*Exemple : affichage d'une lettre sur deux de l'alphabet*

```python
liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's']
for i in range(len(liste)):   #i est une variable qui prend successivement les valeurs des positions
    if i % 2 == 0:
        print(liste[i], end='')
```

### Analyse de code : Parcourir une liste

> #### 🖋️ Application II 
>
> A l'aide d'un tableau, expliciter le déroulement pas à pas du code suivant :
>
```python
liste = [1, 2, 3, 4, 5]
for i in range(len(liste)):
    elt = liste[i]
    print(str(elt) + "² = " + str(elt**2))
```
>
> A l'aide d'un tableau, expliciter le déroulement pas à pas du code suivant :
>
```python
liste = [1, 2, 3, 4, 5]
for elt in liste:
    print(str(elt) + "² = " + str(elt**2))
```
>
>On considère le code suivant :
>
```python
liste = ['a', 'b', 'c', 'd', 'e']
for i in range(len(liste)):
    print("Indice " + str(i) + " : " + str(liste[i]))
```
>
>a) A l'aide d'un tableau, expliciter le déroulement pas à pas du code suivant :
>
>b) Justifier que ce programme ne peut pas être codé avec un parcours de la liste en valeurs.
>

## Modification d'une liste

### Remplacement d'une valeur par une nouvelle valeur

`liste[i] = x` avec i≥0 : Modifie `liste` en remplaçant l'élément d'indice i par x, le premier élément ayant l'indice 0.  
`liste[i] = x` avec i<0 : Modifie `liste` en remplaçant l'élément d'indice i par x en partant de la fin de la liste, le dernier élément ayant l'indice -1.  

*Exemple :*

```python
liste = [12, 8, -9, 9.5, 3]
liste[1] = 'a'  #La variable liste est maintenant égale à [12, 'a', -9, 9.5, 3]
```



### Suppression d'un élément d'une liste

**• Suppression d'un élément à l'aide de la méthode pop(...)**

`liste.pop()` :	Modifie liste en supprimant le dernier élément et renvoie cet élément.  
`liste.pop(i)` : Modifie liste en supprimant le ième élément et renvoie cet élément.

**• Suppression à l'aide l'instruction del**

*Exemple :*

``` python
liste = ['a', 'b', 'c', 'd', 'e', 'f']
del liste[1] #La variable liste est maintenant égale à ['a', 'c', 'd', 'e', 'f']
```

**• Suppression d'un élément d'une liste**

`liste.remove(elt)` : Modifie liste en supprimant l'élément elt.  

Attention, si l'élément x n'est pas dans liste, cette fonction lève une erreur.  

### Condition d'appartenance d'un élément à une liste

Les conditions (utilisable avec `if` ou `while`) d'appartenance et de non-appartenance d'un objet à une liste sont : `in` et `not in`.

*Exemple :*

```python
liste = ['a', 'e', 'i', 'o', 'u', 'y']
caract = 'b'
if caract in liste:
    print(caract, 'est une voyelle')
if caract not in liste:
    print(caract, 'n'est pas une voyelle')
```

### Applications

> #### 🐍 Application III : Faire soi même
>
> 1) Créer une fonction `ajout_fin_element_liste(liste,ele)` avec 2 paramètres : une liste `liste` , à qui on va ajouter l'élément `ele` à la fin de la liste. 
>
> Exemple :
>
``` 
>>> ajout_fin_element_liste([1,2,3,4],5)
[1,2,3,4,5]
```

>
> 2) Créer une fonction `ajout_debut_element_liste(liste,ele)` avec 2 paramètres : une liste `liste` , à qui on va ajouter l'élément `ele` au début de la liste. 
>
> Exemple :
>
``` 
>>> ajout_debut_element_liste([1,2,3,4],0)
[0,1,2,3,4]
```

>
> 3) Créer une fonction `reduction_de_liste(liste, taille)` avec 2 paramètres : une liste `liste` , à qui on va supprimer un élément à la fois jusqu'à obtenir une liste de taille `taille`. Chacun des éléments de la liste `liste` devra être affiché. Si la taille de la liste est plus petite que taille, on ne fera rien. On **renverra la liste** à la fin de la réduction.
>
> Exemple :
>
``` 
>>> reduction_de_liste([1,2,3,4,5], 3)
5
4
[1,2,3]
```
>

### Autres opérations sur les listes

#### Les opérateurs + et * appliqués aux listes

`l1 + l2` : Renvoie une liste qui contient les éléments de l1 avec à la suite ceux de l2.  
`l1 * n ou n * l1` : Renvoie une liste qui contient de façon répétée n fois les éléments de l1.  

*Exemple :*

```python
liste1 = [12, 8, -9]
liste2 = [3, 5]
liste = liste1 + liste2  # liste3 contient [12, 8, -9, 3, 5]
```

**Remarque :** l'opérateur + peut être utilisé pour ajouter un élément à une liste :

```python
liste = [12, 8, -9]
elt = 5
liste = liste + [elt]  # liste3 contient [12, 8, -9, 5]
```

#### La fonction list

La fonction `list(itérable)` transforme un itérable en liste.

*Exemple :*

```python
# Tester ces lignes dans la console python

# Liste des 100 premiers nombres
liste_range = list(range(1,101))

# Transformation d'une chaine de caractères en liste
liste_chaine_carac = list("abcdefghijklmnopqrstuvwxyz")
```

#### Utilisation de méthodes prédéfinies

**• Les méthodes de recherche dans les listes**

`liste.index(x)` : Renvoie l'indice de la première occurrence de x dans liste ou une erreur si x n'est pas dans liste.  
`liste.count(x)` : Renvoie le nombre d'occurrence de x dans liste.

**• La méthode de tri d'une liste**

`liste.sort()` : Modifie liste en triant l'ordre de ses éléments s'ils sont du même type.

#### Quelques fonctions du module random pour les listes

Pour pouvoir utiliser les fonctions suivantes, le module random doit être importé :

```python
from random import *
liste = [0,1,2,3,4,5,6,7,8,9]

choix = choice(liste)	# Renvoie un élément de liste pris aléatoirement.
print(choix)

n = 3
echantillon = sample(liste, n)	# Renvoie une liste contenant n éléments de liste pris aléatoirement.
print(echantillon)

print("liste avant mélange: ", liste)
shuffle(liste)	# Mélange les éléments de liste.
print("liste après: ", liste)
```

### Applications Bonus :

> #### 🐍 Application IV : Pour les plus rapides
>
> On peut considérer les entiers binaires comme des listes de taille 8 composées d'entier
>
> Exemple :
>
``` 
entier_binaire = [1,1,0,1,0,0,1,1]
```
>
> Écrire une fonction `bin_to_dec(binaire:list[int])` qui prendra une liste d'entier en paramètre et qui retrouvera l'entier en base 10 associé.

> Exemple :
>
``` 
>>> bin_to_dec([1,0,0,1,1])
19
```
