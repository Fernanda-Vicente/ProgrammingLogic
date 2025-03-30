import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-10,10,5)
y=x*np.sin(x)

plt.plot(x,y, color="red")
plt.xlabel("Intensidad")
plt.ylabel("Tiempo")
plt.title("Alumnos")
plt.show()