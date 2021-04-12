# Importar modulos
import pyodbc


# Configuracion de conexion a base de datos
server = 'lgalicialap'
database = 'python'
username = 'sa'
password = 'Sql.123'
conexion = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password
conexion = pyodbc.connect(conexion)
# cursor = conexion.cursor()
# cursor.execute("SELECT @@VERSION")
# resConexion = cursor.fetchone()
# print(resConexion)