# =====================================
# app.py – Aplicación Flask principal
# =====================================
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# ---------------------------
# CONFIGURACIÓN DE CONEXIÓN A MySQL
# ---------------------------
app.config['MYSQL_HOST'] = 'proyectowp.cy9nzcfau728.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Paulpoma151123'
app.config['MYSQL_DB'] = 'InversionesPaul'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

# ---------------------------
# RUTA PRINCIPAL - Muestra el formulario
# ---------------------------
@app.route('/')
def index():
    return render_template('index.html')

# ---------------------------
# RUTA PARA REGISTRAR USUARIOS
# ---------------------------
@app.route('/registrar', methods=['POST'])
def registrar():
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        correo = request.form['correo']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO usuarios (nombres, apellidos, correo, password) VALUES (%s, %s, %s, %s)",
                       (nombres, apellidos, correo, password))
        mysql.connection.commit()
        cursor.close()

        return redirect('/')

# ---------------------------
# INICIAR SERVIDOR
# ---------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

