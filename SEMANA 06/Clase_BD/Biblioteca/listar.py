import sqlite3

# Con el comando connect buscará la base de datos que tenga ese nombre, de lo contrario, lo creará
conexion = sqlite3.connect("bdbiblioteca.db")
cursor = conexion.cursor()

consulta = """ SELECT * FROM LIBRO 
           ORDER BY TITULO
           """

cursor.execute(consulta)
libros = cursor.fetchall()

for libro in libros:
    print(libro)

conexion.close()