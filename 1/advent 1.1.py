zahlen = []
with open ('input.txt', 'r') as f:
    for line in f:
        zahlen.append(line[:-1])

zahl_alt = 0
scanner = 0
for zahl in zahlen:
    zahl_neu=int(zahl)
    if zahl_alt < zahl_neu:
        scanner += 1
    zahl_alt = zahl_neu

print(str(scanner-1))