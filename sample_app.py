from flask import Flask
from flask import request
from flask import render_template
import os
import pymysql

sample = Flask(__name__)

DB_HOST = os.environ.get('DB_HOST', 'db')
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
DB_NAME = os.environ.get('DB_NAME', '082_db')

@sample.route ("/")
def home():
	try:
		conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
		conn.close()
		db_status = 'Conexion exitosa a la base de datos, prueba de CI/CD para despliegue continuo'
	except Exception as e:
		db_status = f'Error al conectar a la base de datos: {e}'

	return f"<h1>Bienvenido a mi aplicacion Flask</h1><h2>{db_status}</h2>"

if __name__ == "__main__":
	flask_debug = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
	flask_host = os.environ.get('FLASK_RUN_HOST')
	sample.run(debug=flask_debug, host=flask_host, port=5050)
