minutos = 0
valorminuto = 355
iva = 0.20
totaliva = float
totalpagar = 0
total = 0
minutos = int(input("Cantidad Minutos :"))
totalpagar =  minutos * valorminuto
totaliva = totalpagar * iva
total = totalpagar + totaliva
print("Valor Minutos",totalpagar)
print("IVA : ",totaliva)
print("Total :",total)