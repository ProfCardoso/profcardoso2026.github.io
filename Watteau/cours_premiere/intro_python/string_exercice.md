---
title: Initialisation à Python
---

<link rel="stylesheet" href="../../assets/style.css" />


# Applications 

## Chaîne de caractère

### Application I : Ascii art

Créer une variable qui contiennent l'ascii-art suivants :

```ascii
       ^
       |
       +
       |
       |
       |
       |
       |
       A
      ===                ________
     /EEE\               |______|
    //EEE\\              |*(  )*|
___//_____\\_____________|O|  |O|_______
```

### Application II

Compléter le code ci-dessous pour créer la variable phrase uniquement à partir des variables disponibles.

```python
mot1 = "Bonjour"
mot2 = "Hector"
mot3 = "!"
mot4 = " "
phrase = ...  # Phrase doit contenir "Bonjour Hector !"
```
### Application III

Compléter le code ci-dessous pour créer la variable phrase à partir des variables qui lui précèdent.

```python
prénom = "Hector"
age = 16
phrase = ...  # "Bonjour. Je m'appelle Hector et j'ai 16 ans !"
```

### Application IV

1) Indiquer comment on obtient le nombre de caractères d'une chaine de caractères.

2) Écrire une fonction qui prend deux chaines en paramètre et renvoie la chaine dont la longueur est la plus grande.

3) Compléter avec le programme principal qui permet de créer deux variables contenant des chaines et de tester la fonction avec ces deux variables.

### Applications V

Sans tester le code, indiquer ce que contiennent les variables lettre1 et lettre2 à la fin de l'exécution.

```python
alphabet = "abcdefghijklmnopqrstuvwxyz"
lettre1 = alphabet[0]
lettre2 = alphabet[-1]
```

### Application VI

On dispose de la variable alphabet.

```python
alphabet = "abcdefghijklmnopqrstuvwxyz"
```
Écrire le code qui demande un nombre entre 1 et 26 à l'utilisateur et qui donne par la suite la lettre correspondante de l'alphabet.

Ainsi la lettre 1 doit renvoyer `a` et la lettre 26 doit renvoyer `z`.

### Application VII

Sans tester le code, indiquer le contenu des différentes variables presence_ à la fin de l'exécution.

```python
demi_alphabet = "abcdefghijklm"
presence1 = 'a' in demi_alphabet
presence2 = 'o' in demi_alphabet
presence3 = 'ab' in demi_alphabet
chaine = 'ab'
presence4 = chaine in demi_alphabet
presence5 = 'mn' in demi_alphabet
```

## Print

### Application I

D'abord sur feuille, puis sur l'ordinateur : Écrire un programme qui, à partir de trois variables contenant chacune un prénom :

- écrit les trois prénoms sur trois lignes différentes en utilisant trois print(),
- écrit les trois prénoms sur la même ligne en utilisant qu'un seul print(),
- écrit les trois prénoms sur la même ligne en utilisant trois print(),
- écrit les trois prénoms sur trois lignes différentes en utilisant qu'un seul print().

## Input

### Application I

1) Écrire l'algorithme qui demande une température t et qui affiche une chaine de caractère correspond à l'état de l'eau à cette température c'est-à-dire "SOLIDE", "LIQUIDE" ou "GAZEUX". On préféra une phrase comme par exemple : "A -5 °C, l'eau est SOLIDE.".

On considérera que :

- Si la température est strictement négative alors l'eau est à l'état solide.
- Si la température est entre 0 et 100 (compris) l'eau est à l'état liquide.
- Si la température est strictement supérieure à 100. 

Attention : la valeur à donner par l'utilisateur doit être en int.


## Si vous avez tout fini : Autres actions possibles sur les chaines


Voici un extrait du roman "La disparition" de George Perec :

```
Anton Voyl n'arrivait pas à dormir. Il alluma. Son Jaz marquait minuit vingt. Il poussa un profond soupir, s'assit dans son lit, s'appuyant sur son polochon. Il prit un roman, il l'ouvrit, il lut; mais il n'y saisissait qu'un imbroglio confus, il butait à tout instant sur un mot dont il ignorait la signification.

Il abandonna son roman sur son lit. Il alla à son lavabo ; il mouilla un gant qu'il passa sur son front, sur son cou.

Son pouls battait trop fort. Il avait chaud. Il ouvrit son vasistas, scruta la nuit. Il faisait doux. Un bruit indistinct montait du faubourg. Un carillon, plus lourd qu'un glas, plus sourd qu'un tocsin, plus profond qu'un bourdon, non loin, sonna trois coups. Du canal Saint-Martin, un clapotis plaintif signalait un chaland qui passait.

Sur l'abattant du vasistas, un animal au thorax indigo, à l'aiguillon safran, ni un cafard, ni un charançon, mais plutôt un artison, s'avançait, traînant un brin d'alfa. Il s'approcha, voulant l'aplatir d'un coup vif, mais l'animal prit son vol, disparaissant dans la nuit avant qu'il ait pu l'assaillir.
```

Écrire un programme qui permet de déterminer le nombre de `e` dans cet extrait.