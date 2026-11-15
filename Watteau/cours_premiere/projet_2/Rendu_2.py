import pyxel

pyxel.init(128, 128, title="Rendu 2")

x = 45
y = 55
couleur = 7


def update():
    global x, y, couleur
    if pyxel.btn(pyxel.KEY_LEFT):           # btn : vrai tant que la touche est maintenue
        x = x - 1
    if pyxel.btn(pyxel.KEY_RIGHT):
        x = x + 1
    if pyxel.btn(pyxel.KEY_UP):
        y = y - 1
    if pyxel.btn(pyxel.KEY_DOWN):
        y = y + 1
    x = max(5, min(pyxel.width, x))                 # on empêche le texte de sortir de la fenêtre
    y = max(5, min(pyxel.height, y))

    if y > pyxel.height//2 - 3:         # Changement de couleur au milieu de l'écran moins la moitié de la taille du carré 
        couleur = 0
    elif y < pyxel.height//2 - 3 :         
        couleur = 8

def draw():
    pyxel.cls(0) # Fond noir

    pyxel.rect(0, pyxel.height//2, pyxel.width, pyxel.height//2, 8) # Rectangle pour la moitié basse de l'écran
    pyxel.rect(x, y, 5,5, couleur)


pyxel.run(update, draw)



