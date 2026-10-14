import Funktioner    

x = input("Ange dosnivå (Gy): ")
dospunkter = input("Ange dospunkter (lista): ")

def vx_uträkning(aktivapunkter, x):
    högre_doser = []
    b = 1
    while b <= len(aktivapunkter):
        if aktivapunkter[b][4] >= x:
            högre_doser.append(aktivapunkter[b])
        b += 1
    andel_högre_doser = len(högre_doser) / len(aktivapunkter)
    return andel_högre_doser
    
    
def vx_funktionen(dospunkter, x):
    prostatapunkter, urethrapunkter, rectumpunkter, normalpunkter = Funktioner.dospunkt_sortering(dospunkter)
    uppdelning = [prostatapunkter, urethrapunkter, rectumpunkter, normalpunkter]
    b = 1
    while b <= len(uppdelning):
        exec(f"{str(uppdelning[b])}_vx") = vx_uträkning(uppdelning[b], x)
        b += 1
    return (prostatapunkter_vx, urethrapunkter_vx, rectumpunkter_vx, normalpunkter_vx)



print(vx_funktionen(dospunkter, x))
