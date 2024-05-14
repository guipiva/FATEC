def conversao(hora,minuto,segundo):
    for i in range(hora,minuto,segundo):
        hs = hora * 60**2
        ms = minuto * 60

        return (hs + ms + segundo)