from exemple import *
from rescale import *
import math
import random

def ex1_data_generation():
    data = []
    name = "hero"
    for i in range(random.randint(20, 100)):
        fullname = name + str(i)
        strength = random.randint(1, 100)
        size = random.randint(100, 200)
        data.append((fullname, strength, size))
    return data

# Nom : Le meilleur partenaire
# Paramètre : liste de tuples <nom, force, taille>
# Retour : string - le nom du héro qui a le score force * taille le plus petit
def ex1_correction(input):
    minimum = math.inf
    argmin = ""
    for d in input:
        value = d[1] * d[2]
        if value < minimum:
            minimum = value
            argmin = d[0]
    return argmin
    
def ex2_data_generation():
    data = {}
    name = "hero"
    ret_name = ""
    nb_data = random.randint(20, 100)
    for i in range(nb_data):
        fullname = name + str(i)
        number = "06"
        for i in range(8):
            number += str(random.randint(0, 9))
        data[fullname] = number
    j = random.randint(0, len(data) - 1)
    cnt = 0
    for key in data:
        if cnt == j:
            ret_name = key
        cnt += 1
    return ret_name, data

# Nom : Contacter le nouveau partenaire
# Paramètre : string - nom du héro à contacter, dictionnaire - le répertoire téléphonique de Batman
# Retour : string - le numéro de la personne que Batman a choisi
def ex2_correction(name, input):
    return input[name]

def ex3_data_generation():
    joker_places = set()
    not_police_places = set()
    place_name = "place"
    nb_data = random.randint(10, 110)
    for i in range(nb_data):
        fullname = place_name + str(i)
        joker_places.add(fullname)
        if random.randint(0, 3) <= 0 :
            not_police_places.add(fullname)
    return joker_places, not_police_places

# Nom : Une menace pèse
# Paramètre : set - lieux que le Joker veut attaquer, set - lieux impossibles à surveiller par la police
# Retour : set - lieux que Batman et son acolyte doivent surveiller
def ex3_correction(set1, set2):
    return set1 & set2

def ex4_data_generation():
    places = set()
    place_name = "place"
    nb_data = random.randint(10, 110)
    for i in range(nb_data):
        fullname = place_name + str(i)
        places.add((fullname, random.randint(25, 5000)))
    return places

# Nom : Organisation des rondes
# Paramètre : set - lieux que Batman et son partenaire doivent surveiller
# Retour : set - lieux que Batman doit surveiller
def ex4_correction(input):
    result = list(input)
    result.sort(key=lambda x: x[1])
    del result[int(len(result) / 2):len(result)]
    return set(result)


def main():
    __ITERATION__ = 100
    reussite = 0
    echec = 0

    note1 = 0
    note2 = 0
    note3 = 0
    note4 = 0

    ### Exercice 1 ###
    for i in range(__ITERATION__):
        data = ex1_data_generation()
        solution = ex1_correction(data)
        if solution == exercice1(data):
            reussite += 1
        else:
            echec += 1
    assert reussite + echec == __ITERATION__
    note1 = rescale(20, __ITERATION__, reussite)
    print("note1 :", note1,"/20")

    ### Exercice 2 ###
    reussite = 0
    echec = 0
    for i in range(__ITERATION__):
        name, data = ex2_data_generation()
        solution = ex2_correction(name, data)
        if solution == exercice2(name, data):
            reussite += 1
        else:
            echec += 1
    assert reussite + echec == __ITERATION__
    note2 = rescale(20, __ITERATION__, reussite)
    print("note2 :", note2,"/20")

    ### Exercice 3 ###
    reussite = 0
    echec = 0
    for i in range(__ITERATION__):
        set1, set2 = ex3_data_generation()
        solution = ex3_correction(set1, set2)
        if len(solution & exercice3(set1, set2)) == len(solution):
            reussite += 1
        else:
            echec += 1
    assert reussite + echec == __ITERATION__
    note3 = rescale(20, __ITERATION__, reussite)
    print("note3 :", note3,"/20")

    ### Exercice 4 ###
    reussite = 0
    echec = 0
    for i in range(__ITERATION__):
        data = ex4_data_generation()
        solution = ex4_correction(data)
        if len(solution & exercice4(data)) == len(solution):
            reussite += 1
        else:
            echec += 1
    assert reussite + echec == __ITERATION__
    note4 = rescale(20, __ITERATION__, reussite)
    print("note4 :", note4,"/20")

    # Note finale
    print("Total :", (note1 + note2 + note3 + note4) / 4)

    
if __name__ == "__main__":
    # execute only if run as a script
    main()