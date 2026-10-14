def vävuppdelning(dospunkter, vävnad):
    antal_punkter = len(dospunkter)
    b = 1
    Dospunkter_med_samma_vävnad = []
    while b <= antal_punkter:
        if dospunkter[b][5] == vävnad:
            Dospunkter_med_samma_vävnad.append(dospunkter[b])
        b += 1
    return(Dospunkter_med_samma_vävnad)

def dospunkt_sortering(dospunkter):
    prostatapunkter = vävuppdelning(dospunkter, "Prostata")
    urethrapunkter = vävuppdelning(dospunkter, "Urethra")
    rectumpunkter = vävuppdelning(dospunkter, "Rectum")
    normalpunkter = vävuppdelning(dospunkter, "Normalvävnad")
    return (prostatapunkter, urethrapunkter, rectumpunkter, normalpunkter)