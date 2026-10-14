import Funktioner

x = input("Ange önskad andel (i procent): ")
dospunkter = input("Ange dospunkter (lista): ")

def dx_uträkning(aktivapunkter, x):
    dos_lista = []
    b = 1
    while b <= len(aktivapunkter):
        dos_lista.append(aktivapunkter[b][4])
        b += 1
    sorterad_lista = sorted(dos_lista)
    andel = round((x / 100) * len(sorterad_lista))
    agerande_punkter = sorterad_lista[:andel]
    dosvärde = agerande_punkter[-1]
    return dosvärde
  

def dx_funktionen(dospunkter, x):
    prostatapunkter, urethrapunkter, rectumpunkter, normalpunkter = Funktioner.dospunkt_sortering(dospunkter)
    uppdelning = [prostatapunkter, urethrapunkter, rectumpunkter, normalpunkter]
    b = 1
    while b <= len(uppdelning):
        exec(f"{str(uppdelning[b])}_Dx") = Dx_uträkning(uppdelning[b], x)
        b += 1
    return (prostatapunkter_Dx, urethrapunkter_Dx, rectumpunkter_Dx, normalpunkter_Dx)


print(dx_funktionen(dospunkter, x))
