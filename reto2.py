def cliente(informacion:dict)->dict:
    

    respuesta={}
    respuesta['nombre'] = informacion['nombre']
    respuesta['edad'] = informacion['edad']
    
    
    if informacion["edad"] > 18:
     respuesta["atraccion"] = "X-treme"
     respuesta["apto"] = True
     if informacion['primer_ingreso'] == True:
      valor_boleta = 20000
      descuento = 0.05
      t_descuento = valor_boleta * descuento
      total = valor_boleta - t_descuento
      respuesta['primer_ingreso'] = True
      respuesta["total_boleta"] = total
     else:
      respuesta['primer_ingreso'] = False
      respuesta["total_boleta"] = valor_boleta
              
    elif informacion["edad"] >= 15 and informacion["edad"]<= 18 :
     respuesta["atraccion"] = "carros chocones"
     respuesta["apto"] = True
     if informacion['primer_ingreso'] == True:
      valor_boleta =5000
      descuento = 0.07
      t_descuento = valor_boleta * descuento
      total = valor_boleta - t_descuento
      respuesta['primer_ingreso'] = True
      respuesta["total_boleta"] = total   
     else:
      respuesta['primer_ingreso'] = False
      respuesta["total_boleta"] = valor_boleta
    
    elif informacion["edad"] >= 7 and informacion["edad"]< 15 :
     respuesta["atraccion"] = "sillas_voladoras"
     respuesta["apto"] = True
     if informacion['primer_ingreso'] == True:
      valor_boleta =10000
      descuento = 0.05
      t_descuento = valor_boleta * descuento
      total = valor_boleta - t_descuento
      respuesta['primer_ingreso'] = True
      informacion["total_boleta"] = total   
     else:
      respuesta['primer_ingreso'] = False
      informacion["total_boleta"] = valor_boleta
    
    elif informacion["edad"] < 7:
     informacion["atraccion"] = "N/A"
     informacion["apto"] = False
     informacion["total_boleta"] = "N/A"   
         
    return respuesta

informacion={}
informacion={"Id_cliente":1,"nombre":"Jhoana Fernandez","edad":20,"primer_ingreso":True}

print("Datos :", cliente(informacion))


    
    