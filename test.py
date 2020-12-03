
"""
    @brief: evalua tres numeros que recibe como parametros.
            Suma los dos primeros y multiplica el tercero
            al resultado si cumple la condicion definida

    @n1: valor ingresado por el usuario
    @n2: valor ingresado por el usuario
    @n3: valor a evaluar a la condicion
"""

def ejemplo_none(n1, n2, n3 = None):
    resultado = n1 + n2
    if n3 is not None:
        resultado = resultado * n3

    return resultado

print(ejemplo_none(4,4,2))