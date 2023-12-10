import mysql.connector

class Database:
    """Clase para conectar con la BBDD y ejecutar las consultas."""

    def __init__(self, name):
        """Constructor de la clase."""
        self._conn = mysql.connector.connect(**name)
        self._cursor = self._conn.cursor(buffered=True)

    def create(self, table, category):
        sql = "INSERT INTO {}(valor1,valor2,valor3,valor4) VALUES ({},1,1,1) ".format(table, category)
        self._cursor.execute(sql)
        self._conn.commit()

    def get(self, id):
       
        pass

    def update(self, id, data):
       
        pass

    def delete(self, id):
        
        pass

    def close(self):
        """Cerrar la conexión con la BBDD."""
        self._conn.close()
        self._cursor.close()