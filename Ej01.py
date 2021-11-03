numero1 = 0
numero2 = 0
operacion = 0

i = 0
while i < 4:
    i+=1
    numero1 = int(input("Primer Numero :"))
    numero2 = int(input("Segundo Numero :"))
    operacion = int(input("Seleccione >> 1.suma , 2.resta , 3.división , 4.multiplicación , 5.Salir :"))
    if operacion == 1:
       print("Suma :",numero1 + numero2)
       continue
    elif operacion == 2:
      print(numero1 - numero2)
      continue
    
    elif operacion == 3:
      print(numero1 / numero2)
      continue
    elif operacion == 4:
      print(numero1 * numero2)
      continue
else:
      print("Hasta Luego")
