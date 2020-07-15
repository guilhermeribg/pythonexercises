def maiusculas(frase):
    frase_final = ""
    array_frase = list(frase)
    for i in array_frase:
        if i >= "A" and i <= "Z":
            frase_final += i
    return frase_final