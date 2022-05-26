def cliente(informacion:dict):
    
    informacion["id_cliente"]
    informacion["nombre"]
    informacion["edad"]
    informacion["primer_ingreso"]
    
    if informacion["edad"] > 18:
     informacion["atraccion"] = "X-treme"
     informacion["apto"] = True
     valor_boleta = 20000
     if informacion['primer_ingreso'] == True:
      descuento = 0.05
      t_descuento = valor_boleta * descuento
      total = valor_boleta - t_descuento
      informacion["total_boleta"] = total
     else:
      informacion["total_boleta"] = valor_boleta
              
    elif informacion["edad"] >= 15 and informacion["edad"]<= 18 :
     informacion["atraccion"] = "carros chocones"
     valor_boleta =5000
     if informacion['primer_ingreso'] == True:
      descuento = 0.07
      t_descuento = valor_boleta * descuento
      total = valor_boleta - t_descuento
      informacion["total_boleta"] = total   
     else:
      informacion["total_boleta"] = valor_boleta
    
    elif informacion["edad"] >= 7 and informacion["edad"]< 15 :
     informacion["atraccion"] = "sillas_voladoras"
     valor_boleta =10000
     if informacion['primer_ingreso'] == True:
      descuento = 0.05
      t_descuento = valor_boleta * descuento
      total = valor_boleta - t_descuento
      informacion["total_boleta"] = total   
     else:
      informacion["total_boleta"] = valor_boleta
    
    return informacion

informacion={}
informacion["id_cliente"] = 1
informacion["nombre"] = "Juan"
informacion["edad"] = 8
informacion["primer_ingreso"] = True
print("Datos :", cliente(informacion))


    
    