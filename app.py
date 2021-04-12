# Importar Modulos
from flask import Flask, jsonify

# Instancia aplicacion
app = Flask(__name__)

# Importacion de apps
from apps.users import login
from db.conexion import conexion

# Routes

# Api principal
@app.route('/api')
def main():
    cursor = conexion.cursor()
    cursor.execute("SELECT @@VERSION")
    versionSqlServer = cursor.fetchone()
    return jsonify({
        'mensaje': 'Server API REST - Python/Flask is ONLINE',
        'versionSqlServer': versionSqlServer[0]
    })
    
    
# App user 
@app.route('/api/user/login')
def loginUser():
    return jsonify({'userLogin': login()})


# Ejecutar Aplicacion
if __name__ == '__main__':
    app.run(debug = True, port = 4000)