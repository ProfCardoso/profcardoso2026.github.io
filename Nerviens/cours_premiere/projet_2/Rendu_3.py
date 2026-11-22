import pyxel

pyxel.init(128, 128, title='Murs')

joueurx = 10
joueury = 10
joueurw = 8
joueurh = 8

VITESSE = 2

murs = [(0, 128//4, 128//2, 8), (128//2, 2*(128//4), 128//2, 8), (0, 3*(128//4), 128//2, 8)]

arrivee = (128-8, 128-8, 8, 8)


def collision(ax, ay, aw, ah, bx, by, bw, bh):
    return ax < bx + bw and ax + aw > bx and ay < by + bh and ay + ah > by

def touche_un_mur(x, y, w, h, murs):
    for (mx, my, mw, mh) in murs:
        if collision(x, y, w, h, mx, my, mw, mh):
            return True
    return False

def touche_l_arrivee(x, y, w, h, arrivee):
    ax, ay, aw, ah = arrivee
    if collision(x, y, w, h, ax, ay, aw, ah):
        return True
    return False


def update():
    global joueurx,joueury,joueurw,joueurh
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    dx, dy = 0, 0
    if pyxel.btn(pyxel.KEY_LEFT):
        dx = -VITESSE
    if pyxel.btn(pyxel.KEY_RIGHT):
        dx = VITESSE
    if pyxel.btn(pyxel.KEY_UP):
        dy = -VITESSE
    if pyxel.btn(pyxel.KEY_DOWN):
        dy = VITESSE

    joueurx += dx
    joueury += dy


def draw():
    pyxel.cls(0)
    for (mx, my, mw, mh) in murs:
        pyxel.rect(mx, my, mw, mh, 5)
    
    ax, ay, aw, ah = arrivee
    pyxel.rect(ax, ay, aw, ah, 14)
    
    pyxel.rect(joueurx, joueury, joueurw, joueurh, 11)
    
    if touche_un_mur(joueurx, joueury, joueurw, joueurh, murs) :
        pyxel.text(5, 5, 'COLLISION', 7)
        
    if touche_l_arrivee(joueurx, joueury, joueurw, joueurh, arrivee) :
        pyxel.text(5, 5, 'FIN', 7)

pyxel.run(update, draw)
