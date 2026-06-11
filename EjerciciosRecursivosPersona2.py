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
