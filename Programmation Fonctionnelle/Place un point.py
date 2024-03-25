import math
import matplotlib.pyplot as plt
import numpy as np

MotClePoint = ["place", "point","coordonnées"]
FinDePhrase = "stop"

def stop(Phrase):
    L = []
    Phrase = Phrase.split()
    for i in range(len(Phrase)+1):
        L.append(Phrase[i])
        if Phrase[i] == "stop":
            return L
    return "Il faut un stop"

def TypeMotCle(Phrase):
    s=0
    Phrase = stop(Phrase)
    if Phrase == "Il faut un stop":
        return "Il faut un stop"

    for i in range(len(Phrase)):
        for j in range(len(MotClePoint)):
            if Phrase[i] == MotClePoint[j]:
                s=s+1
    if s == 3:
        return "point"
    else:
        return "autre"

def CommandePoint(Phrase):
    if TypeMotCle(Phrase)=="Il faut un stop":
        return "Il faut un stop"
    elif TypeMotCle(Phrase)=="autre":
        return "Ce n est pas un point"
    if TypeMotCle(Phrase)=="point":
        Phrase = Phrase.split()
        Coordonnees = [Phrase[Phrase.index("coordonnées")+1],Phrase[Phrase.index("coordonnées")+2]]
        return "EnPoint({0} + {1}i)".format(Coordonnees[0], Coordonnees[1])
