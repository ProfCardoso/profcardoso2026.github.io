import pyxel


# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Nuit du c0de")


x = 0
    
def update():
    global x
    x = (x + 1) % pyxel.width
    
def draw():
    pyxel.cls(0)
    pyxel.text(3, 5, "Le carre qui bouge sur la ligne", 9)
    pyxel.line(0, pyxel.height//2, pyxel.width, pyxel.height//2, 8)
    pyxel.rect(x, pyxel.height//2 - 4, 8, 8, 9)
    

pyxel.run(update, draw)


