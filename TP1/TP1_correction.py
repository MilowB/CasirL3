from exemple import *
from rescale import *
import random

def fibo(nterms):
    n1 = 0
    n2 = 1
    if nterms <= 1:
        return nterms    
    for i in range(2, nterms):
        suivant = n1 + n2
        n1 = n2
        n2 = suivant
    return n2


def main():
    __ITERATION__ = 100
    reussite = 0
    echec = 0
    note1 = 0
    # exercice2 : correction manuelle
    note3 = 0

    ### Exercice 1 ###
    for i in range(__ITERATION__):
        n = random.randint(1, 99)
        res = exercice1(n)
        if (res and n > 20) or (not res and n <= 20):
            reussite += 1
        else :
            echec += 1
    assert reussite + echec == __ITERATION__
    note1 = rescale(5, __ITERATION__, reussite)
    print("exercice 1 :", note1,"/5")
    
    ### Exercice 2 ###
    reussite = 0
    echec = 0
    for i in range(__ITERATION__):
        n = random.randint(0, 200)
        if fibo(n) == exercice3(n):
            reussite += 1
        else :
            echec += 1
    note3 = rescale(3, __ITERATION__, reussite)
    print("exercice 3 :", note3,"/3")
    print("total :", note1 + note3,"/8")



if __name__ == "__main__":
    # execute only if run as a script
    main()