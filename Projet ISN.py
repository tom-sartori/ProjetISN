from tkinter import *
from random import *


### EVENEMENTS ###

def haut(event):
    global x, y, v, passage, pas, AffichageIng, AffichagePri, yFut, xFut, case, s, PersoDro, PersoDos, PersoGau, PersoHaut, ImPersoHaut 

    if AffichageIng or AffichagePri:  # lorsqu'on est dans le menu en jeu
        return ()

    xFut = x
    yFut = y - v  # yFut est le coordonnée en y que le perso devrait avoir apres son déplacement
    CasePerso()

    if case in s:  # si la futur case du perso est dans la liste des cases bloqués alors on sort de la fonction pour que le perso n'avance pas
        return ()

    if x == 585 and y == 300:  # on test si le perso est sur l'avant derniere case verticale lorsqu'il appuie pour avancer mais avant que les coord aient avancés
        passage = 1

    if passage == 1 and x == 585 and y == 228 and pas > 0:  # si passage est à 1, que le perso est sur la derniere case et qu'on appuie pour monter alors on remet au depart pour la salle d'apres
        InitPerso()
    else:
        if y - v > 188 and pas > 0:  # tant que le perso ne sort pas du cadre en hauteur, on le fait avancer case par case (variable v pour la taille de l'avancement)
            y = y - v

            try:  # on essaie d'enlever toutes les images orientés et seulement celle du dernier déplacement est possible. on devrait donc avoir NameError pour les autres images
                can.delete(PersoDos)
            except NameError:  # on excepte NameError et ainsi le programme de fait pas d'erreur
                rien = 0

            try:
                can.delete(PersoGau)
            except NameError:
                rien = 0

            try:
                can.delete(PersoDro)
            except NameError:
                rien = 0

            ImPersoHaut = PhotoImage(file ='Images/haut.gif')
            PersoHaut = can.create_image(x, y, image=ImPersoHaut)
            can.coords(PersoHaut, x, y)
            
            print("haut  ", "x= ", x, "y = ", y)
            DecomptPas()

    if pas == 0:
        MenuIng()



def bas(event):
    global x, y, v, pas, AffichageIng, AffichagePri, xFut, yFut, case, s, PersoDro, PersoDos, ImPersoDos, PersoGau, PersoHaut

    if AffichageIng or AffichagePri:
        return ()

    xFut = x
    yFut = y + v
    CasePerso()
  
    if case in s:
        return ()

    if y + v < 709 and pas > 0:  # la bordure inférieure du cadre est à 709px en y
        y = y + v


        try:    # on essaie d'enlever toutes les images orientés et seulement celle du dernier déplacement est possible. on devrait donc avoir NameError pour les autres images
            can.delete(PersoHaut)            
        except NameError:  # on excepte NameError et ainsi le programme de fait pas d'erreur
            rien = 0

        try:
            can.delete(PersoGau)
        except NameError:
            rien = 0

        try:
            can.delete(PersoDro)
        except NameError:
            rien = 0

        ImPersoDos = PhotoImage(file ='Images/PersoDos.gif')
        PersoDos = can.create_image(x, y, image=ImPersoDos)
        can.coords(PersoDos, x, y)
        
        print("bas   ", "x= ", x, "y = ", y)
        DecomptPas()

    if pas == 0:
        MenuIng()



def gauche(event):
    global x, y, v, passage, pas, AffichageIng, AffichagePri, xFut, yFut, case, s, PersoDro, PersoDos, PersoGau, ImPersoGau, PersoHaut

    if AffichageIng or AffichagePri:
        return ()

    xFut = x - v
    yFut = y
    CasePerso()

    if case in s:
        return ()

    if x == 657 and y == 228:  # lorsque le perso est sur l'avant derniere case à droite et qu'il veut aller a gauche donc sur la derniere case alors passage=1
        passage = 1

    if x - v > 117 and pas > 0:  # la bordure gauche du cadre est à 117px en x
        x = x - v


        try:    # on essaie d'enlever toutes les images orientés et seulement celle du dernier déplacement est possible. on devrait donc avoir NameError pour les autres images
            can.delete(PersoDos)            
        except NameError:  # on excepte NameError et ainsi le programme de fait pas d'erreur
            rien = 0
    
        try:
            can.delete(PersoHaut)
        except NameError:
            rien = 0

        try:
            can.delete(PersoDro)
        except NameError:
            rien = 0

        ImPersoGau = PhotoImage(file ='Images/gauche.gif')
        PersoGau = can.create_image(x, y, image=ImPersoGau)
        can.coords(PersoGau, x, y)
        
        print("gauche", "x= ", x, "y = ", y)
        DecomptPas()

    if pas == 0:
        MenuIng()



def droite(event):
    global x, y, v, passage, pas, AffichageIng, AffichagePri, xFut, yFut, case, s, PersoDro, ImPersoDro, PersoDos, PersoGau, PersoHaut

    if AffichageIng or AffichagePri:
        return ()

    xFut = x + v
    yFut = y
    CasePerso()

    if case in s:
        return ()

    if x == 513 and y == 228:  # lorsque le perso est sur l'avant derniere case à gauche et qu'il veut aller a droite donc sur la derniere case alors passage=1
        passage = 1

    if x + v < 1063 and pas > 0:  # la bordure droite du cadre est à 1063px en x
        x = x + v

        try:    # on essaie d'enlever toutes les images orientés et seulement celle du dernier déplacement est possible. on devrait donc avoir NameError pour les autres images
            can.delete(PersoDos)            
        except NameError:  # on excepte NameError et ainsi le programme de fait pas d'erreur
            rien = 0
            
        try:
            can.delete(PersoHaut)
        except NameError:
            rien = 0

        try:
            can.delete(PersoGau)
        except NameError:
            rien = 0
            
        ImPersoDro = PhotoImage(file ='Images/droite.gif')
        PersoDro = can.create_image(x, y, image=ImPersoDro)
        can.coords(PersoDro, x, y)
        
        print("droite", "x= ", x, "y = ", y)
        DecomptPas()

    if pas == 0:
        MenuIng()



def echap(event):
    global salle, AffichageIng, BReturnMenu, BReturnC, pas, BQuitter

    if pas == 0:  # lorsqu'on est a 0 pas, le menu en jeu est deja affiché ; il ne faut donc pas l'enlever en appuyant sur echap
        return ()

    if salle != 0:

        if not AffichageIng:
            AffichageIng = True
            MenuIng()

        else:
            BReturnMenu.destroy()
            BReturnC.destroy()
            BQuitter.destroy()
            AffichageIng = False



### MENUS ###

def MenuPrincipal():
    global BReturnMenu, BReturnC, salle, AffichageIng, AffichagePri, Fond1, PersoDos, NbPas, ImMonstre1, Monstre1, BJouer, BChrono, BHard, BQuitter, MenuP, NbSalle
    print("Menu Principal")

    salle = 0
    AffichagePri = True  # lorsque AffichagePri est vrai, cela signifie qu'on est dans le menu principal

    if AffichageIng:
        BReturnMenu.destroy()  # on enleve les boutons du menu en jeu
        BReturnC.destroy()
        BQuitter.destroy()


        AffichageIng = False  # AffichageIng est faux car on est plus dans le menu en jeu

        can.delete(Fond1)  # on enleve les images affichés lorsqu'on joue (fond, perso, compteurs)
        can.delete(PersoDos)
        NbPas.place_forget()
        NbSalle.place_forget()

        try:  # on essaie d'enlever le monstre et si il est présent on l'enleve. si il n'est pas encore present, on devrait avoir une erreur NameError
            can.delete(Monstre1)
        except NameError:  # on excepte NameError et ainsi le programme de fait pas d'erreur. en suite, comme le monstre n'est pas initialisé on a pas besoin de le suprimer
            rien = 0

    MenuP = can.create_image(587, 389, image=ImMenuPrinc)

    BJouer = Button(fen, command=ModeNormal, bd=0, image=ImgJouer)  # bouton du menu principal
    BJouer.place(x=125, y=100)

    BChrono = Button(fen, command=ModeChrono, bd=0, image=ImgChrono)  # bouton du menu principal
    BChrono.place(x=730, y=100)

    BHard = Button(fen, command=ModeHard, bd=0, image=ImgHard)  # bouton du menu principal
    BHard.place(x=430, y=360)

    BQuitter = Button(fen, command=quitter, bd=0, image=ImgQuitter)
    BQuitter.place(x=430, y=600)



def MenuIng():  # on affiche un menu permettant de retourner au dernier checkpoint ou au menu principal (MenuIng = menu in game)
    global BReturnMenu, BReturnC, AffichageIng, BReturnMenu, BReturnC, BQuitter

    AffichageIng = True

    BReturnMenu = Button(fen, command=MenuPrincipal, bd=0, image=ImgMP)  # bouton du menu principal
    BReturnMenu.place(x=262, y=278)

    BReturnC = Button(fen, command=checkpoint, bd=0, image=ImgChekpoint)  # bouton du checkpoint
    BReturnC.place(x=622, y=278)

    BQuitter = Button(fen, command=quitter, bd=0, image=ImgQuitter)
    BQuitter.place(x=430, y=550)



### MODES ###

def ModeNormal():  # mode classique
    global salle, Fond1, AffichagePri, NbPas, MenuP, NbSalle, MHard
    print("mode normal")

    AffichagePri = False
    MHard = False

    can.pack()

    BJouer.destroy()  # permet d'enlever les boutons du menu principal lorsqu'on arrive dans le jeu
    BChrono.destroy()
    BHard.destroy()
    BQuitter.destroy()
    can.delete(MenuP)

    Fond1 = can.create_image(587, 389, image=ImFondIng1)

    pas = 123  # nombre aléatoire utilisé juste pour l'initialisation du label
    NbPas = Label(fen, text=pas, bg="#524f53", padx=5, pady=5)  # affichage du décompte des pas
    NbPas.place(x=205, y=40)

    NbSalle = Label(fen, text=salle, bg="#524f53", padx=5,pady=5)  # on affiche la salle dans laquelle le personnage se trouve
    NbSalle.place(x=463, y=40)

    InitPerso()



def ModeChrono():  # mode avec compteur de temps

    print("mode chrono en développement")

    BJouer.destroy()  # peremet d'enlever les boutons du menu principal lorsqu'on arrive dans le jeu
    BChrono.destroy()
    BHard.destroy()



def ModeHard():  # mode hard sans vies
    global salle, Fond1, AffichagePri, NbPas, MenuP, NbSalle, MHard
    print("mode hard")
    
    AffichagePri = False

    MHard = True
    can.pack()

    BJouer.destroy()  # permet d'enlever les boutons du menu principal lorsqu'on arrive dans le jeu
    BChrono.destroy()
    BHard.destroy()
    BQuitter.destroy()
    can.delete(MenuP)

    Fond1 = can.create_image(587, 389, image=ImFondIng1)

    pas = 123  # nombre aléatoire utilisé juste pour l'initialisation du label
    NbPas = Label(fen, text=pas, bg="#524f53", padx=5, pady=5)  # affichage du décompte des pas
    NbPas.place(x=205, y=40)

    NbSalle = Label(fen, text=salle, bg="#524f53", padx=5,pady=5)  # on affiche la salle dans laquelle le personnage se trouve
    NbSalle.place(x=463, y=40)

    InitPerso()



def quitter():
    print("quitter")
    fen.destroy()



### ###

def InitPerso():  # Initialisation du personnage aux coordonnées d'entrée dans la salle
    global x, y, v, PersoDos, ImPersoDos, passage, pas, salle, xIA, yIA, ImMonstre1, Monstre1, Fond1, NbSalle
    print("Initialisation")

    x = 585  # x et y sont les coordonnées de départ
    y = 660
    v = 72  # v est la taille d'une case qui définit donc l'avancement a chaque pat

    passage = 0
    pas = 22
    DecomptPas()

    can.delete(Fond1)
    Fond1 = can.create_image(587, 389, image=ImFondIng1)

    salle = salle + 1
    print("salle = ", salle)
    NbSalle.config(text=salle)  # rafraichie le nombre de la salle

    InitBlocage()   #on affiche le blocage avant le personnage pour pas qu'il soit coupé par les images de blocage

    ImPersoDos = PhotoImage(file='Images/PersoDos.gif')  # image du perso de dos
    PersoDos = can.create_image(x, y, image=ImPersoDos)

    can.coords(PersoDos, x, y)


    if salle == 4:  # initialisation de l'IA en salle 3

        xIA = 225
        yIA = 300  # can.delete(PersoDos)

        ImMonstre1 = PhotoImage(file='Images/IMonstre1.gif')  # image du monstre
        Monstre1 = can.create_image(xIA, yIA, image=ImMonstre1)

        can.coords(Monstre1, xIA, yIA)

    if salle == 5:
        can.delete(Monstre1)

    if salle == 10:
        MenuIng()
        can.create_image(587, 389, image=ImVictoire)
        NbPas.place_forget()
        NbSalle.place_forget()
        BReturnC.place_forget()



def DecomptPas():
    global pas, xIA, yIA, ImMonstre1, Monstre1, NbPas

    if pas > 0:  # décompte des pas uniquement lorsqu'on a marché moins de 21 pas
        pas = pas - 1
        if salle == 4:
            IA()

    NbPas.config(text=pas)  # rafraichie le nombre de pas a chaque fois qu'on entre dans la procédure



def checkpoint():  # checkpoint en salle 3 et 6
    global salle, AffichageIng, MHard
    print("Checkpoint")

    if MHard:
        return()
    
    check = 1

    if salle >= 3:
        check = 3
    if salle >= 6:
        check = 6

    BReturnMenu.destroy()
    BReturnC.destroy()
    BQuitter.destroy()
    AffichageIng = False

    salle = check - 1  # check -1 car on ajoute une salle sans InitPerso
    InitPerso()



### IA ###

def IA():
    global x, y, xIA, yIA, Monstre1, s

    Rx = abs(xIA - x)  # Rx et Ry sont les rapports de disatance horizontaux et verticaux entre les coordonnés du perso et ceux du monstre
    Ry = abs(yIA - y)  # ils permettent de definir si le monstre va se deplacer en horizontal ou en vertical

    AxIA = xIA  # AxIA et ayIA sont les coordonnées de l'IA avec que son déplacement soit effectué
    AyIA = yIA

    if Rx == Ry:  # lorsque Rx=Ry, on choisit aléatoirement l'une des deux variables pour choisir de manière aléatoire le deplacement vertical ou horizontal du monstre
        choix = choice([0, 1])

        if choix == 0:  # si choix=0, le deplacement sera horizontal
            Rx = Rx - 1
        else:
            Rx = Rx + 1


    if Rx < Ry:  # Rx<Ry lorsque le monstre est plus près du perso en horizontal qu'en vertical.

        if x == xIA:  # le perso et le monstre sont sur la meme ligne verticale. on modifie donc yIA
            if y > yIA:  # le perso est en dessous du monstre
                yIA = yIA + 72
            else:  # y < yIA le perso est au dessus du monstre
                yIA = yIA - 72

        else:
            if x > xIA:  # le perso est à droite du monstre
                xIA = xIA + 72  # on deplace donc le monstre vers la droite

            else:  # le perso est à gauche du monstre
                xIA = xIA - 72

    else:  # Rx > Ry lorsque le monstre est plus près de personnage en vertical

        if y == yIA:  # le perso et le monstre sont sur la meme ligne verticale
            if x > xIA:  # le perso est a droite du monstre
                xIA = xIA + 72
            else:  # x < xIA le perso est a gauche du monstre
                xIA = xIA - 72

        else:
            if y > yIA:  # le perso est en dessous du monstre
                yIA = yIA + 72

            else:  # le perso est au dessus du monstre
                yIA = yIA - 72


    caseIA = -1

    for j in range(7):  # on verifie que l'IA ne se deplace pas sur une case bloquée
        for i in range(13):
            if yIA == 228 + j * 72 and xIA == 153 + i * 72:
                caseIA = i + j * 13

    if caseIA in s:  # si la futur case de l'IA est une case bloquée alors on remet les anciens coordonnées et on n'effectue pas le déplacement
        xIA = AxIA
        yIA = AyIA
        return ()

    can.coords(Monstre1, xIA, yIA)

    if x == xIA and y == yIA:
        MenuIng()



### BLOCAGE ###

def CasePerso():
    global yFut, xFut, case

    case = -1

    for j in range(7):
        for i in range(13):
            if yFut == 228 + j * 72 and xFut == 153 + i * 72:
                case = i + j * 13



def InitBlocage():  # on lance InitBlocage a chaque entrée dans une salle pour initialiser les cases bloqués
    global salle, xBloc, ybloc, bloc1, s

    LBloc = [0] * 91  # initialisation des 90 cases sans blocage

    s = []

    s1 = [3, 15, 27, 30, 31, 32, 33, 34, 43, 47, 56, 57, 58, 59, 60, 64, 76, 77, 88, 89, 90]  # index des cases bloqués en salle 1
    s2 = [16, 19, 20, 21, 24, 26, 27, 29, 31, 43, 47, 51, 52, 58, 60, 61, 62, 67, 69, 70]
    s3 = [15, 19, 20, 21, 29, 30, 31, 36, 37, 38, 45, 46, 47, 53, 54, 55, 60, 61, 62, 71, 72, 73, 81, 82]
    s4 = [0, 3, 8, 12, 18, 26, 29, 33, 36, 44, 50, 54, 58, 69, 73, 76, 78, 80, 90]
    s5 = [5, 8, 15, 16, 24, 27, 31, 32, 33, 35, 36, 40, 42, 43, 44, 47, 62, 66, 67, 68, 71, 72, 73, 75, 83]
    s6 = [1, 14, 16, 17, 18, 21, 22, 30, 33, 36, 37, 38, 41, 42, 43, 45, 46, 47, 56, 62, 63, 67, 69, 70, 71, 75, 76]
    s7 = []
    s8 = [14, 15, 16, 18, 20, 21, 22, 23, 30, 32, 34, 36, 37, 40, 48, 49, 54, 56, 59, 61, 63, 67, 68, 70, 72, 79, 83, 85]
    s9 = [3, 4, 5, 7, 14, 16, 22, 27, 34, 35, 36, 40, 42, 43, 44, 45, 46, 50, 53, 54, 61, 69, 70, 72, 73, 76, 80, 88, 89]

    if salle == 1:
        s = s1
    if salle == 2:
        s = s2
    if salle == 3:
        s = s3
    if salle == 4:
        s = s4
    if salle == 5:
        s = s5
    if salle == 6:
        s = s6
    if salle == 7:
        for i in range (27):
            x = randint(0, 90)
            if x != 6 and x != 84:
                s7.append(x)
        s = s7
    if salle == 8:
        s = s8
    if salle == 9:
        s = s9

    s.sort()    #permet de mettre la liste dans l'ordre croissant 

    xBloc = 0
    yBloc = 0

    LxBloc = []
    LyBloc = []

    for i in range(len(s)):  # placement de images du blocage
        a = s[i]  # a change à chaque tour dans la boucle et est égale à la valeur de s à l'indice i
        LBloc[a] = 1

        if a <= 12:  # première ligne
            yBloc = 242

        if a >= 13 and a <= 26:  # deuxième ligne
            yBloc = 314

        if a >= 27 and a <= 39:
            yBloc = 386

        if a >= 40 and a <= 52:
            yBloc = 458

        if a >= 53 and a <= 65:
            yBloc = 530

        if a >= 66 and a <= 78:
            yBloc = 602

        if a >= 79 and a <= 91:
            yBloc = 674
            

        for j in range (13):    #pour les colones
            if (a % 13) == j:
                xBloc = 155 + j*72 

        bloc1 = can.create_image(xBloc, yBloc, image=ImBloc1)

        LxBloc.append(xBloc)
        LyBloc.append(yBloc)

    print(LxBloc)
    print(LyBloc)



### PROGRAMME PRINCIPAL ###

fen = Tk()
fen.title("PROJET F")

can = Canvas(fen, width=1170, height=775, bg="white")  # initialisation du canvas de bonne taille avec un fond blanc
can.pack()

##########################################################

# Mise en ram des différentes images
ImFondIng1 = PhotoImage(file='images/FondIng1.gif')  # ImFondIng1 est l'image de fond pendant la partie
ImgQuitter = PhotoImage(file="images/BouttonQuitter.gif")  # image du bouton quitter
ImgJouer = PhotoImage(file="images/BouttonJouer.gif")
ImgHard = PhotoImage(file="images/BouttonHard.gif")
ImgChrono = PhotoImage(file="images/BouttonChrono.gif")
ImgChekpoint = PhotoImage(file="images/BouttonCheckpoint.gif")
ImgMP = PhotoImage(file="images/BouttonMenuPrincipal.gif")
ImBloc1 = PhotoImage(file="images/bloc1.gif")  # image de case bloquée
ImMenuPrinc = PhotoImage(file="images/MenuPrincipal.gif")  # image menu principal
ImVictoire = PhotoImage(file="images/Victoire.gif")  # image de victoire

# Touches
fen.bind("<Up>", haut)
fen.bind("<Down>", bas)
fen.bind("<Left>", gauche)
fen.bind("<Right>", droite)
fen.bind("<Escape>", echap)

##########################################################


AffichageIng = False

MenuPrincipal()

fen.mainloop()

