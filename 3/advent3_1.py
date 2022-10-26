werte = []
gamma0 = 0
gamma1 = 0
gamma_ges = ""
epsilon_ges = ""

with open ('input.txt', 'r') as f:
    for line in f:
        werte.append(line[:-1])

for i in range(0,12):
    for wert in werte:
        if int(wert[i]) == 1:
            gamma1 += 1
        else:
            gamma0 += 1
    if gamma1 > gamma0:
        gamma_ges += "1"
        epsilon_ges += "0"
    else:
        gamma_ges += "0"
        epsilon_ges += "1"
    gamma0 = 0
    gamma1 = 0
print(int(gamma_ges, 2)*int(epsilon_ges, 2))