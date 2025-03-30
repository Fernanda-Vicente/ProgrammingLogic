productos=["peluche", "muñeca", "pelota", "carrito", "zapatos"]
precios= [40, 60, 25,30, 120]

minimum=max(precios)
pos=precios.index(minimum)
prod=productos[pos]
print(prod)

pos_productos=productos.index("pelota")
precio_pelota=precios[pos_productos]
print(precio_pelota)