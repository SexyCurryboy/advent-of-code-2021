werte = []
gamma0 = 0
gamma1 = 0
epsilon0 = 0
epsilon1 = 0
gamma = None
epsilon = None
with open ('input.txt', 'r') as f:
    for line in f:
        werte.append(line[:-1])

wertegamma_neu = werte
werteepsilon_neu = werte 

for i in range(0,12):
    wertegamma_alt = wertegamma_neu
    if len(wertegamma_alt) < 1:
        break
    for wert in wertegamma_alt:
        if int(wert[i]) == 1:
            gamma1 += 1
        else:
            gamma0 += 1
    if gamma1 > gamma0:
        gamma = 1
    elif gamma1 < gamma0:
        gamma = 0
    else:
        gamma = 1

    gamma_end = wertegamma_neu[0]

    wertegamma_neu = []

    for wert in wertegamma_alt:
        if int(wert[i]) == gamma:
            wertegamma_neu.append(wert)
    gamma0 = 0
    gamma1 = 0
    gamma = None

for i in range(0,12):
    werteepsilon_alt = werteepsilon_neu
    if len(werteepsilon_alt) < 1:
        break
    for wert in werteepsilon_alt:
        if int(wert[i]) == 1:
            epsilon1 += 1
        else:
            epsilon0 += 1
    if epsilon1 > epsilon0:
        epsilon = 0
    elif epsilon1 < epsilon0:
        epsilon = 1
    else:
        epsilon = 0

    if len(werteepsilon_alt) != 1:
        werteepsilon_neu = []
    epsilon_end = werteepsilon_neu[0]
    for wert in werteepsilon_alt:
        if int(wert[i]) == epsilon:
            werteepsilon_neu.append(wert)
    epsilon0 = 0
    epsilon1 = 0
    epsilon = None

print(int(gamma_end, 2)*int(epsilon_end, 2))

#Liste 2 mal kopieren
#Nummer finden (1 oder 0)
#Falls 1:
#Nochmals checken in kopierter Liste1 & alle 0 entfernen
#Checken in kopierter Liste2 & alle 1 entfernen
#Falls 0 andersherum
#Anzahl Elemente in Liste checken, falls nur eins:
#fertig & Ergebnis berechnen
#sonst wiederholen