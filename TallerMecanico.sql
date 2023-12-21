-- Borra las tablas si existen
DROP TABLE IF EXISTS Comanda;
DROP TABLE IF EXISTS Tarea;
DROP TABLE IF EXISTS Pieza;
DROP TABLE IF EXISTS Consumible;
DROP TABLE IF EXISTS Factura;
DROP TABLE IF EXISTS Empleado;
DROP TABLE IF EXISTS Cliente;
DROP TABLE IF EXISTS SolicitudCita;
DROP TABLE IF EXISTS Marca;
DROP TABLE IF EXISTS Modelo;
DROP TABLE IF EXISTS Vehiculo;
DROP TABLE IF EXISTS Proveedor;
DROP TABLE IF EXISTS Revision;
DROP TABLE IF EXISTS Problema;
DROP TABLE IF EXISTS Modelo_Tarea;
DROP TABLE IF EXISTS Revision_Tarea;
DROP TABLE IF EXISTS Reporte;
DROP TABLE IF EXISTS no_Planificada;
DROP TABLE IF EXISTS Modelo_Pieza;
DROP TABLE IF EXISTS Cantidad_Pieza_Tarea;
DROP TABLE IF EXISTS Cantidad_Consumible_Tarea;
DROP TABLE IF EXISTS Cantidad_Consumible_Comanda;
DROP TABLE IF EXISTS Cantidad_Pieza_Comanda;
DROP TABLE IF EXISTS pedido_Pieza;
DROP TABLE IF EXISTS pedido_Consumible;
DROP TABLE IF EXISTS ProveedorTelefono;


CREATE TABLE IF NOT EXISTS Comanda (
    id_Comanda SERIAL PRIMARY KEY,
    precio_Total NUMERIC(10, 2) NOT NULL CHECK(precio_Total >= 0.00)
);

CREATE TABLE IF NOT EXISTS Tarea (
    id_Tarea SERIAL PRIMARY KEY,
    nombre_Servicio VARCHAR(50) NOT NULL,
    descripcion TEXT,
    duracion INT NOT NULL CHECK(duracion >= 0),
    coste NUMERIC(10, 2) NOT NULL CHECK(coste >= 0.00)
);

CREATE TABLE IF NOT EXISTS Pieza (
    id_Pieza SERIAL PRIMARY KEY,
    nombre_Producto VARCHAR(50) NOT NULL,
    precio NUMERIC(10, 2) NOT NULL CHECK(precio >= 0.00),
    unidades INT NOT NULL CHECK(unidades >= 0),
    num_Fabricante VARCHAR(15) NOT NULL
);

CREATE TABLE IF NOT EXISTS Consumible (
    id_Consumible SERIAL PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    precio NUMERIC(10, 2) NOT NULL CHECK(precio >= 0.00),
    litros_por_unidad NUMERIC(5, 2) NOT NULL CHECK(litros_por_unidad >= 0.00)
);

CREATE TABLE IF NOT EXISTS Factura (
    num_Referencia SERIAL PRIMARY KEY,
    porcentaje_Impuestos NUMERIC(5, 2) NOT NULL CHECK(porcentaje_Impuestos >= 0.00),
    coste_Total NUMERIC(10, 2) NOT NULL CHECK(coste_Total >= 0.00),
    fecha_Emision DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS Empleado (
    dni VARCHAR(9) PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    turno VARCHAR(7) NOT NULL,
    direccion TEXT, 
    telefono VARCHAR(20) NOT NULL,
    email VARCHAR(30) NOT NULL,
    dni_encargado VARCHAR(9) REFERENCES Empleado(dni)
);

CREATE TABLE IF NOT EXISTS Cliente (
    dni VARCHAR(9) PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    direccion TEXT,
    telefono VARCHAR(20) NOT NULL,
    email VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS SolicitudCita (
    fecha DATE,
    hora TIME,
    num_Referencia SERIAL PRIMARY KEY,
    dni_cliente VARCHAR(9) NOT NULL REFERENCES Cliente(dni)
);

CREATE TABLE IF NOT EXISTS Marca (
    id_Marca SERIAL PRIMARY KEY,
    nombre VARCHAR(15) NOT NULL
);

CREATE TABLE IF NOT EXISTS Modelo (
    id_Modelo SERIAL PRIMARY KEY,
    anyo INT NOT NULL,
    nombre VARCHAR(15) NOT NULL,
    id_Marca INT REFERENCES Marca(id_Marca)
);

CREATE TABLE IF NOT EXISTS Vehiculo (
    matricula VARCHAR(15) NOT NULL PRIMARY KEY,
    num_Bastidor VARCHAR(17) NOT NULL,
    anyo_Compra INT NOT NULL,
    anyo_Fabricacion INT NOT NULL,
    tipo_Vehiculo VARCHAR(20) NOT NULL,
    num_KM INT NOT NULL,
    dni_cliente VARCHAR(9) NOT NULL REFERENCES Cliente(dni),
    id_Modelo INT REFERENCES Modelo(id_Modelo)
);

CREATE TABLE IF NOT EXISTS Proveedor (
    codigo INT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    direccion_CP INT NOT NULL,
    direccion_Calle VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS Revision (
    codigo_Revision VARCHAR(6) PRIMARY KEY,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    periodica BOOLEAN NOT NULL,
    dni_empleado VARCHAR(9) REFERENCES Empleado(dni),
    UNIQUE (codigo_Revision)
);

CREATE TABLE IF NOT EXISTS Problema (
    id_Problema SERIAL PRIMARY KEY,
    descripcion TEXT,
    codigo_Revision VARCHAR(6) REFERENCES Revision(codigo_Revision) UNIQUE
);

CREATE TABLE IF NOT EXISTS Modelo_Tarea (
    id_Modelo INT REFERENCES Modelo(id_Modelo),
    id_Tarea INT REFERENCES Tarea(id_Tarea),
    PRIMARY KEY (id_Modelo, id_Tarea)
);

CREATE TABLE IF NOT EXISTS Revision_Tarea (
    id_Revision VARCHAR(6) REFERENCES Revision(codigo_Revision),
    id_Tarea INT REFERENCES Tarea(id_Tarea),
    PRIMARY KEY (id_Revision, id_Tarea)
);

CREATE TABLE IF NOT EXISTS Reporte (
    num_Referencia INT PRIMARY KEY,
    codigo_Revision VARCHAR(6) REFERENCES Revision(codigo_Revision) UNIQUE,
    id_Tarea INT REFERENCES Tarea(id_Tarea),
    descripcion TEXT
);

CREATE TABLE IF NOT EXISTS no_Planificada (
    num_Referencia INT REFERENCES Reporte(num_Referencia),
    id_Tarea INT REFERENCES Tarea(id_Tarea),
    PRIMARY KEY (num_Referencia, id_Tarea)
);

CREATE TABLE IF NOT EXISTS Modelo_Pieza (
    id_Modelo INT REFERENCES Modelo(id_Modelo),
    id_Pieza INT REFERENCES Pieza(id_Pieza),
    PRIMARY KEY (id_Modelo, id_Pieza)
);

CREATE TABLE IF NOT EXISTS Cantidad_Pieza_Tarea (
    id_Cantidad SERIAL PRIMARY KEY,
    cantidad INT NOT NULL CHECK(cantidad >= 0),
    id_Pieza INT REFERENCES Pieza(id_Pieza),
    id_Tarea INT REFERENCES Tarea(id_Tarea)
);

CREATE TABLE IF NOT EXISTS Cantidad_Consumible_Tarea (
    id_Cantidad SERIAL PRIMARY KEY,
    cantidad INT NOT NULL CHECK(cantidad >= 0),
    id_Consumible INT REFERENCES Consumible(id_Consumible),
    id_Tarea INT REFERENCES Tarea(id_Tarea)
);

CREATE TABLE IF NOT EXISTS Cantidad_Consumible_Comanda (
    id_Cantidad SERIAL PRIMARY KEY,
    cantidad INT NOT NULL CHECK(cantidad >= 0),
    id_Consumible INT REFERENCES Consumible(id_Consumible),
    id_Comanda INT REFERENCES Comanda(id_Comanda)
);

CREATE TABLE IF NOT EXISTS Cantidad_Pieza_Comanda (
    id_Cantidad SERIAL PRIMARY KEY,
    cantidad INT NOT NULL CHECK(cantidad >= 0),
    id_Pieza INT REFERENCES Pieza(id_Pieza),
    id_Comanda INT REFERENCES Comanda(id_Comanda)
);

CREATE TABLE IF NOT EXISTS pedido_Pieza (
    id_Pedido SERIAL PRIMARY KEY,
    id_Pieza INT REFERENCES Pieza(id_Pieza),
    codigo_Proveedor INT REFERENCES Proveedor(codigo),
    cantidad INT NOT NULL CHECK(cantidad >= 0)
);

CREATE TABLE IF NOT EXISTS pedido_Consumible (
    id_Pedido SERIAL PRIMARY KEY,
    id_Consumible INT REFERENCES Consumible(id_Consumible),
    codigo_Proveedor INT REFERENCES Proveedor(codigo),
    cantidad INT NOT NULL CHECK(cantidad >= 0)
);

CREATE TABLE IF NOT EXISTS ProveedorTelefono (
    telefono VARCHAR(20) PRIMARY KEY,
    codigo_proveedor INT REFERENCES Proveedor(codigo)
);

-- Trigger para calcular el coste total en la tabla Comanda
CREATE OR REPLACE FUNCTION calcular_coste_total()
RETURNS TRIGGER AS $$
BEGIN
    NEW.precio_Total = (SELECT SUM(cantidad * precio)
                       FROM Cantidad_Pieza_Comanda cpc
                       JOIN Pieza p ON cpc.id_Pieza = p.id_Pieza
                       WHERE cpc.id_Comanda = NEW.id_Comanda);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER actualizar_coste_total
BEFORE INSERT OR UPDATE ON Cantidad_Pieza_Comanda
FOR EACH ROW EXECUTE FUNCTION calcular_coste_total();

-- Trigger para evitar duplicados en la tabla Tarea
CREATE OR REPLACE FUNCTION evitar_duplicados_tarea()
RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT COUNT(*) FROM Tarea WHERE id_Tarea = NEW.id_Tarea) > 0 THEN
        RAISE EXCEPTION 'Ya existe una tarea con el mismo ID';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_duplicados_tarea
BEFORE INSERT OR UPDATE ON Tarea
FOR EACH ROW EXECUTE FUNCTION evitar_duplicados_tarea();

-- Trigger para evitar duplicados en la tabla Pieza
CREATE OR REPLACE FUNCTION evitar_duplicados_pieza()
RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT COUNT(*) FROM Pieza WHERE id_Pieza = NEW.id_Pieza) > 0 THEN
        RAISE EXCEPTION 'Ya existe una pieza con el mismo ID';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_duplicados_pieza
BEFORE INSERT OR UPDATE ON Pieza
FOR EACH ROW EXECUTE FUNCTION evitar_duplicados_pieza();

-- Trigger para evitar duplicados en la tabla Consumible:
CREATE OR REPLACE FUNCTION evitar_duplicados_consumible()
RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT COUNT(*) FROM Consumible WHERE id_Consumible = NEW.id_Consumible) > 0 THEN
        RAISE EXCEPTION 'Ya existe un consumible con el mismo ID';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_duplicados_consumible
BEFORE INSERT OR UPDATE ON Consumible
FOR EACH ROW EXECUTE FUNCTION evitar_duplicados_consumible();

-- Trigger para evitar duplicados en la tabla Factura
CREATE OR REPLACE FUNCTION evitar_duplicados_factura()
RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT COUNT(*) FROM Factura WHERE num_Referencia = NEW.num_Referencia) > 0 THEN
        RAISE EXCEPTION 'Ya existe una factura con el mismo número de referencia';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger para asegurar que el DNI sea único en la tabla Empleado
CREATE OR REPLACE FUNCTION asegurar_dni_unico_empleado()
RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT COUNT(*) FROM Empleado WHERE dni = NEW.dni) > 0 THEN
        RAISE EXCEPTION 'Ya existe un empleado con el mismo DNI';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_dni_unico_empleado
BEFORE INSERT OR UPDATE ON Empleado
FOR EACH ROW EXECUTE FUNCTION asegurar_dni_unico_empleado();

CREATE TRIGGER verificar_duplicados_factura
BEFORE INSERT OR UPDATE ON Factura
FOR EACH ROW EXECUTE FUNCTION evitar_duplicados_factura();

-- Trigger para asegurar que el DNI sea único en la tabla Cliente
CREATE OR REPLACE FUNCTION asegurar_dni_unico_cliente()
RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT COUNT(*) FROM Cliente WHERE dni = NEW.dni) > 0 THEN
        RAISE EXCEPTION 'Ya existe un cliente con el mismo DNI';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_dni_unico_cliente
BEFORE INSERT OR UPDATE ON Cliente
FOR EACH ROW EXECUTE FUNCTION asegurar_dni_unico_cliente();

-- Trigger para asegurar que el num_Referencia sea único en la tabla SolicitudCita:
CREATE OR REPLACE FUNCTION asegurar_num_referencia_unico_cita()
RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT COUNT(*) FROM SolicitudCita WHERE num_Referencia = NEW.num_Referencia) > 0 THEN
        RAISE EXCEPTION 'Ya existe una cita con el mismo número de referencia';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_num_referencia_unico_cita
BEFORE INSERT OR UPDATE ON SolicitudCita
FOR EACH ROW EXECUTE FUNCTION asegurar_num_referencia_unico_cita();

-- Trigger para asegurar que la matricula sea única en la tabla Vehiculo
CREATE OR REPLACE FUNCTION asegurar_matricula_unica()
RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT COUNT(*) FROM Vehiculo WHERE matricula = NEW.matricula) > 0 THEN
        RAISE EXCEPTION 'Ya existe un vehículo con la misma matrícula';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_matricula_unica
BEFORE INSERT OR UPDATE ON Vehiculo
FOR EACH ROW EXECUTE FUNCTION asegurar_matricula_unica();

-- Trigger para asegurar que el num_Bastidor sea único en la tabla Vehiculo:
CREATE OR REPLACE FUNCTION asegurar_num_bastidor_unico()
RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT COUNT(*) FROM Vehiculo WHERE num_Bastidor = NEW.num_Bastidor) > 0 THEN
        RAISE EXCEPTION 'Ya existe un vehículo con el mismo número de bastidor';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_num_bastidor_unico
BEFORE INSERT OR UPDATE ON Vehiculo
FOR EACH ROW EXECUTE FUNCTION asegurar_num_bastidor_unico();

-- Trigger para evitar duplicados en la tabla Proveedor
CREATE OR REPLACE FUNCTION evitar_duplicados_proveedor()
RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT COUNT(*) FROM Proveedor WHERE codigo = NEW.codigo) > 0 THEN
        RAISE EXCEPTION 'Ya existe un proveedor con el mismo código';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_duplicados_proveedor
BEFORE INSERT OR UPDATE ON Proveedor
FOR EACH ROW EXECUTE FUNCTION evitar_duplicados_proveedor();

-- Trigger para asegurar que el codigo_Revision sea único en la tabla Revision
CREATE OR REPLACE FUNCTION asegurar_codigo_revision_unico()
RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT COUNT(*) FROM Revision WHERE codigo_Revision = NEW.codigo_Revision) > 0 THEN
        RAISE EXCEPTION 'Ya existe una revisión con el mismo código';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_codigo_revision_unico
BEFORE INSERT OR UPDATE ON Revision
FOR EACH ROW EXECUTE FUNCTION asegurar_codigo_revision_unico();

-- Trigger para asegurar que el id_Problema sea único en la tabla Problema:
CREATE OR REPLACE FUNCTION asegurar_id_problema_unico()
RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT COUNT(*) FROM Problema WHERE id_Problema = NEW.id_Problema) > 0 THEN
        RAISE EXCEPTION 'Ya existe un problema con el mismo ID';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_id_problema_unico
BEFORE INSERT OR UPDATE ON Problema
FOR EACH ROW EXECUTE FUNCTION asegurar_id_problema_unico();

-- Trigger para asegurar que el num_Referencia sea único en la tabla Reporte:
CREATE OR REPLACE FUNCTION asegurar_num_referencia_unico()
RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT COUNT(*) FROM Reporte WHERE num_Referencia = NEW.num_Referencia) > 0 THEN
        RAISE EXCEPTION 'Ya existe un reporte con el mismo número de referencia';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_num_referencia_unico
BEFORE INSERT OR UPDATE ON Reporte
FOR EACH ROW EXECUTE FUNCTION asegurar_num_referencia_unico();

-- Trigger para asegurar que el id_Pedido sea único en la tabla pedido_Pieza
CREATE OR REPLACE FUNCTION asegurar_id_pedido_unico_pieza()
RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT COUNT(*) FROM pedido_Pieza WHERE id_Pedido = NEW.id_Pedido) > 0 THEN
        RAISE EXCEPTION 'Ya existe un pedido de pieza con el mismo ID de pedido';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_id_pedido_unico_pieza
BEFORE INSERT OR UPDATE ON pedido_Pieza
FOR EACH ROW EXECUTE FUNCTION asegurar_id_pedido_unico_pieza();

-- Trigger para asegurar que el id_Pedido sea único en la tabla pedido_Consumible
CREATE OR REPLACE FUNCTION asegurar_id_pedido_unico_consumible()
RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT COUNT(*) FROM pedido_Consumible WHERE id_Pedido = NEW.id_Pedido) > 0 THEN
        RAISE EXCEPTION 'Ya existe un pedido de consumible con el mismo ID de pedido';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_id_pedido_unico_consumible
BEFORE INSERT OR UPDATE ON pedido_Consumible
FOR EACH ROW EXECUTE FUNCTION asegurar_id_pedido_unico_consumible();

-- Trigger para asegurar que el telefono sea único en la tabla ProveedorTelefono
CREATE OR REPLACE FUNCTION asegurar_telefono_unico_proveedor()
RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT COUNT(*) FROM ProveedorTelefono WHERE telefono = NEW.telefono) > 0 THEN
        RAISE EXCEPTION 'Ya existe un proveedor con el mismo número de teléfono';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_telefono_unico_proveedor
BEFORE INSERT OR UPDATE ON ProveedorTelefono
FOR EACH ROW EXECUTE FUNCTION asegurar_telefono_unico_proveedor();
-------------------------------------------------------------------------------------------------------------
-- Trigger para asegurar que el precio total de una comanda no sea negativo
CREATE OR REPLACE FUNCTION comprobar_precio_comanda()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.precio_total < 0.0 THEN
    RAISE EXCEPTION 'El precio total de la comanda no puede ser negativo';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER antes_insertar_comanda
BEFORE INSERT ON comanda
FOR EACH ROW
EXECUTE FUNCTION comprobar_precio_comanda();

-- Trigger para asegurar que la duración de una tarea no sea negativa:
CREATE OR REPLACE FUNCTION comprobar_duracion_tarea()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.duracion < 0 THEN
    RAISE EXCEPTION 'La duración de la tarea no puede ser negativa';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER antes_insertar_tarea
BEFORE INSERT ON tarea
FOR EACH ROW
EXECUTE FUNCTION comprobar_duracion_tarea();

-- Trigger para asegurar que el coste total de una factura no sea negativo
CREATE OR REPLACE FUNCTION comprobar_coste_Factura()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.coste_total < 0.0 THEN
    RAISE EXCEPTION 'El coste total de la factura no puede ser negativo';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER antes_insertar_coste_Factura
BEFORE INSERT ON factura
FOR EACH ROW
EXECUTE FUNCTION comprobar_coste_Factura();

-- Trigger para asegurar que el porcentaje de impuestos esté en el rango correcto
CREATE OR REPLACE FUNCTION comprobar_impuestos_porcentaje()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.porcentaje_impuestos < 0.0 OR NEW.porcentaje_impuestos > 100.0 THEN
    RAISE EXCEPTION 'El porcentaje de impuestos debe estar entre 0 y 100';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER antes_insertar_porcentaje
BEFORE INSERT ON factura
FOR EACH ROW
EXECUTE FUNCTION comprobar_impuestos_porcentaje();
