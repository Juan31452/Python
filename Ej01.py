numero1 = 0
numero2 = 0
suma = 0
resta = 0
multiplica = 0
divide = 0
numero1 = int(input("Primer Numero :"))
numero2 = int(input("Segundo Numero :"))
operacion = input("Seleccione >> 1.suma , 2.resta , 3.división , 4.multiplicación ")
if operacion == "1":

    print("Suma :",numero1 + numero2)
elif operacion == "2":

    print(numero1 - numero2)

elif operacion == "3":

    print(numero1 / numero2)

elif operacion == "4":

    print(numero1 * numero2)
else:
    print("Seleccione un numero del 1 al 4")
