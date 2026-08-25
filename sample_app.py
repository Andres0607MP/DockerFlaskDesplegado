from flask import Flask
from flask import request
from flask import render_template
import pymysql

sample = Flask(__name__)

@sample.route ("/")
def home():
	try:
		conn = pymysql.connect(host='db', user='root', password='sena123', database='082_db')
		conn.close()
		db_status = 'Conexion exitosa a la base de datos, prueba de CI/CD para despliegue continuo'
	except Exception as e:
		db_status = f'Error al conectar a la base de datos: {e}'

	return f"<h1>Bienvenido a mi aplicacion Flask</h1><h2>{db_status}</h2>"

if __name__ == "__main__":
	sample.run(debug=True, host='0.0.0.0', port=5050)
