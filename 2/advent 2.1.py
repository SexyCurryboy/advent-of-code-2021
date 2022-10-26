befehle = []
tiefe = 0
strecke = 0
with open ('input.txt', 'r') as f:
    for line in f:
        befehle.append(line[:-1])

for befehl in befehle:
    if 'up' in befehl:
        tiefe -= int((befehl.replace('up ', '')))
    elif 'down' in befehl:
        tiefe += int((befehl.replace('down ', '')))
    elif 'forward' in befehl:
        strecke += int((befehl.replace('forward ', '')))

print(strecke*tiefe)

