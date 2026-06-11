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

