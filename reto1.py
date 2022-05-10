def calculocdt(usuario:str,capital:int,tiempo:int):
 interes = 0.03
 perder = 0.02
 if tiempo > 2 :
     
     valor_interes = (capital * interes * tiempo)/12 
     valor_total = valor_interes + capital
     print("Para el usuario "+ usuario," la cantidad de dinero a recibir,\n" 
           "según el monto inicial",+ capital ,
           "\n para un tiempo de",tiempo ,"meses es" ,valor_total)
 
 if tiempo <=2:
     valor_perder = capital * perder
     valor_total = capital -valor_perder
     print("Para el usuario "+ usuario," la cantidad de dinero a recibir,\n" 
           "según el monto inicial",+ capital ,
           "\n para un tiempo de",tiempo ,"meses es" ,valor_total)

usu = input("Usuario :")
cap = int(input("Capital :"))
tie = int(input("Tiempo :"))
 
calculocdt(usu,cap,tie)     