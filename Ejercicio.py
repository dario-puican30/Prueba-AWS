'''
def sumar_numeros(numero1, numero2):
    suma = numero1 + numero2
    return suma

def main():
    print("Hola Mundo")
    print(sumar_numeros(5,10))
    print(sumar_numeros(8,10))
    
main()

------------

def comparar_numero(numero1, numero2):
    resultado = ''
    if numero1 > numero2:
        resultado = str(numero1) + " es mayor que " + str(numero2)
    elif numero1 < numero2:
        resultado = str(numero1) + " es menor que " + str(numero2)
    else:
        resultado = str(numero1) + " es igual a " + str(numero2)
    return resultado

def main():
    print(comparar_numero(15, 10))
    
main()

------------

def prueba_for():
    print(list(range(0, 5, 1)))

def main():
    prueba_for()
    
main()

------------

def main():
    
    numero_inicial = int(input("Ingrese el número inicial: "))
    numero_final = int(input("Ingrese el número final: "))
  
    print(list(range(numero_inicial,numero_final + 1,1)))

main()

------------

def main():

    i = 0
    while i < 5:
        print(i)
        i += 1
    
main()

------------


def calcular_mes_de_venta(monto_inicial):
    if monto_inicial <= 0:
        return "El monto inicial debe ser positivo."

    monto_objetivo = monto_inicial * 2
    monto_actual = monto_inicial
    mes = 0

    print(f"Monto inicial: {monto_inicial:.2f}")
    print(f"Monto objetivo (doble): {monto_objetivo:.2f}\n")

    while monto_actual < monto_objetivo:
        mes += 1
        if mes % 4 == 0:  # Mes 4 y múltiplos de 4
            perdida = -0.025  # Pierde 2.5%
            monto_actual *= (1 + perdida)
            print(f"Mes {mes}: Pérdida del {abs(perdida*100)}% -> Monto actual: {monto_actual:.2f}")
        else:  # Otros meses
            ganancia = 0.10  # Gana 10%
            monto_actual *= (1 + ganancia)
            print(f"Mes {mes}: Ganancia del {ganancia*100}% -> Monto actual: {monto_actual:.2f}")

    return f"\n¡El monto objetivo se ha duplicado! Debes vender tus acciones en el mes {mes}."
    
monto_inicial = 1000
print(calcular_mes_de_venta(monto_inicial))

------------
'''

def calcular_sueldo_despues_n_anos(tipo_trabajador, sueldo_inicial, n_anos):
    
    sueldo_actual = float(sueldo_inicial)

    for ano in range(1, n_anos + 1):
        if tipo_trabajador == 'g':  # Gerente
            if ano % 4 == 0: # Cada 4 años
                aumento = 0.18
            else:
                aumento = 0.14
        elif tipo_trabajador == 'e':  # Empleado
            if ano % 4 == 0: # Cada 4 años
                aumento = 0.12
            else:
                aumento = 0.08
        
        sueldo_actual *= (1 + aumento)

    return sueldo_actual

def main():
    print(calcular_sueldo_despues_n_anos("g", 1000, 5))
    
main()
    
        
        
    