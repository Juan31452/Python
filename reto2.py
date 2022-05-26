def cliente(informacion:dict)->dict:
    

  respuesta={}
  respuesta['nombre'] = informacion['nombre']
  respuesta['edad'] = informacion['edad']
    
  if informacion['edad'] >=7:
   if informacion['edad'] > 18:
    respuesta["atraccion"] = 'X-Treme'
    respuesta['apto'] = True
    if informacion['primer_ingreso'] == True:
     valor_boleta = 20000 
     descuento = 0.05
     t_descuento = valor_boleta * descuento
     total = valor_boleta - t_descuento
     respuesta['primer_ingreso'] = True
     respuesta['total_boleta'] = total
    else:
     respuesta['primer_ingreso'] = False
     respuesta['total_boleta'] = 20000
                
   elif informacion['edad'] >= 15 and informacion['edad']<= 18 :
     respuesta['atraccion'] = 'Carros chocones'
     respuesta['apto'] = True
     if informacion['primer_ingreso'] == True:
       valor_boleta =5000
       descuento = 0.07
       t_descuento = valor_boleta * descuento
       total = valor_boleta - t_descuento
       respuesta['primer_ingreso'] = True
       respuesta['total_boleta'] = total   
     else:
       respuesta['primer_ingreso'] = False
       respuesta['total_boleta'] = 5000
      
   elif informacion['edad'] >= 7 and informacion['edad']< 15 :
    respuesta['atraccion'] = 'Sillas voladoras'
    respuesta['apto'] = True
    if informacion['primer_ingreso'] == True:
     valor_boleta =10000
     descuento = 0.05
     t_descuento = valor_boleta * descuento
     total = valor_boleta - t_descuento
     respuesta['primer_ingreso'] = True
     respuesta['total_boleta'] = total   
    else:
     respuesta['primer_ingreso'] = False
     respuesta['total_boleta'] = 10000
      
  else:
     respuesta['atraccion'] = 'N/A'
     respuesta['apto'] = False
     respuesta['primer_ingreso'] = True
     respuesta['total_boleta'] = 'N/A'   
         
  return respuesta

informacion={}
#informacion={'id_cliente':1,'nombre':'Jhoana Fernandez','edad':20,'primer_ingreso':True}
#informacion={'id_cliente':1,'nombre':'Jhoana Fernandez','edad':20,'primer_ingreso':False}
#informacion={"Id_cliente":2,"nombre":"Gloria Suarez","edad":3,"primer_ingreso":True}
#informacion={'id_cliente':3,'nombre':'Tatiana Suarez','edad':17,'primer_ingreso':True}
#informacion={'id_cliente':3,'nombre':'Tatiana Suarez','edad':17,'primer_ingreso':False}
#informacion={'id_cliente':4,'nombre':'Tatiana Ruiz','edad':8,'primer_ingreso':True}
informacion={'id_cliente':4,'nombre':'Tatiana Ruiz','edad':8,'primer_ingreso':False}


print("Datos :", cliente(informacion))


    
 