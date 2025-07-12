class Libro:
    def __init__(self, titulo, autor, añodepublicacion, genero):
        self.titulo = titulo
        self.autor = autor
        self.añodepublicacion = añodepublicacion
        self.genero = genero

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.añodepublicacion}")
        print(f"Género: {self.genero}")
        print("-" * 30)

libro1 = Libro("El diario de Ana Frank", "Ana Frank", "1947", "Biografía")
libro2 = Libro("El código de Da Vinci", "Dan Brown", "2003", "Misterio")
libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "1605", "Novela")
libro4 = Libro("El principito", "Antoine de Saint", "1943", "Literatura infantil")
libro5 = Libro("El señor de los anillos", "J.R.R. Tolkien", "1954", "Fantasía")

libro1.mostrar_informacion()
libro2.mostrar_informacion()
libro3.mostrar_informacion()
libro4.mostrar_informacion()
libro5.mostrar_informacion()
