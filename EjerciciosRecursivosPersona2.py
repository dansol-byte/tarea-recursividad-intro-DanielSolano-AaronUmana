"Taller Github"
"Aarón Umaña"
"Estudiante 2"

# Ejercicio 1 PILA
def sumar_digitos(num):
    if num < 10:
        return num
    return num % 10 + sumar_digitos(num // 10)

# Ejercicio 2 PILA
def contar_pares(num):
    if num < 10:
        if num % 2 == 0:
            return 1
        return 0
    if (num % 10) % 2 == 0:
        return 1 + contar_pares(num // 10)
    return contar_pares(num // 10)

# Ejercicio 3 PILA
def mayor_lista(lista):
    if len(lista) == 1:
        return lista[0]
    
    mayor_resto = mayor_lista(lista[1:])

    if lista[0] > mayor_resto:
        return lista[0]
    return mayor_resto

# Ejercicio 4 COLA
def invertir_numero(num):
    return invertir_num_aux(num, 0)

def invertir_num_aux(num, invertido):
    if num == 0:
        return invertido
    return invertir_num_aux(num // 10, invertido * 10 + num % 10)

# Ejercicio 5 COLA
def eliminar_impares(num):
    return eliminar_imp_aux(num, 0, 1)

def eliminar_imp_aux(num, res, pos):
    if num == 0:
        return res
    digito = num % 10
    if digito % 2 == 0:
        res = digito * pos + res
        pos *= 10
    return eliminar_imp_aux(num // 10, res, pos)

# Ejercicio 6 COLA
def contar_bloques_iguales(lista):
    if lista == []:
        return 0
    return contar_bloques_aux(lista, 1)

def contar_bloques_aux(lista, bloques):
    if len(lista) == 1:
        return bloques
    if lista[0] != lista[1]:
        bloques += 1
    return contar_bloques_aux(lista[1:], bloques)

# Ejercicio 7 COLA
def separar_por_paridad(num):
    pares, impares = separar_aux(num, 0, 0, 1, 1)
    return [pares, impares]

def separar_aux(num, pares, impares, pos_par, pos_impar):
    if num == 0:
        return pares, impares
    digito = num % 10
    if digito % 2 == 0:
        pares = digito * pos_par + pares
        pos_par *= 10
    else:
        impares = digito * pos_impar + impares
        pos_impar *= 10
    return separar_aux(num // 10, pares, impares, pos_par, pos_impar)

# Ejercicio 8 PILA
def detectar_valles(lista):
    if len(lista) < 3:
        return []
    res = detectar_valles(lista[1:])
    if lista[1] < lista[0] and lista[1] < lista[2]:
        return [[lista[0], lista[1], lista[2]]] + res
    return res

# Ejercicio 9 COlA
def sublistas_ascendentes(lista):
    if lista == []:
        return []
    return sublistas_aux(lista[1:], [[lista[0]]])

def sublistas_aux(lista, res):
    if lista == []:
        return res
    ultimo = res[-1][-1]
    if lista[0] > ultimo:
        res[-1].append(lista[0])
    else:
        res.append([lista[0]])
    return sublistas_aux(lista[1:], res)
