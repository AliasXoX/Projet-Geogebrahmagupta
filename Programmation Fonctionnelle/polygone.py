def associer(coord):
    i = 0
    tab = []
    while i<len(coord):
        tab.append('('+coord[i]+','+coord[i+1]+')')
        i+=2
    return tab

def polygone(s):
    s = s.replace(',',' ')
    s = s.replace('(',' ')
    s = s.replace(')',' ')
    phrase = s.split()
    coord = []
    for mot in phrase:
        try:
            val = float(mot)
            coord.append(mot)
        except ValueError:
            continue
    commande = "Polygon("
    for vec in associer(coord):
        commande = commande + vec + ','
    commande = commande[:-1] + ')'
    return commande

keywords = ['triangle','carré','pentagone','hexagone','heptagone','octogone','enneagone','decagone','hendecagone','dodécagone','polygone']
