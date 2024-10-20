import seaborn as sns 
from random import randint
from PIL import Image, ImageColor
n=100
fondo=(0, 0, 255)
zona=Image.new('RGB', (n, n), color = fondo)
celda=zona.load()
k=25
color=sns.color_palette("Set3", k).as_hex()
for semilla in range(k):
    while True:
        columna=randint(0, n-1)
        fila=randint(0, n-1)
        if celda[columna, fila]==fondo:
            celda[columna, fila]==ImageColor.getrgb(color[semilla])
            break
visual=zona.resize((10*n, 10*n))
visual.show()
visual.save("p4p.png")