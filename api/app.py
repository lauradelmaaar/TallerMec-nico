import os
import psycopg2
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database="taller_mecanico",
                            user="postgres",
                            password="Nicolasml01",
                            port=5432)
    return conn

@app.route('/comandas', methods=['GET', 'POST'])
def comandas():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Comanda")
        result = []
        for comanda in cursor.fetchall():
            result.append({
                'id_Comanda': comanda[0],
                'precio_Total': float(comanda[1])
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nueva_comanda = (
            request.form['precio_Total'],
        )
        cursor.execute("INSERT INTO Comanda (precio_Total) VALUES (%s)", nueva_comanda)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Comanda creada'}), 201
    
@app.route('/comandas/<id_Comanda>', methods=['GET'])
def get_comanda(id_Comanda):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Comanda WHERE id_Comanda=%s", (id_Comanda,))
        result = []
        for comanda in cursor.fetchall():
            result.append({
                'id_Comanda': comanda[0],
                'precio_Total': float(comanda[1])
            })
        conn.close()
        return jsonify(result)

@app.route('/comandas/delete/<id_Comanda>', methods=['GET'])
def delete_comanda(id_Comanda):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si la comanda existe
        cursor.execute("SELECT * FROM Comanda WHERE id_Comanda=%s", (id_Comanda,))
        comanda = cursor.fetchone()

        if comanda is None:
            conn.close()
            return jsonify({'error': 'La comanda no existe'}), 404

        # Si la comanda existe, proceder con la eliminación
        cursor.execute("DELETE FROM Comanda WHERE id_Comanda=%s", (id_Comanda,))
        conn.commit()
        conn.close()
        return "Comanda Eliminada Correctamente"

@app.route('/comandas/update/<id_Comanda>', methods=['POST'])
def update_comanda(id_Comanda):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Comprobar si la comanda existe
        cursor.execute("SELECT * FROM Comanda WHERE id_Comanda=%s", (id_Comanda,))
        comanda_existente = cursor.fetchone()

        if comanda_existente is None:
            conn.close()
            return jsonify({'error': 'La comanda no existe'}), 404

        # Si la comanda existe, proceder con la actualización
        nueva_comanda = (
            request.form['precio_Total'],
            id_Comanda
        )
        cursor.execute("UPDATE Comanda SET precio_Total=%s WHERE id_Comanda=%s", nueva_comanda)
        conn.commit()
        conn.close()
        return "Comanda Actualizada Correctamente"

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
        # Comprobar si la tarea existe
        cursor.execute("SELECT * FROM tarea WHERE id_Tarea=%s", (id_Tarea,))
        tarea = cursor.fetchone()

        if tarea is None:
            conn.close()
            return jsonify({'error': 'La tarea no existe'}), 404

        # Si la tarea existe, proceder con la eliminación
        cursor.execute("DELETE FROM tarea WHERE id_Tarea=%s", (id_Tarea,))
        conn.commit()
        conn.close()
        return "Tarea Eliminada Correctamente"

@app.route('/tareas/update/<id_Tarea>', methods=['POST'])
def update_Tarea(id_Tarea):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Comprobar si la tarea existe
        cursor.execute("SELECT * FROM tarea WHERE id_Tarea=%s", (id_Tarea,))
        tarea_existente = cursor.fetchone()

        if tarea_existente is None:
            conn.close()
            return jsonify({'error': 'La tarea no existe'}), 404

        # Si la tarea existe, proceder con la actualización
        nueva_tarea = (
            request.form['nombre_Servicio'],
            request.form['descripcion'],
            request.form['duracion'],
            request.form['coste'],
            id_Tarea
        )
        cursor.execute("UPDATE tarea SET nombre_Servicio=%s, descripcion=%s, duracion=%s, coste=%s WHERE id_Tarea=%s", nueva_tarea)
        conn.commit()
        conn.close()
        return "Tarea Actualizada Correctamente"

@app.route('/piezas', methods=['GET', 'POST'])
def piezas():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Pieza")
        result = []
        for pieza in cursor.fetchall():
            result.append({
                'id_Pieza': pieza[0],
                'nombre_Producto': pieza[1],
                'precio': float(pieza[2]),
                'unidades': pieza[3],
                'num_Fabricante': pieza[4]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nueva_pieza = (
            request.form['nombre_Producto'],
            request.form['precio'],
            request.form['unidades'],
            request.form['num_Fabricante']
        )
        cursor.execute("INSERT INTO Pieza (nombre_Producto, precio, unidades, num_Fabricante) VALUES (%s, %s, %s, %s)", nueva_pieza)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Pieza creada'}), 201
    
@app.route('/piezas/<id_Pieza>', methods=['GET'])
def get_pieza(id_Pieza):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Pieza WHERE id_Pieza=%s", (id_Pieza,))
        result = []
        for pieza in cursor.fetchall():
            result.append({
                'id_Pieza': pieza[0],
                'nombre_Producto': pieza[1],
                'precio': float(pieza[2]),
                'unidades': pieza[3],
                'num_Fabricante': pieza[4]
            })
        conn.close()
        return jsonify(result)

@app.route('/piezas/delete/<id_Pieza>', methods=['GET'])
def delete_pieza(id_Pieza):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si la pieza existe
        cursor.execute("SELECT * FROM Pieza WHERE id_Pieza=%s", (id_Pieza,))
        pieza = cursor.fetchone()

        if pieza is None:
            conn.close()
            return jsonify({'error': 'La pieza no existe'}), 404

        # Si la pieza existe, proceder con la eliminación
        cursor.execute("DELETE FROM Pieza WHERE id_Pieza=%s", (id_Pieza,))
        conn.commit()
        conn.close()
        return "Pieza Eliminada Correctamente"

@app.route('/piezas/update/<id_Pieza>', methods=['POST'])
def update_pieza(id_Pieza):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Comprobar si la pieza existe
        cursor.execute("SELECT * FROM Pieza WHERE id_Pieza=%s", (id_Pieza,))
        pieza_existente = cursor.fetchone()

        if pieza_existente is None:
            conn.close()
            return jsonify({'error': 'La pieza no existe'}), 404

        # Si la pieza existe, proceder con la actualización
        nueva_pieza = (
            request.form['nombre_Producto'],
            request.form['precio'],
            request.form['unidades'],
            request.form['num_Fabricante'],
            id_Pieza
        )
        cursor.execute("UPDATE Pieza SET nombre_Producto=%s, precio=%s, unidades=%s, num_Fabricante=%s WHERE id_Pieza=%s", nueva_pieza)
        conn.commit()
        conn.close()
        return "Pieza Actualizada Correctamente"

@app.route('/consumibles', methods=['GET', 'POST'])
def consumibles():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Consumible")
        result = []
        for consumible in cursor.fetchall():
            result.append({
                'id_Consumible': consumible[0],
                'nombre': consumible[1],
                'precio': float(consumible[2]),
                'litros_por_unidad': float(consumible[3])
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nuevo_consumible = (
            request.form['nombre'],
            request.form['precio'],
            request.form['litros_por_unidad']
        )
        cursor.execute("INSERT INTO Consumible (nombre, precio, litros_por_unidad) VALUES (%s, %s, %s)", nuevo_consumible)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Consumible creado'}), 201
    
@app.route('/consumibles/<id_Consumible>', methods=['GET'])
def get_consumible(id_Consumible):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Consumible WHERE id_Consumible=%s", (id_Consumible,))
        result = []
        for consumible in cursor.fetchall():
            result.append({
                'id_Consumible': consumible[0],
                'nombre': consumible[1],
                'precio': float(consumible[2]),
                'litros_por_unidad': float(consumible[3])
            })
        conn.close()
        return jsonify(result)

@app.route('/consumibles/delete/<id_Consumible>', methods=['GET'])
def delete_consumible(id_Consumible):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si el consumible existe
        cursor.execute("SELECT * FROM Consumible WHERE id_Consumible=%s", (id_Consumible,))
        consumible = cursor.fetchone()

        if consumible is None:
            conn.close()
            return jsonify({'error': 'El consumible no existe'}), 404

        # Si el consumible existe, proceder con la eliminación
        cursor.execute("DELETE FROM Consumible WHERE id_Consumible=%s", (id_Consumible,))
        conn.commit()
        conn.close()
        return "Consumible Eliminado Correctamente"

@app.route('/consumibles/update/<id_Consumible>', methods=['POST'])
def update_consumible(id_Consumible):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Comprobar si el consumible existe
        cursor.execute("SELECT * FROM Consumible WHERE id_Consumible=%s", (id_Consumible,))
        consumible_existente = cursor.fetchone()

        if consumible_existente is None:
            conn.close()
            return jsonify({'error': 'El consumible no existe'}), 404

        # Si el consumible existe, proceder con la actualización
        nuevo_consumible = (
            request.form['nombre'],
            request.form['precio'],
            request.form['litros_por_unidad'],
            id_Consumible
        )
        cursor.execute("UPDATE Consumible SET nombre=%s, precio=%s, litros_por_unidad=%s WHERE id_Consumible=%s", nuevo_consumible)
        conn.commit()
        conn.close()
        return "Consumible Actualizado Correctamente"

@app.route('/facturas', methods=['GET', 'POST'])
def facturas():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Factura")
        result = []
        for factura in cursor.fetchall():
            result.append({
                'num_Referencia': factura[0],
                'porcentaje_Impuestos': float(factura[1]),
                'coste_Total': float(factura[2]),
                'fecha_Emision': factura[3].strftime("%Y-%m-%d")
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nueva_factura = (
            request.form['porcentaje_Impuestos'],
            request.form['coste_Total'],
            request.form['fecha_Emision']
        )
        cursor.execute("INSERT INTO Factura (porcentaje_Impuestos, coste_Total, fecha_Emision) VALUES (%s, %s, %s)", nueva_factura)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Factura creada'}), 201
    
@app.route('/facturas/<num_Referencia>', methods=['GET'])
def get_factura(num_Referencia):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Factura WHERE num_Referencia=%s", (num_Referencia,))
        result = []
        for factura in cursor.fetchall():
            result.append({
                'num_Referencia': factura[0],
                'porcentaje_Impuestos': float(factura[1]),
                'coste_Total': float(factura[2]),
                'fecha_Emision': factura[3].strftime("%Y-%m-%d")
            })
        conn.close()
        return jsonify(result)

@app.route('/facturas/delete/<num_Referencia>', methods=['GET'])
def delete_factura(num_Referencia):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si la factura existe
        cursor.execute("SELECT * FROM Factura WHERE num_Referencia=%s", (num_Referencia,))
        factura = cursor.fetchone()

        if factura is None:
            conn.close()
            return jsonify({'error': 'La factura no existe'}), 404

        # Si la factura existe, proceder con la eliminación
        cursor.execute("DELETE FROM Factura WHERE num_Referencia=%s", (num_Referencia,))
        conn.commit()
        conn.close()
        return "Factura Eliminada Correctamente"

@app.route('/facturas/update/<num_Referencia>', methods=['POST'])
def update_factura(num_Referencia):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Comprobar si la factura existe
        cursor.execute("SELECT * FROM Factura WHERE num_Referencia=%s", (num_Referencia,))
        factura_existente = cursor.fetchone()

        if factura_existente is None:
            conn.close()
            return jsonify({'error': 'La factura no existe'}), 404

        # Si la factura existe, proceder con la actualización
        nueva_factura = (
            request.form['porcentaje_Impuestos'],
            request.form['coste_Total'],
            request.form['fecha_Emision'],
            num_Referencia
        )
        cursor.execute("UPDATE Factura SET porcentaje_Impuestos=%s, coste_Total=%s, fecha_Emision=%s WHERE num_Referencia=%s", nueva_factura)
        conn.commit()
        conn.close()
        return "Factura Actualizada Correctamente"

@app.route('/empleados', methods=['GET', 'POST'])
def empleados():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Empleado")
        result = []
        for empleado in cursor.fetchall():
            result.append({
                'dni': empleado[0],
                'nombre': empleado[1],
                'turno': empleado[2],
                'direccion': empleado[3],
                'telefono': empleado[4],
                'email': empleado[5],
                'dni_encargado': empleado[6]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nuevo_empleado = (
            request.form['dni'],
            request.form['nombre'],
            request.form['turno'],
            request.form['direccion'],
            request.form['telefono'],
            request.form['email'],
            request.form['dni_encargado']
        )
        cursor.execute("INSERT INTO Empleado (dni, nombre, turno, direccion, telefono, email, dni_encargado) VALUES (%s, %s, %s, %s, %s, %s, %s)", nuevo_empleado)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Empleado creado'}), 201
    
@app.route('/empleados/<dni>', methods=['GET'])
def get_empleado(dni):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Empleado WHERE dni=%s", (dni,))
        result = []
        for empleado in cursor.fetchall():
            result.append({
                'dni': empleado[0],
                'nombre': empleado[1],
                'turno': empleado[2],
                'direccion': empleado[3],
                'telefono': empleado[4],
                'email': empleado[5],
                'dni_encargado': empleado[6]
            })
        conn.close()
        return jsonify(result)

@app.route('/empleados/delete/<dni>', methods=['GET'])
def delete_empleado(dni):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si el empleado existe
        cursor.execute("SELECT * FROM Empleado WHERE dni=%s", (dni,))
        empleado = cursor.fetchone()

        if empleado is None:
            conn.close()
            return jsonify({'error': 'El empleado no existe'}), 404

        # Si el empleado existe, proceder con la eliminación
        cursor.execute("DELETE FROM Empleado WHERE dni=%s", (dni,))
        conn.commit()
        conn.close()
        return "Empleado Eliminado Correctamente"

@app.route('/empleados/update/<dni>', methods=['POST'])
def update_empleado(dni):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Comprobar si el empleado existe
        cursor.execute("SELECT * FROM Empleado WHERE dni=%s", (dni,))
        empleado_existente = cursor.fetchone()

        if empleado_existente is None:
            conn.close()
            return jsonify({'error': 'El empleado no existe'}), 404

        # Si el empleado existe, proceder con la actualización
        nuevo_empleado = (
            request.form['dni'],
            request.form['nombre'],
            request.form['turno'],
            request.form['direccion'],
            request.form['telefono'],
            request.form['email'],
            request.form['dni_encargado'],
            dni
        )
        cursor.execute("UPDATE Empleado SET dni=%s, nombre=%s, turno=%s, direccion=%s, telefono=%s, email=%s, dni_encargado=%s WHERE dni=%s", nuevo_empleado)
        conn.commit()
        conn.close()
        return "Empleado Actualizado Correctamente"

@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Cliente")
        result = []
        for cliente in cursor.fetchall():
            result.append({
                'dni': cliente[0],
                'nombre': cliente[1],
                'direccion': cliente[2],
                'telefono': cliente[3],
                'email': cliente[4]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nuevo_cliente = (
            request.form['dni'],
            request.form['nombre'],
            request.form['direccion'],
            request.form['telefono'],
            request.form['email']
        )
        cursor.execute("INSERT INTO Cliente (dni, nombre, direccion, telefono, email) VALUES (%s, %s, %s, %s, %s)", nuevo_cliente)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Cliente creado'}), 201
    
@app.route('/clientes/<dni>', methods=['GET'])
def get_cliente(dni):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Cliente WHERE dni=%s", (dni,))
        result = []
        for cliente in cursor.fetchall():
            result.append({
                'dni': cliente[0],
                'nombre': cliente[1],
                'direccion': cliente[2],
                'telefono': cliente[3],
                'email': cliente[4]
            })
        conn.close()
        return jsonify(result)

@app.route('/clientes/delete/<dni>', methods=['GET'])
def delete_cliente(dni):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si el cliente existe
        cursor.execute("SELECT * FROM Cliente WHERE dni=%s", (dni,))
        cliente = cursor.fetchone()

        if cliente is None:
            conn.close()
            return jsonify({'error': 'El cliente no existe'}), 404

        # Si el cliente existe, proceder con la eliminación
        cursor.execute("DELETE FROM Cliente WHERE dni=%s", (dni,))
        conn.commit()
        conn.close()
        return "Cliente Eliminado Correctamente"

@app.route('/clientes/update/<dni>', methods=['POST'])
def update_cliente(dni):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Comprobar si el cliente existe
        cursor.execute("SELECT * FROM Cliente WHERE dni=%s", (dni,))
        cliente_existente = cursor.fetchone()

        if cliente_existente is None:
            conn.close()
            return jsonify({'error': 'El cliente no existe'}), 404

        # Si el cliente existe, proceder con la actualización
        nuevo_cliente = (
            request.form['dni'],
            request.form['nombre'],
            request.form['direccion'],
            request.form['telefono'],
            request.form['email'],
            dni
        )
        cursor.execute("UPDATE Cliente SET dni=%s, nombre=%s, direccion=%s, telefono=%s, email=%s WHERE dni=%s", nuevo_cliente)
        conn.commit()
        conn.close()
        return "Cliente Actualizado Correctamente"

@app.route('/solicitudes_cita', methods=['GET', 'POST'])
def solicitudes_cita():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM SolicitudCita")
        result = []
        for solicitud_cita in cursor.fetchall():
            result.append({
                'fecha': solicitud_cita[0].strftime("%Y-%m-%d"),
                'hora': str(solicitud_cita[1]),
                'num_Referencia': solicitud_cita[2],
                'dni_cliente': solicitud_cita[3]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nueva_solicitud_cita = (
            request.form['fecha'],
            request.form['hora'],
            request.form['dni_cliente']
        )
        cursor.execute("INSERT INTO SolicitudCita (fecha, hora, dni_cliente) VALUES (%s, %s, %s)", nueva_solicitud_cita)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Solicitud de cita creada'}), 201
    
@app.route('/solicitudes_cita/<num_Referencia>', methods=['GET'])
def get_solicitud_cita(num_Referencia):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM SolicitudCita WHERE num_Referencia=%s", (num_Referencia,))
        result = []
        for solicitud_cita in cursor.fetchall():
            result.append({
                'fecha': solicitud_cita[0].strftime("%Y-%m-%d"),
                'hora': str(solicitud_cita[1]),
                'num_Referencia': solicitud_cita[2],
                'dni_cliente': solicitud_cita[3]
            })
        conn.close()
        return jsonify(result)

@app.route('/solicitudes_cita/delete/<num_Referencia>', methods=['GET'])
def delete_solicitud_cita(num_Referencia):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si la solicitud de cita existe
        cursor.execute("SELECT * FROM SolicitudCita WHERE num_Referencia=%s", (num_Referencia,))
        solicitud_cita = cursor.fetchone()

        if solicitud_cita is None:
            conn.close()
            return jsonify({'error': 'La solicitud de cita no existe'}), 404

        # Si la solicitud de cita existe, proceder con la eliminación
        cursor.execute("DELETE FROM SolicitudCita WHERE num_Referencia=%s", (num_Referencia,))
        conn.commit()
        conn.close()
        return "Solicitud de Cita Eliminada Correctamente"

@app.route('/solicitudes_cita/update/<num_Referencia>', methods=['POST'])
def update_solicitud_cita(num_Referencia):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Comprobar si la solicitud de cita existe
        cursor.execute("SELECT * FROM SolicitudCita WHERE num_Referencia=%s", (num_Referencia,))
        solicitud_cita_existente = cursor.fetchone()

        if solicitud_cita_existente is None:
            conn.close()
            return jsonify({'error': 'La solicitud de cita no existe'}), 404

        # Si la solicitud de cita existe, proceder con la actualización
        nueva_solicitud_cita = (
            request.form['fecha'],
            request.form['hora'],
            request.form['dni_cliente'],
            num_Referencia
        )
        cursor.execute("UPDATE SolicitudCita SET fecha=%s, hora=%s, dni_cliente=%s WHERE num_Referencia=%s", nueva_solicitud_cita)
        conn.commit()
        conn.close()
        return "Solicitud de Cita Actualizada Correctamente"

@app.route('/marcas', methods=['GET', 'POST'])
def marcas():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Marca")
        result = []
        for marca in cursor.fetchall():
            result.append({
                'id_Marca': marca[0],
                'nombre': marca[1]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nueva_marca = (
            request.form['nombre']
        )
        cursor.execute("INSERT INTO Marca (nombre) VALUES (%s)", (nueva_marca,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Marca creada'}), 201
    
@app.route('/marcas/<id_Marca>', methods=['GET'])
def get_marca(id_Marca):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Marca WHERE id_Marca=%s", (id_Marca,))
        result = []
        for marca in cursor.fetchall():
            result.append({
                'id_Marca': marca[0],
                'nombre': marca[1]
            })
        conn.close()
        return jsonify(result)

@app.route('/marcas/delete/<id_Marca>', methods=['GET'])
def delete_marca(id_Marca):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si la marca existe
        cursor.execute("SELECT * FROM Marca WHERE id_Marca=%s", (id_Marca,))
        marca = cursor.fetchone()

        if marca is None:
            conn.close()
            return jsonify({'error': 'La marca no existe'}), 404

        # Si la marca existe, proceder con la eliminación
        cursor.execute("DELETE FROM Marca WHERE id_Marca=%s", (id_Marca,))
        conn.commit()
        conn.close()
        return "Marca Eliminada Correctamente"

@app.route('/marcas/update/<id_Marca>', methods=['POST'])
def update_marca(id_Marca):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Comprobar si la marca existe
        cursor.execute("SELECT * FROM Marca WHERE id_Marca=%s", (id_Marca,))
        marca_existente = cursor.fetchone()

        if marca_existente is None:
            conn.close()
            return jsonify({'error': 'La marca no existe'}), 404

        # Si la marca existe, proceder con la actualización
        nueva_marca = (
            request.form['nombre'],
            id_Marca
        )
        cursor.execute("UPDATE Marca SET nombre=%s WHERE id_Marca=%s", nueva_marca)
        conn.commit()
        conn.close()
        return "Marca Actualizada Correctamente"

@app.route('/modelos', methods=['GET', 'POST'])
def modelos():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Modelo")
        result = []
        for modelo in cursor.fetchall():
            result.append({
                'id_Modelo': modelo[0],
                'anyo': modelo[1],
                'nombre': modelo[2],
                'id_Marca': modelo[3]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nuevo_modelo = (
            request.form['anyo'],
            request.form['nombre'],
            request.form['id_Marca']
        )
        cursor.execute("INSERT INTO Modelo (anyo, nombre, id_Marca) VALUES (%s, %s, %s)", nuevo_modelo)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Modelo creado'}), 201
    
@app.route('/modelos/<id_Modelo>', methods=['GET'])
def get_modelo(id_Modelo):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Modelo WHERE id_Modelo=%s", (id_Modelo,))
        result = []
        for modelo in cursor.fetchall():
            result.append({
                'id_Modelo': modelo[0],
                'anyo': modelo[1],
                'nombre': modelo[2],
                'id_Marca': modelo[3]
            })
        conn.close()
        return jsonify(result)

@app.route('/modelos/delete/<id_Modelo>', methods=['GET'])
def delete_modelo(id_Modelo):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si el modelo existe
        cursor.execute("SELECT * FROM Modelo WHERE id_Modelo=%s", (id_Modelo,))
        modelo = cursor.fetchone()

        if modelo is None:
            conn.close()
            return jsonify({'error': 'El modelo no existe'}), 404

        # Si el modelo existe, proceder con la eliminación
        cursor.execute("DELETE FROM Modelo WHERE id_Modelo=%s", (id_Modelo,))
        conn.commit()
        conn.close()
        return "Modelo Eliminado Correctamente"

@app.route('/modelos/update/<id_Modelo>', methods=['POST'])
def update_modelo(id_Modelo):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Comprobar si el modelo existe
        cursor.execute("SELECT * FROM Modelo WHERE id_Modelo=%s", (id_Modelo,))
        modelo_existente = cursor.fetchone()

        if modelo_existente is None:
            conn.close()
            return jsonify({'error': 'El modelo no existe'}), 404

        # Si el modelo existe, proceder con la actualización
        nuevo_modelo = (
            request.form['anyo'],
            request.form['nombre'],
            request.form['id_Marca'],
            id_Modelo
        )
        cursor.execute("UPDATE Modelo SET anyo=%s, nombre=%s, id_Marca=%s WHERE id_Modelo=%s", nuevo_modelo)
        conn.commit()
        conn.close()
        return "Modelo Actualizado Correctamente"

@app.route('/vehiculos', methods=['GET', 'POST'])
def vehiculos():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Vehiculo")
        result = []
        for vehiculo in cursor.fetchall():
            result.append({
                'matricula': vehiculo[0],
                'num_Bastidor': vehiculo[1],
                'anyo_Compra': vehiculo[2],
                'anyo_Fabricacion': vehiculo[3],
                'tipo_Vehiculo': vehiculo[4],
                'num_KM': vehiculo[5],
                'dni_cliente': vehiculo[6],
                'id_Modelo': vehiculo[7]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nuevo_vehiculo = (
            request.form['matricula'],
            request.form['num_Bastidor'],
            request.form['anyo_Compra'],
            request.form['anyo_Fabricacion'],
            request.form['tipo_Vehiculo'],
            request.form['num_KM'],
            request.form['dni_cliente'],
            request.form['id_Modelo']
        )
        cursor.execute("INSERT INTO Vehiculo (matricula, num_Bastidor, anyo_Compra, anyo_Fabricacion, tipo_Vehiculo, num_KM, dni_cliente, id_Modelo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", nuevo_vehiculo)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Vehículo creado'}), 201
    
@app.route('/vehiculos/<matricula>', methods=['GET'])
def get_vehiculo(matricula):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Vehiculo WHERE matricula=%s", (matricula,))
        result = []
        for vehiculo in cursor.fetchall():
            result.append({
                'matricula': vehiculo[0],
                'num_Bastidor': vehiculo[1],
                'anyo_Compra': vehiculo[2],
                'anyo_Fabricacion': vehiculo[3],
                'tipo_Vehiculo': vehiculo[4],
                'num_KM': vehiculo[5],
                'dni_cliente': vehiculo[6],
                'id_Modelo': vehiculo[7]
            })
        conn.close()
        return jsonify(result)

@app.route('/vehiculos/delete/<matricula>', methods=['GET'])
def delete_vehiculo(matricula):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si el vehículo existe
        cursor.execute("SELECT * FROM Vehiculo WHERE matricula=%s", (matricula,))
        vehiculo = cursor.fetchone()

        if vehiculo is None:
            conn.close()
            return jsonify({'error': 'El vehículo no existe'}), 404

        # Si el vehículo existe, proceder con la eliminación
        cursor.execute("DELETE FROM Vehiculo WHERE matricula=%s", (matricula,))
        conn.commit()
        conn.close()
        return "Vehículo Eliminado Correctamente"

@app.route('/vehiculos/update/<matricula>', methods=['POST'])
def update_vehiculo(matricula):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Comprobar si el vehículo existe
        cursor.execute("SELECT * FROM Vehiculo WHERE matricula=%s", (matricula,))
        vehiculo_existente = cursor.fetchone()

        if vehiculo_existente is None:
            conn.close()
            return jsonify({'error': 'El vehículo no existe'}), 404

        # Si el vehículo existe, proceder con la actualización
        nuevo_vehiculo = (
            request.form['matricula'],
            request.form['num_Bastidor'],
            request.form['anyo_Compra'],
            request.form['anyo_Fabricacion'],
            request.form['tipo_Vehiculo'],
            request.form['num_KM'],
            request.form['dni_cliente'],
            request.form['id_Modelo'],
            matricula
        )
        cursor.execute("UPDATE Vehiculo SET matricula=%s, num_Bastidor=%s, anyo_Compra=%s, anyo_Fabricacion=%s, tipo_Vehiculo=%s, num_KM=%s, dni_cliente=%s, id_Modelo=%s WHERE matricula=%s", nuevo_vehiculo)
        conn.commit()
        conn.close()
        return "Vehículo Actualizado Correctamente"

@app.route('/proveedores', methods=['GET', 'POST'])
def proveedores():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Proveedor")
        result = []
        for proveedor in cursor.fetchall():
            result.append({
                'codigo': proveedor[0],
                'nombre': proveedor[1],
                'direccion_CP': proveedor[2],
                'direccion_Calle': proveedor[3]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nuevo_proveedor = (
            request.form['codigo'],
            request.form['nombre'],
            request.form['direccion_CP'],
            request.form['direccion_Calle']
        )
        cursor.execute("INSERT INTO Proveedor (codigo, nombre, direccion_CP, direccion_Calle) VALUES (%s, %s, %s, %s)", nuevo_proveedor)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Proveedor creado'}), 201
    
@app.route('/proveedores/<codigo>', methods=['GET'])
def get_proveedor(codigo):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Proveedor WHERE codigo=%s", (codigo,))
        result = []
        for proveedor in cursor.fetchall():
            result.append({
                'codigo': proveedor[0],
                'nombre': proveedor[1],
                'direccion_CP': proveedor[2],
                'direccion_Calle': proveedor[3]
            })
        conn.close()
        return jsonify(result)

@app.route('/proveedores/delete/<codigo>', methods=['GET'])
def delete_proveedor(codigo):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si el proveedor existe
        cursor.execute("SELECT * FROM Proveedor WHERE codigo=%s", (codigo,))
        proveedor = cursor.fetchone()

        if proveedor is None:
            conn.close()
            return jsonify({'error': 'El proveedor no existe'}), 404

        # Si el proveedor existe, proceder con la eliminación
        cursor.execute("DELETE FROM Proveedor WHERE codigo=%s", (codigo,))
        conn.commit()
        conn.close()
        return "Proveedor Eliminado Correctamente"

@app.route('/proveedores/update/<codigo>', methods=['POST'])
def update_proveedor(codigo):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Comprobar si el proveedor existe
        cursor.execute("SELECT * FROM Proveedor WHERE codigo=%s", (codigo,))
        proveedor_existente = cursor.fetchone()

        if proveedor_existente is None:
            conn.close()
            return jsonify({'error': 'El proveedor no existe'}), 404

        # Si el proveedor existe, proceder con la actualización
        nuevo_proveedor = (
            request.form['codigo'],
            request.form['nombre'],
            request.form['direccion_CP'],
            request.form['direccion_Calle']
        )
        cursor.execute("UPDATE Proveedor SET codigo=%s, nombre=%s, direccion_CP=%s, direccion_Calle=%s WHERE codigo=%s", nuevo_proveedor)
        conn.commit()
        conn.close()
        return "Proveedor Actualizado Correctamente"

@app.route('/revisiones', methods=['GET', 'POST'])
def revisiones():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Revision")
        result = []
        for revision in cursor.fetchall():
            result.append({
                'codigo_Revision': revision[0],
                'fecha': revision[1].strftime("%Y-%m-%d"),
                'hora': str(revision[2]),
                'periodica': revision[3],
                'dni_empleado': revision[4]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nueva_revision = (
            request.form['codigo_Revision'],
            request.form['fecha'],
            request.form['hora'],
            request.form['periodica'],
            request.form['dni_empleado']
        )
        cursor.execute("INSERT INTO Revision (codigo_Revision, fecha, hora, periodica, dni_empleado) VALUES (%s, %s, %s, %s, %s)", nueva_revision)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Revisión creada'}), 201
    
@app.route('/revisiones/<codigo_Revision>', methods=['GET'])
def get_revision(codigo_Revision):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Revision WHERE codigo_Revision=%s", (codigo_Revision,))
        result = []
        for revision in cursor.fetchall():
            result.append({
                'codigo_Revision': revision[0],
                'fecha': revision[1].strftime("%Y-%m-%d"),
                'hora': str(revision[2]),
                'periodica': revision[3],
                'dni_empleado': revision[4]
            })
        conn.close()
        return jsonify(result)

@app.route('/revisiones/delete/<codigo_Revision>', methods=['GET'])
def delete_revision(codigo_Revision):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si la revisión existe
        cursor.execute("SELECT * FROM Revision WHERE codigo_Revision=%s", (codigo_Revision,))
        revision = cursor.fetchone()

        if revision is None:
            conn.close()
            return jsonify({'error': 'La revisión no existe'}), 404

        # Si la revisión existe, proceder con la eliminación
        cursor.execute("DELETE FROM Revision WHERE codigo_Revision=%s", (codigo_Revision,))
        conn.commit()
        conn.close()
        return "Revisión Eliminada Correctamente"

@app.route('/revisiones/update/<codigo_Revision>', methods=['POST'])
def update_revision(codigo_Revision):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Comprobar si la revisión existe
        cursor.execute("SELECT * FROM Revision WHERE codigo_Revision=%s", (codigo_Revision,))
        revision_existente = cursor.fetchone()

        if revision_existente is None:
            conn.close()
            return jsonify({'error': 'La revisión no existe'}), 404

        # Si la revisión existe, proceder con la actualización
        nueva_revision = (
            request.form['codigo_Revision'],
            request.form['fecha'],
            request.form['hora'],
            request.form['periodica'],
            request.form['dni_empleado'],
            codigo_Revision
        )
        cursor.execute("UPDATE Revision SET codigo_Revision=%s, fecha=%s, hora=%s, periodica=%s, dni_empleado=%s WHERE codigo_Revision=%s", nueva_revision)
        conn.commit()
        conn.close()
        return "Revisión Actualizada Correctamente"

@app.route('/problemas', methods=['GET', 'POST'])
def problemas():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Problema")
        result = []
        for problema in cursor.fetchall():
            result.append({
                'id_Problema': problema[0],
                'descripcion': problema[1],
                'codigo_Revision': problema[2]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nuevo_problema = (
            request.form['descripcion'],
            request.form['codigo_Revision']
        )
        cursor.execute("INSERT INTO Problema (descripcion, codigo_Revision) VALUES (%s, %s)", nuevo_problema)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Problema creado'}), 201
    
@app.route('/problemas/<id_Problema>', methods=['GET'])
def get_problema(id_Problema):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Problema WHERE id_Problema=%s", (id_Problema,))
        result = []
        for problema in cursor.fetchall():
            result.append({
                'id_Problema': problema[0],
                'descripcion': problema[1],
                'codigo_Revision': problema[2]
            })
        conn.close()
        return jsonify(result)

@app.route('/problemas/delete/<id_Problema>', methods=['GET'])
def delete_problema(id_Problema):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si el problema existe
        cursor.execute("SELECT * FROM Problema WHERE id_Problema=%s", (id_Problema,))
        problema = cursor.fetchone()

        if problema is None:
            conn.close()
            return jsonify({'error': 'El problema no existe'}), 404

        # Si el problema existe, proceder con la eliminación
        cursor.execute("DELETE FROM Problema WHERE id_Problema=%s", (id_Problema,))
        conn.commit()
        conn.close()
        return "Problema Eliminado Correctamente"

@app.route('/problemas/update/<id_Problema>', methods=['POST'])
def update_problema(id_Problema):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Comprobar si el problema existe
        cursor.execute("SELECT * FROM Problema WHERE id_Problema=%s", (id_Problema,))
        problema_existente = cursor.fetchone()

        if problema_existente is None:
            conn.close()
            return jsonify({'error': 'El problema no existe'}), 404

        # Si el problema existe, proceder con la actualización
        nuevo_problema = (
            request.form['descripcion'],
            request.form['codigo_Revision'],
            id_Problema
        )
        cursor.execute("UPDATE Problema SET descripcion=%s, codigo_Revision=%s WHERE id_Problema=%s", nuevo_problema)
        conn.commit()
        conn.close()
        return "Problema Actualizado Correctamente"

@app.route('/modelos_tareas', methods=['GET', 'POST'])
def modelos_tareas():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Modelo_Tarea")
        result = []
        for modelo_tarea in cursor.fetchall():
            result.append({
                'id_Modelo': modelo_tarea[0],
                'id_Tarea': modelo_tarea[1]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nueva_relacion = (
            request.form['id_Modelo'],
            request.form['id_Tarea']
        )
        cursor.execute("INSERT INTO Modelo_Tarea (id_Modelo, id_Tarea) VALUES (%s, %s)", nueva_relacion)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Relación Modelo-Tarea creada'}), 201
    
@app.route('/modelos_tareas/<id_Modelo>/<id_Tarea>', methods=['GET'])
def get_modelo_tarea(id_Modelo, id_Tarea):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Modelo_Tarea WHERE id_Modelo=%s AND id_Tarea=%s", (id_Modelo, id_Tarea))
        result = []
        for modelo_tarea in cursor.fetchall():
            result.append({
                'id_Modelo': modelo_tarea[0],
                'id_Tarea': modelo_tarea[1]
            })
        conn.close()
        return jsonify(result)

@app.route('/modelos_tareas/delete/<id_Modelo>/<id_Tarea>', methods=['GET'])
def delete_modelo_tarea(id_Modelo, id_Tarea):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si la relación Modelo-Tarea existe
        cursor.execute("SELECT * FROM Modelo_Tarea WHERE id_Modelo=%s AND id_Tarea=%s", (id_Modelo, id_Tarea))
        modelo_tarea = cursor.fetchone()

        if modelo_tarea is None:
            conn.close()
            return jsonify({'error': 'La relación Modelo-Tarea no existe'}), 404

        # Si la relación existe, proceder con la eliminación
        cursor.execute("DELETE FROM Modelo_Tarea WHERE id_Modelo=%s AND id_Tarea=%s", (id_Modelo, id_Tarea))
        conn.commit()
        conn.close()
        return "Relación Modelo-Tarea Eliminada Correctamente"

@app.route('/revisiones_tareas', methods=['GET', 'POST'])
def revisiones_tareas():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Revision_Tarea")
        result = []
        for revision_tarea in cursor.fetchall():
            result.append({
                'id_Revision': revision_tarea[0],
                'id_Tarea': revision_tarea[1]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nueva_relacion = (
            request.form['id_Revision'],
            request.form['id_Tarea']
        )
        cursor.execute("INSERT INTO Revision_Tarea (id_Revision, id_Tarea) VALUES (%s, %s)", nueva_relacion)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Relación Revision-Tarea creada'}), 201
    
@app.route('/revisiones_tareas/<id_Revision>/<id_Tarea>', methods=['GET'])
def get_revision_tarea(id_Revision, id_Tarea):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Revision_Tarea WHERE id_Revision=%s AND id_Tarea=%s", (id_Revision, id_Tarea))
        result = []
        for revision_tarea in cursor.fetchall():
            result.append({
                'id_Revision': revision_tarea[0],
                'id_Tarea': revision_tarea[1]
            })
        conn.close()
        return jsonify(result)

@app.route('/revisiones_tareas/delete/<id_Revision>/<id_Tarea>', methods=['GET'])
def delete_revision_tarea(id_Revision, id_Tarea):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si la relación Revision-Tarea existe
        cursor.execute("SELECT * FROM Revision_Tarea WHERE id_Revision=%s AND id_Tarea=%s", (id_Revision, id_Tarea))
        revision_tarea = cursor.fetchone()

        if revision_tarea is None:
            conn.close()
            return jsonify({'error': 'La relación Revision-Tarea no existe'}), 404

        # Si la relación existe, proceder con la eliminación
        cursor.execute("DELETE FROM Revision_Tarea WHERE id_Revision=%s AND id_Tarea=%s", (id_Revision, id_Tarea))
        conn.commit()
        conn.close()
        return "Relación Revision-Tarea Eliminada Correctamente"

@app.route('/reportes', methods=['GET', 'POST'])
def reportes():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Reporte")
        result = []
        for reporte in cursor.fetchall():
            result.append({
                'num_Referencia': reporte[0],
                'codigo_Revision': reporte[1],
                'id_Tarea': reporte[2],
                'descripcion': reporte[3]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nuevo_reporte = (
            request.form['num_Referencia'],
            request.form['codigo_Revision'],
            request.form['id_Tarea'],
            request.form['descripcion']
        )
        cursor.execute("INSERT INTO Reporte (num_Referencia, codigo_Revision, id_Tarea, descripcion) VALUES (%s, %s, %s, %s)", nuevo_reporte)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Reporte creado'}), 201
    
@app.route('/reportes/<num_Referencia>', methods=['GET'])
def get_reporte(num_Referencia):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Reporte WHERE num_Referencia=%s", (num_Referencia,))
        result = []
        for reporte in cursor.fetchall():
            result.append({
                'num_Referencia': reporte[0],
                'codigo_Revision': reporte[1],
                'id_Tarea': reporte[2],
                'descripcion': reporte[3]
            })
        conn.close()
        return jsonify(result)

@app.route('/reportes/delete/<num_Referencia>', methods=['GET'])
def delete_reporte(num_Referencia):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si el reporte existe
        cursor.execute("SELECT * FROM Reporte WHERE num_Referencia=%s", (num_Referencia,))
        reporte = cursor.fetchone()

        if reporte is None:
            conn.close()
            return jsonify({'error': 'El reporte no existe'}), 404

        # Si el reporte existe, proceder con la eliminación
        cursor.execute("DELETE FROM Reporte WHERE num_Referencia=%s", (num_Referencia,))
        conn.commit()
        conn.close()
        return "Reporte Eliminado Correctamente"

@app.route('/reportes/update/<num_Referencia>', methods=['POST'])
def update_reporte(num_Referencia):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Comprobar si el reporte existe
        cursor.execute("SELECT * FROM Reporte WHERE num_Referencia=%s", (num_Referencia,))
        reporte_existente = cursor.fetchone()

        if reporte_existente is None:
            conn.close()
            return jsonify({'error': 'El reporte no existe'}), 404

        # Si el reporte existe, proceder con la actualización
        nuevo_reporte = (
            request.form['num_Referencia'],
            request.form['codigo_Revision'],
            request.form['id_Tarea'],
            request.form['descripcion'],
            num_Referencia
        )
        cursor.execute("UPDATE Reporte SET num_Referencia=%s, codigo_Revision=%s, id_Tarea=%s, descripcion=%s WHERE num_Referencia=%s", nuevo_reporte)
        conn.commit()
        conn.close()
        return "Reporte Actualizado Correctamente"


@app.route('/no_planificadas', methods=['GET', 'POST'])
def no_planificadas():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM no_Planificada")
        result = []
        for no_planificada in cursor.fetchall():
            result.append({
                'num_Referencia': no_planificada[0],
                'id_Tarea': no_planificada[1]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nueva_relacion = (
            request.form['num_Referencia'],
            request.form['id_Tarea']
        )
        cursor.execute("INSERT INTO no_Planificada (num_Referencia, id_Tarea) VALUES (%s, %s)", nueva_relacion)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Relación no Planificada creada'}), 201
    
@app.route('/no_planificadas/<num_Referencia>/<id_Tarea>', methods=['GET'])
def get_no_planificada(num_Referencia, id_Tarea):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM no_Planificada WHERE num_Referencia=%s AND id_Tarea=%s", (num_Referencia, id_Tarea))
        result = []
        for no_planificada in cursor.fetchall():
            result.append({
                'num_Referencia': no_planificada[0],
                'id_Tarea': no_planificada[1]
            })
        conn.close()
        return jsonify(result)

@app.route('/no_planificadas/delete/<num_Referencia>/<id_Tarea>', methods=['GET'])
def delete_no_planificada(num_Referencia, id_Tarea):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si la relación no Planificada existe
        cursor.execute("SELECT * FROM no_Planificada WHERE num_Referencia=%s AND id_Tarea=%s", (num_Referencia, id_Tarea))
        no_planificada = cursor.fetchone()

        if no_planificada is None:
            conn.close()
            return jsonify({'error': 'La relación no Planificada no existe'}), 404

        # Si la relación existe, proceder con la eliminación
        cursor.execute("DELETE FROM no_Planificada WHERE num_Referencia=%s AND id_Tarea=%s", (num_Referencia, id_Tarea))
        conn.commit()
        conn.close()
        return "Relación no Planificada Eliminada Correctamente"

@app.route('/modelos_piezas', methods=['GET', 'POST'])
def modelos_piezas():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Modelo_Pieza")
        result = []
        for modelo_pieza in cursor.fetchall():
            result.append({
                'id_Modelo': modelo_pieza[0],
                'id_Pieza': modelo_pieza[1]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nueva_relacion = (
            request.form['id_Modelo'],
            request.form['id_Pieza']
        )
        cursor.execute("INSERT INTO Modelo_Pieza (id_Modelo, id_Pieza) VALUES (%s, %s)", nueva_relacion)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Relación Modelo-Pieza creada'}), 201
    
@app.route('/modelos_piezas/<id_Modelo>/<id_Pieza>', methods=['GET'])
def get_modelo_pieza(id_Modelo, id_Pieza):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Modelo_Pieza WHERE id_Modelo=%s AND id_Pieza=%s", (id_Modelo, id_Pieza))
        result = []
        for modelo_pieza in cursor.fetchall():
            result.append({
                'id_Modelo': modelo_pieza[0],
                'id_Pieza': modelo_pieza[1]
            })
        conn.close()
        return jsonify(result)

@app.route('/modelos_piezas/delete/<id_Modelo>/<id_Pieza>', methods=['GET'])
def delete_modelo_pieza(id_Modelo, id_Pieza):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si la relación Modelo-Pieza existe
        cursor.execute("SELECT * FROM Modelo_Pieza WHERE id_Modelo=%s AND id_Pieza=%s", (id_Modelo, id_Pieza))
        modelo_pieza = cursor.fetchone()

        if modelo_pieza is None:
            conn.close()
            return jsonify({'error': 'La relación Modelo-Pieza no existe'}), 404

        # Si la relación existe, proceder con la eliminación
        cursor.execute("DELETE FROM Modelo_Pieza WHERE id_Modelo=%s AND id_Pieza=%s", (id_Modelo, id_Pieza))
        conn.commit()
        conn.close()
        return "Relación Modelo-Pieza Eliminada Correctamente"

@app.route('/cantidades_piezas_tareas', methods=['GET', 'POST'])
def cantidades_piezas_tareas():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Cantidad_Pieza_Tarea")
        result = []
        for cantidad_pieza_tarea in cursor.fetchall():
            result.append({
                'id_Cantidad': cantidad_pieza_tarea[0],
                'cantidad': cantidad_pieza_tarea[1],
                'id_Pieza': cantidad_pieza_tarea[2],
                'id_Tarea': cantidad_pieza_tarea[3]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nueva_cantidad_pieza_tarea = (
            request.form['cantidad'],
            request.form['id_Pieza'],
            request.form['id_Tarea']
        )
        cursor.execute("INSERT INTO Cantidad_Pieza_Tarea (cantidad, id_Pieza, id_Tarea) VALUES (%s, %s, %s)", nueva_cantidad_pieza_tarea)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Cantidad Pieza-Tarea creada'}), 201
    
@app.route('/cantidades_piezas_tareas/<id_Cantidad>', methods=['GET'])
def get_cantidad_pieza_tarea(id_Cantidad):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Cantidad_Pieza_Tarea WHERE id_Cantidad=%s", (id_Cantidad,))
        result = []
        for cantidad_pieza_tarea in cursor.fetchall():
            result.append({
                'id_Cantidad': cantidad_pieza_tarea[0],
                'cantidad': cantidad_pieza_tarea[1],
                'id_Pieza': cantidad_pieza_tarea[2],
                'id_Tarea': cantidad_pieza_tarea[3]
            })
        conn.close()
        return jsonify(result)

@app.route('/cantidades_piezas_tareas/delete/<id_Cantidad>', methods=['GET'])
def delete_cantidad_pieza_tarea(id_Cantidad):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si la relación Cantidad Pieza-Tarea existe
        cursor.execute("SELECT * FROM Cantidad_Pieza_Tarea WHERE id_Cantidad=%s", (id_Cantidad,))
        cantidad_pieza_tarea = cursor.fetchone()

        if cantidad_pieza_tarea is None:
            conn.close()
            return jsonify({'error': 'La relación Cantidad Pieza-Tarea no existe'}), 404

        # Si la relación existe, proceder con la eliminación
        cursor.execute("DELETE FROM Cantidad_Pieza_Tarea WHERE id_Cantidad=%s", (id_Cantidad,))
        conn.commit()
        conn.close()
        return "Relación Cantidad Pieza-Tarea Eliminada Correctamente"

@app.route('/cantidades_consumibles_tareas', methods=['GET', 'POST'])
def cantidades_consumibles_tareas():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Cantidad_Consumible_Tarea")
        result = []
        for cantidad_consumible_tarea in cursor.fetchall():
            result.append({
                'id_Cantidad': cantidad_consumible_tarea[0],
                'cantidad': cantidad_consumible_tarea[1],
                'id_Consumible': cantidad_consumible_tarea[2],
                'id_Tarea': cantidad_consumible_tarea[3]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nueva_cantidad_consumible_tarea = (
            request.form['cantidad'],
            request.form['id_Consumible'],
            request.form['id_Tarea']
        )
        cursor.execute("INSERT INTO Cantidad_Consumible_Tarea (cantidad, id_Consumible, id_Tarea) VALUES (%s, %s, %s)", nueva_cantidad_consumible_tarea)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Cantidad Consumible-Tarea creada'}), 201
    
@app.route('/cantidades_consumibles_tareas/<id_Cantidad>', methods=['GET'])
def get_cantidad_consumible_tarea(id_Cantidad):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Cantidad_Consumible_Tarea WHERE id_Cantidad=%s", (id_Cantidad,))
        result = []
        for cantidad_consumible_tarea in cursor.fetchall():
            result.append({
                'id_Cantidad': cantidad_consumible_tarea[0],
                'cantidad': cantidad_consumible_tarea[1],
                'id_Consumible': cantidad_consumible_tarea[2],
                'id_Tarea': cantidad_consumible_tarea[3]
            })
        conn.close()
        return jsonify(result)

@app.route('/cantidades_consumibles_tareas/delete/<id_Cantidad>', methods=['GET'])
def delete_cantidad_consumible_tarea(id_Cantidad):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si la relación Cantidad Consumible-Tarea existe
        cursor.execute("SELECT * FROM Cantidad_Consumible_Tarea WHERE id_Cantidad=%s", (id_Cantidad,))
        cantidad_consumible_tarea = cursor.fetchone()

        if cantidad_consumible_tarea is None:
            conn.close()
            return jsonify({'error': 'La relación Cantidad Consumible-Tarea no existe'}), 404

        # Si la relación existe, proceder con la eliminación
        cursor.execute("DELETE FROM Cantidad_Consumible_Tarea WHERE id_Cantidad=%s", (id_Cantidad,))
        conn.commit()
        conn.close()
        return "Relación Cantidad Consumible-Tarea Eliminada Correctamente"

@app.route('/cantidades_consumibles_comandas', methods=['GET', 'POST'])
def cantidades_consumibles_comandas():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Cantidad_Consumible_Comanda")
        result = []
        for cantidad_consumible_comanda in cursor.fetchall():
            result.append({
                'id_Cantidad': cantidad_consumible_comanda[0],
                'cantidad': cantidad_consumible_comanda[1],
                'id_Consumible': cantidad_consumible_comanda[2],
                'id_Comanda': cantidad_consumible_comanda[3]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nueva_cantidad_consumible_comanda = (
            request.form['cantidad'],
            request.form['id_Consumible'],
            request.form['id_Comanda']
        )
        cursor.execute("INSERT INTO Cantidad_Consumible_Comanda (cantidad, id_Consumible, id_Comanda) VALUES (%s, %s, %s)", nueva_cantidad_consumible_comanda)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Cantidad Consumible-Comanda creada'}), 201
    
@app.route('/cantidades_consumibles_comandas/<id_Cantidad>', methods=['GET'])
def get_cantidad_consumible_comanda(id_Cantidad):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Cantidad_Consumible_Comanda WHERE id_Cantidad=%s", (id_Cantidad,))
        result = []
        for cantidad_consumible_comanda in cursor.fetchall():
            result.append({
                'id_Cantidad': cantidad_consumible_comanda[0],
                'cantidad': cantidad_consumible_comanda[1],
                'id_Consumible': cantidad_consumible_comanda[2],
                'id_Comanda': cantidad_consumible_comanda[3]
            })
        conn.close()
        return jsonify(result)

@app.route('/cantidades_consumibles_comandas/delete/<id_Cantidad>', methods=['GET'])
def delete_cantidad_consumible_comanda(id_Cantidad):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si la relación Cantidad Consumible-Comanda existe
        cursor.execute("SELECT * FROM Cantidad_Consumible_Comanda WHERE id_Cantidad=%s", (id_Cantidad,))
        cantidad_consumible_comanda = cursor.fetchone()

        if cantidad_consumible_comanda is None:
            conn.close()
            return jsonify({'error': 'La relación Cantidad Consumible-Comanda no existe'}), 404

        # Si la relación existe, proceder con la eliminación
        cursor.execute("DELETE FROM Cantidad_Consumible_Comanda WHERE id_Cantidad=%s", (id_Cantidad,))
        conn.commit()
        conn.close()
        return "Relación Cantidad Consumible-Comanda Eliminada Correctamente"

@app.route('/cantidades_piezas_comandas', methods=['GET', 'POST'])
def cantidades_piezas_comandas():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Cantidad_Pieza_Comanda")
        result = []
        for cantidad_pieza_comanda in cursor.fetchall():
            result.append({
                'id_Cantidad': cantidad_pieza_comanda[0],
                'cantidad': cantidad_pieza_comanda[1],
                'id_Pieza': cantidad_pieza_comanda[2],
                'id_Comanda': cantidad_pieza_comanda[3]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nueva_cantidad_pieza_comanda = (
            request.form['cantidad'],
            request.form['id_Pieza'],
            request.form['id_Comanda']
        )
        cursor.execute("INSERT INTO Cantidad_Pieza_Comanda (cantidad, id_Pieza, id_Comanda) VALUES (%s, %s, %s)", nueva_cantidad_pieza_comanda)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Cantidad Pieza-Comanda creada'}), 201
    
@app.route('/cantidades_piezas_comandas/<id_Cantidad>', methods=['GET'])
def get_cantidad_pieza_comanda(id_Cantidad):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Cantidad_Pieza_Comanda WHERE id_Cantidad=%s", (id_Cantidad,))
        result = []
        for cantidad_pieza_comanda in cursor.fetchall():
            result.append({
                'id_Cantidad': cantidad_pieza_comanda[0],
                'cantidad': cantidad_pieza_comanda[1],
                'id_Pieza': cantidad_pieza_comanda[2],
                'id_Comanda': cantidad_pieza_comanda[3]
            })
        conn.close()
        return jsonify(result)

@app.route('/cantidades_piezas_comandas/delete/<id_Cantidad>', methods=['GET'])
def delete_cantidad_pieza_comanda(id_Cantidad):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si la relación Cantidad Pieza-Comanda existe
        cursor.execute("SELECT * FROM Cantidad_Pieza_Comanda WHERE id_Cantidad=%s", (id_Cantidad,))
        cantidad_pieza_comanda = cursor.fetchone()

        if cantidad_pieza_comanda is None:
            conn.close()
            return jsonify({'error': 'La relación Cantidad Pieza-Comanda no existe'}), 404

        # Si la relación existe, proceder con la eliminación
        cursor.execute("DELETE FROM Cantidad_Pieza_Comanda WHERE id_Cantidad=%s", (id_Cantidad,))
        conn.commit()
        conn.close()
        return "Relación Cantidad Pieza-Comanda Eliminada Correctamente"

@app.route('/ofertas_piezas', methods=['GET', 'POST'])
def ofertas_piezas():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM oferta_pieza")
        result = []
        for oferta_pieza in cursor.fetchall():
            result.append({
                'id_oferta_pieza': oferta_pieza[0],
                'id_Pieza': oferta_pieza[1],
                'codigo_Proveedor': oferta_pieza[2],
                'cantidad': oferta_pieza[3]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nueva_oferta_pieza = (
            request.form['id_Pieza'],
            request.form['codigo_Proveedor'],
            request.form['cantidad']
        )
        cursor.execute("INSERT INTO oferta_pieza (id_Pieza, codigo_Proveedor, cantidad) VALUES (%s, %s, %s)", nueva_oferta_pieza)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Oferta Pieza creada'}), 201
    
@app.route('/ofertas_piezas/<id_oferta_pieza>', methods=['GET'])
def get_oferta_pieza(id_oferta_pieza):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM oferta_pieza WHERE id_oferta_pieza=%s", (id_oferta_pieza,))
        result = []
        for oferta_pieza in cursor.fetchall():
            result.append({
                'id_oferta_pieza': oferta_pieza[0],
                'id_Pieza': oferta_pieza[1],
                'codigo_Proveedor': oferta_pieza[2],
                'cantidad': oferta_pieza[3]
            })
        conn.close()
        return jsonify(result)

@app.route('/ofertas_piezas/delete/<id_oferta_pieza>', methods=['GET'])
def delete_oferta_pieza(id_oferta_pieza):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si la oferta Pieza existe
        cursor.execute("SELECT * FROM oferta_pieza WHERE id_oferta_pieza=%s", (id_oferta_pieza,))
        oferta_pieza = cursor.fetchone()

        if oferta_pieza is None:
            conn.close()
            return jsonify({'error': 'La oferta Pieza no existe'}), 404

        # Si la oferta Pieza existe, proceder con la eliminación
        cursor.execute("DELETE FROM oferta_pieza WHERE id_oferta_pieza=%s", (id_oferta_pieza,))
        conn.commit()
        conn.close()
        return "Oferta Pieza Eliminada Correctamente"

@app.route('/ofertas_consumibles', methods=['GET', 'POST'])
def ofertas_consumibles():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM oferta_consumible")
        result = []
        for oferta_consumible in cursor.fetchall():
            result.append({
                'id_oferta_consumible': oferta_consumible[0],
                'id_Consumible': oferta_consumible[1],
                'codigo_Proveedor': oferta_consumible[2],
                'cantidad': oferta_consumible[3]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nueva_oferta_consumible = (
            request.form['id_Consumible'],
            request.form['codigo_Proveedor'],
            request.form['cantidad']
        )
        cursor.execute("INSERT INTO oferta_consumible (id_Consumible, codigo_Proveedor, cantidad) VALUES (%s, %s, %s)", nueva_oferta_consumible)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Oferta Consumible creada'}), 201
    
@app.route('/ofertas_consumibles/<id_oferta_consumible>', methods=['GET'])
def get_oferta_consumible(id_oferta_consumible):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM oferta_consumible WHERE id_oferta_consumible=%s", (id_oferta_consumible,))
        result = []
        for oferta_consumible in cursor.fetchall():
            result.append({
                'id_oferta_consumible': oferta_consumible[0],
                'id_Consumible': oferta_consumible[1],
                'codigo_Proveedor': oferta_consumible[2],
                'cantidad': oferta_consumible[3]
            })
        conn.close()
        return jsonify(result)

@app.route('/ofertas_consumibles/delete/<id_oferta_consumible>', methods=['GET'])
def delete_oferta_consumible(id_oferta_consumible):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si la oferta Consumible existe
        cursor.execute("SELECT * FROM oferta_consumible WHERE id_oferta_consumible=%s", (id_oferta_consumible,))
        oferta_consumible = cursor.fetchone()

        if oferta_consumible is None:
            conn.close()
            return jsonify({'error': 'La oferta Consumible no existe'}), 404

        # Si la oferta Consumible existe, proceder con la eliminación
        cursor.execute("DELETE FROM oferta_consumible WHERE id_oferta_consumible=%s", (id_oferta_consumible,))
        conn.commit()
        conn.close()
        return "Oferta Consumible Eliminada Correctamente"

@app.route('/proveedores_telefonos', methods=['GET', 'POST'])
def proveedores_telefonos():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM ProveedorTelefono")
        result = []
        for proveedor_telefono in cursor.fetchall():
            result.append({
                'telefono': proveedor_telefono[0],
                'codigo_proveedor': proveedor_telefono[1]
            })
        conn.close()
        return jsonify(result)

    elif request.method == 'POST':
        nuevo_proveedor_telefono = (
            request.form['telefono'],
            request.form['codigo_proveedor']
        )
        cursor.execute("INSERT INTO ProveedorTelefono (telefono, codigo_proveedor) VALUES (%s, %s)", nuevo_proveedor_telefono)
        conn.commit()
        conn.close()
        return jsonify({'message': 'Proveedor Teléfono creado'}), 201
    
@app.route('/proveedores_telefonos/<telefono>', methods=['GET'])
def get_proveedor_telefono(telefono):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM ProveedorTelefono WHERE telefono=%s", (telefono,))
        result = []
        for proveedor_telefono in cursor.fetchall():
            result.append({
                'telefono': proveedor_telefono[0],
                'codigo_proveedor': proveedor_telefono[1]
            })
        conn.close()
        return jsonify(result)

@app.route('/proveedores_telefonos/delete/<telefono>', methods=['GET'])
def delete_proveedor_telefono(telefono):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        # Comprobar si el proveedor Teléfono existe
        cursor.execute("SELECT * FROM ProveedorTelefono WHERE telefono=%s", (telefono,))
        proveedor_telefono = cursor.fetchone()

        if proveedor_telefono is None:
            conn.close()
            return jsonify({'error': 'El proveedor Teléfono no existe'}), 404

        # Si el proveedor Teléfono existe, proceder con la eliminación
        cursor.execute("DELETE FROM ProveedorTelefono WHERE telefono=%s", (telefono,))
        conn.commit()
        conn.close()
        return "Proveedor Teléfono Eliminado Correctamente"

if __name__ == '__main__':
    app.run(debug=True, port=8080)
