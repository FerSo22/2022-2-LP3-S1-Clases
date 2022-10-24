import sqlite3

# Con el comando connect buscará la base de datos que tenga ese nombre, de lo contrario, lo creará
conexion = sqlite3.connect("bdbiblioteca.db")

lista_paises = [('Perú', 'A'),
                ('Argentina', 'A'),
                ('Venezuela', 'A'),
                ('Uruguay', 'A'),
                ('Paraguay', 'A'),
                ('USA', 'A')]

lista_editoriales = [('EIU', 'A'),
                     ('Macro', 'A'),
                     ('Bosch', 'A'),
                     ('Lima Sur', 'A'),
                     ('Colombus', 'A'),
                     ('Centro', 'A')]

lista_autores= [('Flor Cerdán', '25/10/1975'),
                ('Daniel Lévano', '17/01/1980'),
                ('Omar Peña', '15/10/1978'),
                ('César Zapata', '15/10/1960')]

lista_libros = [('Oracle 11g', 10, 2019, 50, 'A', 1, 1, 1),
                ('Sistemas Operativos', 14, 2016, 59, 'A', 1, 4, 3),
                ('Estructura de Datos', 6, 2018, 20, 'A', 2, 3, 3),
                ('Algoritmos con Python', 8, 2017, 70, 'A', 2, 2, 1),
                ('BI', 6, 1998, 50, 'A', 1, 4, 2),
                ('Ing. de Software', 9, 2000, 56, 'A', 3, 2, 4),
                ('Organizacion de PC', 9, 2016, 60, 'A', 7, 2, 1),
                ('Ensamblaje', 9, 2018, 50, 'A', 4, 4, 3)]

consulta_pais = """INSERT INTO 
           pais(nombre, estado) 
           VALUES(?, ?)
           """

consulta_editorial = """INSERT INTO 
           editorial(nombre, estado) 
           VALUES(?, ?)
           """

consulta_autor = """INSERT INTO 
           autor(nombre, f_nacimiento) 
           VALUES(?, ?)
           """

consulta_libro = """INSERT INTO 
           libro(titulo, cantidad, anio, precio, estado, idpais, ideditorial, idautor) 
           VALUES(?, ?, ?, ?, ?, ?, ?, ?)
           """

cursor = conexion.cursor()
cursor.executemany(consulta_pais, lista_paises)
cursor.executemany(consulta_editorial, lista_editoriales)
cursor.executemany(consulta_autor, lista_autores)
cursor.executemany(consulta_libro, lista_libros)

conexion.commit()
conexion.close()