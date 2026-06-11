"Taller Github"
"Aarón Umaña"
"Estudiante 2"

# Ejercicio 1 PILA
def sumar_digitos(num):
    if num < 10:
        return num
    return num % 10 + sumar_digitos(num // 10)
