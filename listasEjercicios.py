
print("Hagamos una lista de palabra")
wordCount = int(input("Cuantas palabras quieres que tenga tu lista? \n"))
if wordCount < 1:
    print ("Imposible!")
else:
    words = []
    for _ in range(wordCount):
        words.append(str(input("Ingresa una palabra: ")))
    print(words)
"""
print("Hagamos una lista de palabra - segunda manera")
wordCount = int(input("Cuantas palabras quieres que tenga tu lista? \n"))
if wordCount < 1:
    print ("Imposible!")
else:
    words = [str(input("Ingresa una palabra: ")) for _ in range(wordCount)]
    print(words)


find_word = str(input("que palabra quiere buscar? \n"))
if words.count(find_word) > 0:
	#print("tu palabra aparece" & str(words.count(find_word)) & "veces")
	print("tu palabra aparece {} veces".format(str(words.count(find_word))))
else:
	print("no esta en la lista")
words.index(find_word)
replacement = str(input("porque palabra quieres reemplazar? \n"))
print("porque palabra quieres reemplazar?")
words.insert(words.index(find_word),replacement)
words.remove(find_word)
print(words)
"""

print("Hagamos una lista de palabras en la que se elimina una palabra")
wordCount = int(input("Cuantas palabras quieres que tenga tu lista? \n"))
if wordCount < 1:
    print ("Imposible!")
else:
    words = [str(input("Ingresa una palabra: ")) for _ in range(wordCount)]
    print(words)
find_word = str(input("que palabra quiere eliminar? \n"))
if words.count(find_word) > 0:
    for count in range(words.count(find_word)):
        words.remove(find_word)
    print(words)
else:
    print("no esta en la lista")


