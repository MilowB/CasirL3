from exemple import *
from rescale import *
from math import sqrt
import random

#####################################################
#         CORRECTION ECRITE PAR INSALGO            #
#####################################################

#Distance entre 2 points
def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

def correction(input):
    parse = input.split('\n')
    line_number = 0
    #Position de la bombe:
    Xb, Yb = [float(i) for i in parse[line_number].split()]
    line_number += 1
    #Nombre de suspects et de positions par suspect:
    N, T = [int(i) for i in parse[line_number].split()]
    line_number += 1

    #vitesse maximale (Cf enonce)
    vitesseMax = 100
    coupables = set()
    lastX,lastY = 0,0

    for i in range(N):
        #Nom du suspect
        suspect = parse[line_number]
        line_number += 1
        criminel = False
        for j in range(T):
            X,Y = [float(k) for k in parse[line_number].split()]
            line_number += 1
            #Si entre 2 positions successives, le suspect a le temps d'atteindre
            #la position de la bombe sans depasser la vitesse maximale,
            #alors il est potentiellement coupable
            if j>0 and (distance(lastX,lastY,Xb,Yb)+distance(Xb,Yb,X,Y)) <= vitesseMax:
                criminel = True
            lastX,lastY = X,Y
        if(criminel):
            coupables.add(suspect)

    #On affiche en sortie la liste des suspects potentiellement coupables
    #(Il y en a au moins un)        
    return coupables

#####################################################
#                  FIN CORRECTION                   #
#####################################################

def main():
    __ITERATION__ = 23
    reussite = 0
    echec = 0
    note1 = 0

    ### Exercice 1 ###
    for i in range(__ITERATION__):
        f = open("input/input"+str(i)+".txt", "r")
        solution = correction(f.read())
        print(solution)
        if len(solution & exercice1(f.read())) == len(solution):
            reussite += 1
        else:
            echec += 1
    assert reussite + echec == __ITERATION__
    note1 = rescale(20, __ITERATION__, reussite)
    print("Total :", note1,"/20")
    
if __name__ == "__main__":
    # execute only if run as a script
    main()