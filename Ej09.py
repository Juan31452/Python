Milista = ["manzana", "banano", "aguacate"]
Mituple = ("mango", "platano", "cafe")

def myfunc():
    
  print("La Lista es "+ str(Milista))
  print("El tuple es " + str(Mituple))
  Milista.append("Naranja")  
  for i in range(len(Milista)):
    print(str(Milista[i]))
  
myfunc()