
#DANIEL SOLANO BARBOZA
#Tarea de recursividad
#Ejercicios de estudiante 1
#11-6-26


def contar_digitos (num):
    if num == 0:
        return 0
    return 1+ contar_digitos (num//10)


#Ejercicio 1 COLA

def sumar_digitos (num):
    return sumar_digitos_aux (num, 0)
def sumar_digitos_aux (num, contador):
    if num == 0:
        return contador
    else:
        return contador + num%10 + sumar_digitos (num//10)


# Ejercicio 2 COLA
def contar_pares (num):
    return contar_pares_aux (num, 0)

def contar_pares_aux (num, contador):

    if num == 0:
        return contador


    if (num%10) % 2 == 0:
            contador += 1
            
    return contar_pares_aux (num//10, contador)

# Ejercicio 3 COLA
def mayor_lista (lista):
    primero = [lista[0]]
    return mayor_aux (lista, primero)

def mayor_aux (lista, mayor):

    if lista == []:
        return mayor [0]

    if lista [0] > mayor [0]:
        mayor.pop()
        mayor.append(lista[0])

    return mayor_aux (lista[1:], mayor)

# Ejercicio 4 PILA


def invertir_numero (num):
    expo = contar_digitos (num) - 1
    return invertir_aux (num, 0, expo)

def invertir_aux (num, inverso, expo):
    if num == 0:
        return 0

    return inverso + (num%10)*10**expo + invertir_aux (num//10, inverso, expo - 1)


# Ejercicio 5 PILA

def eliminar_impares(num):
    if num == 0:
        return 0

    ultimo = num % 10

    if ultimo % 2 == 0:
        return eliminar_impares(num // 10) * 10 + ultimo

    return eliminar_impares(num // 10)

# Ejercicio 6 PILA


def contar_bloques_iguales (lista):
    if lista == []:
        return 0

    if lista == [lista[0]]:
        return 1

    if lista[0] != lista[1]:
        return 1 + contar_bloques_iguales (lista[1:])


    return contar_bloques_iguales(lista[1:])

# Ejercicio 7 PILA

def separar_por_paridad(num):

    if num == 0:
        return [0,0]

    lista = separar_por_paridad(num//10)

    if (num%10) % 2 == 0:
        lista[0] = lista[0] * 10 + (num%10)
        return lista

    lista[1] = lista[1] * 10 + (num%10)
    return lista

# Ejercicio 8 COLA

def detectar_valles (lista):
    return valles_aux (lista, [])

def valles_aux (lista, valles):
    if len(lista) == 2:
        return valles

    if lista [0] > lista [1] < lista [2]:
        valles.append([lista[0],lista[1],lista[2]])
        return valles_aux(lista[1:], valles)
    return valles_aux(lista[1:], valles)

# Ejercicio 9 PILA



def sublistas_ascendentes(lista):
    return sublistas_aux(lista, [], [])

def sublistas_aux(lista, ascendentes, ascensos):

    if lista == []:
        ascendentes.append(ascensos)
        return ascendentes

    if ascensos == []:
        ascensos.append(lista[0])
        return sublistas_aux(lista[1:], ascendentes, ascensos)

    if lista[0] < ascensos[len(ascensos) - 1]:
        ascendentes.append(ascensos[:])
        ascensos.clear()
        ascensos.append(lista[0])
        return sublistas_aux(lista[1:], ascendentes, ascensos)

    if lista[0] > ascensos[len(ascensos) - 1]:
        ascensos.append(lista[0])
        return sublistas_aux(lista[1:], ascendentes, ascensos)


# Ejercicio 10 COLA


def comprimir_repetidos(lista):
    return comprimir_aux(lista, [])

def comprimir_aux(lista, resultado):
    if lista == []:
        return resultado
    
    cantidad = contar(lista, lista[0], 0)
    return comprimir_aux(lista[cantidad:], resultado + [[lista[0], cantidad]])

def contar(lista, elemento, acc):
    if lista == [] or lista[0] != elemento:
        return acc
    return contar(lista[1:], elemento, acc + 1)
        
        
    
        
        

    







    
    
        
            

    

