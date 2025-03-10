# Aula: 04. Listas

#exemplo 1 - acessando valores

lista_numeros = [1, 2, 3, 4]

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])
print(lista_numeros[3])

#exemplo 2 - alterando valores

lista_numeros = [1, 2, 3, 4]

lista_numeros[0] = 10

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])
print(lista_numeros[3])

#exemplo 3 - listas com tipos diferentes

strings = ["hello", "world", "python"]
decimais = [1.0, 1.5, 2.0]
inteiros = [1, 2, 3]

print(strings[0])
print(strings[1])
print(strings[2])

#exemplo 4 - append

lista_vazia = []

lista_vazia.append("hello world")
lista_vazia.append("python")

print(lista_vazia[0])
print(lista_vazia[1])

#exemplo 5 - insert

lista_vazia = []

lista_vazia.insert(0, "hello world")
lista_vazia.insert(1, "python")

#exemplo 6 - remove

lista_vazia = ["hello world", "python"]

lista_vazia.remove("hello world")
lista_vazia.remove("python")

#exemplo 8 - len, min, max

lista_numeros = [1, 2, 3, 4]

print("total: ", len(lista_numeros))
print("menor valor: ", min(lista_numeros))
print("maior valor: ", max(lista_numeros))