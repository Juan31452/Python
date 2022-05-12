def CDT(usuario:str,capital:int,tiempo:int):
 interes = 0.03
 perder = 0.02
 if tiempo > 2 :
     
     valor_interes = (capital * interes * tiempo)/12 
     valor_total = valor_interes + capital
     cadena = ("Para el usuario "+usuario+" "+"La cantidad de dinero a " 
           "recibir,según el monto inicial"+" "+str(capital)+" "+"para un tiempo"
           " de "+str(tiempo)+" "+"meses es "+str(valor_total))
     return cadena
 
 else:
     valor_perder = capital * perder
     valor_total = capital -valor_perder
     cadena = ("Para el usuario "+usuario+" "+"La cantidad de dinero a " 
           "recibir,según el monto inicial"+" "+str(capital)+" "+"para un tiempo"
           " de "+str(tiempo)+" "+"meses es "+str(valor_total))
     return cadena
 

print(CDT("AB1012",1000000,3))     
print(CDT("ER3366",650000,2))     