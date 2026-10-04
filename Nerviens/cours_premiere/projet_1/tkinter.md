---
title: Projet Python
---

# Tkinter : Interface Graphique

<link rel="stylesheet" href="../../assets/style.css" />


## L'idée générale de Tkinter

<a href="https://docs.python.org/3/library/tkinter.html" target="_blank">Tkinter</a> fonctionne autour de trois notions simples :

- Une fenêtre principale → l'application.
- Des widgets → les éléments graphiques : boutons, textes, zones de saisie…
- Des événements → ce qui se passe lorsqu'un utilisateur clique, écrit, sélectionne quelque chose, etc.  

Par exemple, on peut construire :

```shell
┌─────────────────────────────┐
│       Ma première app       │
│                             │
│  Ton prénom : [__________]  │
│                             │
│       [ Dire bonjour ]      │
│                             │
│  Bonjour Alice !            │
└─────────────────────────────┘
```

Le code associé pour cette fenêtre est alors : 

```python
import tkinter as tk

fenetre = tk.Tk()

# Création des éléments graphiques
texte = tk.Label(fenetre, text="Ton prénom :")
champ = tk.Entry(fenetre)
bouton = tk.Button(fenetre, text="Dire bonjour")

# Placement des éléments
texte.pack()
champ.pack()
bouton.pack()

# Lancement de l'application
fenetre.mainloop()
```

## Les éléments graphiques importants 

| Élément      | Rôle                               |
| ------------ | ---------------------------------- |
| `Tk()`       | crée la fenêtre                    |
| `Label`      | affiche du texte                   |
| `Button`     | crée un bouton                     |
| `Entry`      | zone de saisie                     |
| `Frame`      | permet de regrouper des éléments   |
| `pack()`     | place un élément                   |
| `grid()`     | place les éléments dans une grille |
| `mainloop()` | fait fonctionner l'interface       |

## Les événements

C'est probablement la notion la plus intéressante pour votre code, car **un bouton peut déclencher une fonction** !

Exemple :

```python
import tkinter as tk

def bonjour():
    print("Bonjour !")

fenetre = tk.Tk()

bouton = tk.Button(
    fenetre,
    text="Clique-moi",
    command=bonjour
)

bouton.pack()

fenetre.mainloop()
```

Ici :

```shell
command=bonjour
```
signifie : « Lorsque l'utilisateur clique sur le bouton, exécute la fonction bonjour. »  

**Attention à ne pas écrire :**

```shell
command=bonjour()
```

car cela exécuterait immédiatement la fonction lors de la création du bouton.

## Faire sa propre fenêtre

### Niveau 1 — Créer une fenêtre

```python
import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Mon application")

fenetre.mainloop()
```

### Niveau 2 — Afficher quelque chose

```python
label = tk.Label(
    fenetre,
    text="Bonjour !"
)

label.pack()
```

### Niveau 3 — Récupérer une saisie

```python
champ = tk.Entry(fenetre)
champ.pack()

texte = champ.get()
```

### Niveau 4 — réagir à un clic

```python
def action():
    print("Bouton cliqué !")

bouton = tk.Button(
    fenetre,
    text="Cliquer",
    command=action
)

bouton.pack()
```

### Niveau 5 — modifier l'interface

```python
label.config(text="Nouveau texte")
```