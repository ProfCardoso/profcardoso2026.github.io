---
title: Initialisation à Python
---

<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>


<link rel="stylesheet" href="../../assets/style.css" />

# Les Tuples ( ou n-uplets )

Un tuple est une structure de données **ordonnée** et **immuable**.
Comme une liste, il peut contenir plusieurs valeurs, potentiellement de types différents :

```python
coord = (3, 7)
info = ("Léo", 17, "Première")
```

### Ordonnée

Les éléments sont rangés dans un ordre précis : l’index 0, puis 1, puis 2, etc ...

### Immuable

On ne peut pas modifier un tuple une fois qu'il est créé :

- impossible de changer un élément;

- impossible d’en ajouter;

- impossible de supprimer un élément.

➡️ **Remarques :** Cela en fait un type idéal pour représenter des données fixes, stables, comme des coordonnées, des dates, des couleurs RGB…

## Comment créer un tuple ?

Il existe deux manières pour créer un tuple :

- Avec des parenthèses ( qu'on privilégie pour plus de clarté ) 
```
t = (1, 2, 3)
```

- Sans parenthèses 
```
t = 1, 2, 3
```

### Bonus : Tuple à un seul élément

Il est aussi possible de créer des tuples à 1 seul éléments :

```python
t = (5,)    # tuple avec un seul élément

t = (5)     # ⚠️ Ce n’est PAS un tuple → simple entier

```

⚠️ Donc attention à la virgule !

##  Accéder aux éléments

Comme pour les listes, on obtient le contenu des tuples grâce aux indices :

```
t = ("lion", "zèbre", "girafe")

t[0]  # lion
t[2]  # girafe
t[-1] # girafe (dernier élément)
```

## Opérations possibles sur les tuples

Même si les tuples sont immuables, plusieurs opérations restent possibles :

### Longueur/ Taille 

Vous pouvez obtenir la taille d'un tuple avec la fonction `len`

```python
len(t)
```

### Concaténation

Il est possible de concaténer plusieurs tuples pour en créer un nouveau, concaténation de tous les tuples :

```python
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2   # (1, 2, 3, 4)
```

### Test d'appartenance

Comme pour les listes, vous pouvez savoir si un élément est présent dans un tuple avec le mot clé `in`.

```python
t = ("lion", "zèbre", "girafe")
print( "lion" in t )   #True
```


### Parcourir un tuple

Comme les tuples sont ordonnés, il est possible de les parcourir grâce au boucle :

```python
# Par indice
for i in range(len(t)):
    print(t[i])

# Ou par élément
for animal in t:
    print(animal)
```

### Fonctions utiles sur les tuples

Quelques fonctions sont utiles au tuple, en voici quelques unes :
```python
# Minimum / Maximum
min(t), max(t)  # (si éléments comparables)

# Somme des éléments du tuples
sum(t) # (si nombres)

# Position d'une valeur x dans le tuple
t.index(x) 

# Nombre d'occurences d'une valeur x dans le tuple
t.count(x) 

```

## Pour allez plus loin : le déballage (unpacking)

Très utile en Python ! On peut extraire les éléments d’un tuple directement dans des variables :

```python
coord = (4, 9)
x, y = coord
print(x,", ", y)  # 4, 9
```

Ou ignorer des valeurs :

```python
a, _, c = (1, 2, 3)
print(a, c) # 1 3

# ⚠️ Attention 
a, c = (1, 2, 3)    # Provoque une ValueError

```

## Applications 
>
> ### 🖋️ Application I : Un sacré zoo ... 
>
> On considère le tuple suivant :
>

```python

animaux = ("lion", "zèbre", "girafe", "éléphant")

```
>
> 1. Donner sur feuille :
> a) animaux[0]
> b) animaux[2]
> c) animaux[-1]
>
> 2. Peut-on exécuter : `animaux[1] = "tigre"` pour modifier la valeur `"zèbre"` en `"tigre"` ? Pourquoi ?
>
> 3. Écrire pour chacune des remarques suivantes leur expressions sous la forme d'un tuple différent.
>
> - Premier tuple : le tigre est carnivore, et son petit nom est Tigrou.
>
> - Deuxième tuple: les coordonnées du point de son enclos sont 7 et 12.
>
> - Troisème tuple: il pèse 220 kg.
>
> 4. Créer le tuple étant la concaténation des 3 tuples précédent.
>
> ### 🐍 Application II : Des pythons en Python ?
>
> Le zoo vous demande un coup de patte pour gérer leur parc informatique, et plus particulèrement leur vivarium.
>
> Le système de gestion des reptiles stocke toutes les informations de leur pensionnaire sous la forme de liste de tuples de cette forme :
>

```
reptiles = [
    ("iguane vert", "Iguana iguana", "femelle", "Léa", "herbivore"),
    ("gecko léopard", "Eublepharis macularius", "mâle", "Spot", "insectivore"),
    ("caméléon panthère", "Furcifer pardalis", "femelle", "Camy", "insectivore"),
    ("varan malais", "Varanus salvator", "mâle", "Rex", "carnivore"),
    ("tortue d'Hermann", "Testudo hermanni", "femelle", "Dora", "herbivore"),
    ("python royal", "Python regius", "mâle", "Bob", "carnivore"),
    ("boa constricteur", "Boa constrictor", "mâle", "Slinky", "carnivore"),
    ("couleuvre à collier", "Natrix natrix", "femelle", "Nati", "carnivore"),
    ("dragon barbu", "Pogona vitticeps", "mâle", "Spike", "omnivore"),
    ("cobra royal", "Ophiophagus hannah", "femelle", "Kali", "carnivore"),
    ("lézard ocellé", "Timon lepidus", "mâle", "Flash", "omnivore"),
    ("tortue léopard", "Stigmochelys pardalis", "femelle", "Perla", "herbivore")
]

```
> 
> 1. Le zoo veut créer des pancartes avec le nom latin et le surnom de chacun des animaux. Écris un programme qui déballe le nom latin et le surnom pour chacun des reptiles et les stockent dans une autre liste de tuple ne contenant que ces informations.
>
> Exemple :
>

```
reptile = [ ("cobra royal", "Ophiophagus hannah", "femelle", "Kali", "carnivore") ]

print(noms(reptile))    # [("Python regius","Bob")]
```
>
> 2. Oh non ! Une souris s'est enfuie dans la salle des serveurs et a court-circuité les ordinateurs, les animaux se sont sauvés et la liste de tuples a buggé :
>

```
reptiles_bugs = [

    "gecko léopard", "Eublepharis macularius", "mâle", "Spot", "insectivore",
    "cobra royal", "Ophiophagus hannah", "femelle", "Kali", "carnivore",
    "caméléon panthère", "Furcifer pardalis", "femelle", "Camy", "insectivore",
    "tortue d'Hermann", "Testudo hermanni", "femelle", "Dora", "herbivore",
    "couleuvre à collier", "Natrix natrix", "femelle", "Nati", "carnivore",
    "boa constricteur", "Boa constrictor", "mâle", "Slinky", "carnivore",
    "lézard ocellé", "Timon lepidus", "mâle", "Flash", "omnivore",
    "dragon barbu", "Pogona vitticeps", "mâle", "Spike", "omnivore",
    "tortue léopard", "Stigmochelys pardalis", "femelle", "Perla", "herbivore"
    "varan malais", "Varanus salvator", "mâle", "Rex", "carnivore",
    "iguane vert", "Iguana iguana", "femelle", "Léa","herbivore",
]

```
>
> Rattrapez les soucis en écrivant une fonction pour obtenir une liste de tuples, avec chaque tuples contenant : le nom, le nom latin, le sexe, le surnom et le régime alimentaire de tous les reptiles.
>
> 3. Pour les plus rapides : après comptage et recomptage, un des reptiles manque à l'appel ! Trouvez le fuyard en créant une fonction qui compare la liste initiale et celle créée par votre fonction précédente avant qu'il ne blesse un visiteur !
>