productos=["peluche", "muñeca", "pelota", "carrito", "zapatos"]
precios= [40, 60, 25,30, 120]

i=0                                #el listado empieza del 0
while i<4:
 maximum=max(precios)       
 pos_max=precios.index(maximum)
 name=productos[pos_max]
 print ("{:^20} {:^20}".format (name, maximum))           #producto y precio
 del productos[pos_max]            #borrar el producto ya seleccionado
 del precios[pos_max]              #borrar el precio ya seleccionado 
 i+=1                              #
 