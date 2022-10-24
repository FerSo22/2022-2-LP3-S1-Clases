import sqlite3

conexion = sqlite3.connect("bdbiblioteca.db")

consulta = """ DELETE FROM editorial
                WHERE
                    ideditorial = 5
            """

cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()