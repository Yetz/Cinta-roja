entrada=raw_input("Introduce una cadena: ")
 
diccionario={}
 
for letra in entrada:
    if diccionario.has_key(letra):
        diccionario[letra]=diccionario[letra]+1
    else:
        diccionario[letra]=1
 
print diccionario