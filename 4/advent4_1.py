input = []
kugeln = []
zeilen = []
bingo = []

with open ('input.txt', 'r') as f:
    for line in f:
        input.append(line[:-1])

kugeln = input[0].split(",")
input.pop(0)
for line in input:
    if line.split() != []:
        zeile = [int(x) for x in line.split()]
        print(zeile)
        zeilen.append(zeile)

for i in range(0,len(zeilen)-4,5):
    feld = [zeilen[i], zeilen[i+1], zeilen[i+2], zeilen[i+3], zeilen[i+4]]
    for n in range(0,5):
        vertikal = [zeilen[i][n], zeilen[i+1][n], zeilen[i+2][n], zeilen[i+3][n], zeilen[i+4][n]]
        feld.append(vertikal)
    bingo.append(feld)

def check():
    summe = 0
    for kugel in kugeln:
        for f_ind, feld in bingo:
            for linie in feld:
                for zahl in linie:
                    if zahl == int(kugel):
                        linie.remove(zahl)
                    if linie == []:
                        print('finito')
                        for i in range(0,5):
                            summe += sum(feld[i])
                            print(sum(feld[i]))
                        print(feld)
                        return(summe * int(kugel))

print(check())

#liste mit allen horizontalen und allen vertikalen, vorkommende elemente löschen und leere einträge in liste überprüfen -> vollständige reihe
