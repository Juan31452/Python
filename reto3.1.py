def AutoPartes(ventas: list):
    venta={}
    for IdProducto, dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta in ventas:
     if venta.get(IdProducto)==None: 
         venta[IdProducto]=[] 
     venta[IdProducto].append((dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador,fVenta))    
    return venta

print(AutoPartes([
(2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
(2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020')]))