zahlen = []
with open ('input.txt', 'r') as f:
    for line in f:
        zahlen.append(line[:-1])
        print(line.split())
        print(line.split(','))

#dictionary mit allen horizontalen und allen vertikalen, vorkommende elemente löschen und leere einträge im dictionary überprüfen -> vollständiges feld