diccionario = {'nombre': 'Carlos', 'edad': 22, 'cursos': ['python','flask']}
print(diccionario)
print(diccionario['nombre'])
print(diccionario['edad'])
print(diccionario['cursos'][1])

dic = dict(nombre= 'Nestor', apellido='Juarez', edad=22)
print(dic)
#print(dic['edad'])


#Para imprimir llave- valor
for key,value in diccionario.items():
	print(key + " : " + str(value))
"""
lista de cursos = diccionario['cursos']
lista_cursos.append('Java')
print(lista_cursos)
print(diccionario)	
"""
#para saber la longitud de un diccionario- devuelve el número de elementos que tiene el dicionario
print(len(diccionario))

#para saber que llaves tiene tu diccionario- devuelve una lista con las claves del diccionario.
print(diccionario.keys())

#Me devuelve una lista con los valores del diccionario
print(diccionario.values())

#decuelve el valor del elemento con su clave y si no lo encuentra trae un valor por default
print(diccionario.get('nombre','Juanito'))


#inserta un elemento al diccionario con su clave:valor
diccionario['key'] = 'value'
print(diccionario) 

#para eliminar un elemento por la clave
diccionario.pop('key')
print(diccionario)

#para duplicar un diccionario
diccionario2 = diccionario.copy()
print(diccionario2)

#Añade los elementos de un diccionario a otro
diccionario.update(dic)
print(diccionario)
