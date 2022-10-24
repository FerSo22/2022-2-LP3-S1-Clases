import sqlite3

# Con el comando connect buscará la base de datos que tenga ese nombre, de lo contrario, lo creará
conexion = sqlite3.connect("bdbiblioteca.db")

consulta = """INSERT INTO 
           PAIS(nombre, estado) 
           VALUES('Brasil', 'A')
           """
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()

conexion.close()