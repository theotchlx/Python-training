# Dans ce jeu, l'utilisateur choisi un nombre pour l'ordinateur.
# L'ordinateur doit trouver le nombre avec les indications de "plus petit" ou "plus grand".


from random import *

cpt = 1
d = 0
f = int(input('Limite max ?: '))
x = int(input("Le nombre, compris dans l'intervalle: "))

tr = False  # 'Trouvé'
while not tr:

    print("Ordi: Je vais donc chercher entre", d, "et", f)
    nb = randint(d, f)  # Nombre choisi par l'ordinateur (votre opposant, il doit trouver votre nombre)
    # L'ordinateur choisit nb au hasard.
    # La différence avec la v1 étant qu'ici c'est d et f (début et fin) qui sont modifiés en fonction
    # du résultat obtenu, et pas directement nb.

    print("Tour numéro", cpt)
    cpt += 1

    if nb == x:
        print("Ordi: J'ai trouvé! Le nombre est", x, "!!")
        tr = True

    elif nb < x:
        print("Ordi:", nb, "?")
        print("Vous: Trop petit!    [--> {}]".format(x))
        d = nb + 1

    else:
        print("Ordi:", nb, "?")
        print("Vous: Trop grand!    [--> {}]".format(x))
        f = nb - 1

