def conta_letras(frase, contar="vogal"):
    contador_vogal = 0
    contador_consoantes = 0
    frasesp = frase.replace(" ","") #frase sem espaço
    for i in frasesp:
        if i == "A" or i == "E" or i == "I" or i == "O" or i == "U" or i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            contador_vogal+=1
        else:
            contador_consoantes+=1
    if contar == "consoantes":
        return contador_consoantes
    else:
        return contador_vogal
