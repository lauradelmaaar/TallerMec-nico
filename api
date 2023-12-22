import os
import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database="taller_mecanico",
                            user="postgres",
                            password="Nicolasml01",
                            port=5432)
    return conn

@app.route('/tareas', methods=['GET', 'POST'])
def tareas():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM tarea")
        result = []
        for tarea in cursor.fetchall():
            result.append({
                'id_Tarea': tarea[0],
                'nombre_Servicio': tarea[1],
                'descripcion': tarea[2],
                'duracion': tarea[3],
                'coste': float(tarea[4])
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nueva_tarea = (
            request.form['nombre_Servicio'],
            request.form['descripcion'],
            request.form['duracion'],
            request.form['coste']
        )
        cursor.execute("INSERT INTO tarea (nombre_Servicio, descripcion, duracion, coste) VALUES (%s, %s, %s, %s)", nueva_tarea)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Tarea creada'}), 201
    
@app.route('/tareas/<id_Tarea>', methods=['GET'])
def get_tarea(id_Tarea):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM tarea where id_Tarea=%s", (id_Tarea,))
        result = []
        for tarea in cursor.fetchall():
            result.append({
                'id_Tarea': tarea[0],
                'nombre_Servicio': tarea[1],
                'descripcion': tarea[2],
                'duracion': tarea[3],
                'coste': float(tarea[4])
            })
        conn.close()
        return jsonify(result)

@app.route('/tareas/delete/<id_Tarea>', methods=['GET'])
def delete_Tarea(id_Tarea):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        #Comprobar si existe antes de hacer el delete:C
        cursor.execute("DELETE FROM tarea where id_Tarea=%s", (id_Tarea,))
        conn.commit()
        conn.close()
        return "Tarea Eliminada Correctamente"

@app.route('/tareas/update/<id_Tarea>', methods=['POST'])
def update_Tarea(id_Tarea):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        tarea = (
            request.form['nombre_Servicio'],
            request.form['descripcion'],
            request.form['duracion'],
            request.form['coste'],
            id_Tarea
        )
        cursor.execute("UPDATE tarea set nombre_Servicio=%s, descripcion=%s, duracion=%s, coste=%s where id_Tarea=%s", tarea)
        conn.commit()
        conn.close()
        return "Tarea Actualizada Correctamente"
      
if __name__ == '__main__':
    app.run(debug=True, port=8080)
