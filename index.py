import random
"""

#Ejercicio N° 1
#Pedir un numero, sacar el factorial y mostrar el resultado.

print("Por favor ingrese un número entero mayor que 0")

num = int(input("-> "))
fact = 1

if num < 0:
    print("Recuerde que el número debe ser mayor a 0")    
    
else:
    
        for i in range(1, (num+1)):
            fact *= i    
    
        print(f"El factorial del número ingresado es {fact}") 

#Ejercicio N° 2

# Usando el ciclo while, pedir 5 valores enteros, sumarlos y mostrar la suma y el promedio

print("A continuación ingrese 5 valores por favor")
num = 0
valor = 0
suma = 0
promedio = 0

while num< 5:
    valor = int(input("Ingrese un valor -> "))
    num += 1
    suma += valor
    promedio = suma / num
    
print(f"La suma de los valores ingresados es -> {suma}")
print(f"El promedio de la suma es -> {promedio}") 
    

#Ejercicio N° 3

#Usando un ciclo de repeticion y un match dentro del ciclo de repeticion,
#pedir numeros y decir si es par o impar, sale del ciclo cuando se ingresa 0. 


print("Ingrese una opción del 0 al 4 según su necesidad")

opc = 6
num1 = 0
num2 = 0


while opc != 0:
    print("1 - suma")
    print("2 - resta")
    print("3 - dividir")
    print("4 - Multiplicar")
    print("0 - Salir")
    opc = int(input("-> "))
    if opc <=4 and opc >=1:
        num1 = int(input("ingrese valor deseado -> "))
        num2 = int(input("ingrese valor deseado -> "))
        if num1 % 2 == 0:
            print(f"Sabías que {num1} es un número par?")
        if num1 % 2 != 0:
            print(f"Sabías que {num1} es un número impar?")    
        if num2 % 2 == 0:
            print(f"Sabías que {num2} es un número par?")       
        if num2 % 2 != 0:
            print(f"Sabías que {num2} es un número impar?")          
    if opc == 1:
        res = num1 + num2
        print(f"El resultado de la suma es = {res}")
    elif opc == 2:
        res = num1 - num2
        print(f"El resultado de la resta es = {res}")
    elif opc == 3:
        if num2 == 0:
            print("El 2do valor no puede ser cero")
        else:
            res = num1 / num2
            print(f"El resultado de la división es = {res}")
    elif opc == 4:
        res = num1 * num2
        print(f"El resultado de la multiplicación es = {res}")
    elif opc == 0:
        print("Gracias por participar de la prueba")
    else:
        print("El número ingresado no es válido")        


#Ejercicio N° 4
#Pedir 10 valores aleatorios e imprimir lo siguiente:
        #* Cuantos valores son pares y cuantos impares.
        #* Cuantos valores son multiplo de 5 y de 3 al mismo tiempo.
        #* la suma total de los valores
        #* Cuantos valores son negativos y multiplo de 2.
        #*Promedio total.
"""
nump = 0
numi = 0
num5 = 0
numn = 0
suma = 0
promedio = 0


for i in range(10):
    num = random.randint(-500, 500)
    print(num)
    suma += num
    promedio = suma / 10
    if num % 2 == 0:
        nump += 1
    else:
        numi += 1
    if num % 5 == 0 and num % 3==0:
        num5 += 1
    if num < 0 and num % 2 == 0:
        numn += 1
        
        
        
print(f"Hay {nump} número pares")
print(f"Hay {numi} número impares")
print(f"Hay {num5} números múltiplos de 5 y 3 al mismo tiempo")
print(f"La suma de los valores es = {suma}")
print(f"Hay {numn} números negativos multiplos de 2")
print(f"El promedio de los valores es = {promedio} ")
    



