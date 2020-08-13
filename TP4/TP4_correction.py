#from TP4 import *
from rescale import *
import random
import math

class Time:

    def __init__(self):
        self.current_year = 2020
        self.travel_year = -math.inf
        self.d = {"neolithic" : (-10000, -3000), 
        "ancient age" : (-2999, 476), 
        "medieval age" : (477, 1492), 
        "modern age" : (1493, 1789),
        "contemporary age" : (1790, 2020)}

    def setEpoch(self, epoch):
        years_interval = self.d[epoch]
        self.travel_year = random.randint(years_interval[0], years_interval[1])

    def getYearToTravel(self):
        return self.travel_year

    def getMaxBound(self):
        return self.d["neolithic"][0]

    def getCurrentYear(self):
        return self.current_year


class HackTool:

    def __init__(self):
        self.current_year = 2020

    def _verifyHackCode(self, max_value, hackCode):
        if hackCode < math.pow(max_value, 4):
            print("The HackCode ", hackCode, "is correct")
            return True
        return False

    def hackTime(self, travel_year, current_year):
        loading = 0
        printing = True
        while loading < 100:
            current_year -= 2
            loading = rescale(100, self.current_year - travel_year, current_year - travel_year)
            loading = 100 - loading
            if int(loading) % 10 == 0 and printing:
                print(int(loading), "%")
                printing = False
            elif int(loading) % 10 != 0:
                printing = True
        return True
    
    def getHackCode(self, max_value, travel_year):
        res = -1
        hc = int(math.pow(travel_year, 4))
        if self._verifyHackCode(max_value, hc):
            print("Launching time travel")
            res = hc
        return res




def main():
    __ITERATION__ = 23
    reussite = 0
    echec = 0
    note1 = 0

    ############
    #Correction#
    ############

    __epoch_to_travel__ = "medieval age"
    t = Time()
    ht = HackTool()
    t.setEpoch(__epoch_to_travel__)
    ytt = t.getYearToTravel()
    hc = ht.getHackCode(t.getMaxBound(), ytt)
    if hc != -1 and ht.hackTime(ytt, t.getCurrentYear()):
        print("Time travel to the",__epoch_to_travel__,"COMPLETE")
    else:
        print("HackCode incorrect")
        print("Aborting the time travel")


    ############
    #Correction#
    ############
    
    '''
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
    '''
    
if __name__ == "__main__":
    # execute only if run as a script
    main()