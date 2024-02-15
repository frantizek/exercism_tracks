import re

def abbreviate(words):
    el_acronimo = ""
    lista_de_palabras = str(words.replace('-', ' ')).split(' ',)
    for palabra in lista_de_palabras:
        el_acronimo += re.sub("[^a-zA-Z]", "", palabra)[:1:].upper()

    return el_acronimo
