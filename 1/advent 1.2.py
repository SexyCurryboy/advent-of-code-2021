zahlen = []
with open ('input.txt', 'r') as f:
    for line in f:
        zahlen.append(line[:-1])

zahl_neu = 0
zahl_alt = 0
scanner = 0
zahl2 = 0
zahl3 = 0
durchläufe = 0
for zahl in zahlen:
    durchläufe += 1
    zahl1 = int(zahl)
    print(zahl1, zahl2, zahl3)
    zahl_neu = zahl1 + zahl2 + zahl3
    print(zahl_alt, zahl_neu)
    if durchläufe>3 and zahl_neu > zahl_alt:
        scanner += 1
        print(':)', scanner)
    zahl_alt = zahl_neu
    zahl3 = zahl2
    zahl2 = zahl1

print(str(scanner))