-- Datos para la tabla Comanda
INSERT INTO Comanda (id_Comanda, precio_Total) VALUES
(1, 150.50),
(2, 200.75),
(3, 180.00),
(4, 120.00),
(5, 180.25),
(6, 220.50);

-- Datos para la tabla Tarea
INSERT INTO Tarea (id_Tarea, nombre_Servicio, descripcion, duracion, coste) VALUES
(1, 'Cambio de aceite', 'Cambio de aceite y filtro', 60, 50.00),
(2, 'Reparación de frenos', 'Sustitución de pastillas y discos', 120, 120.00),
(3, 'Inspección general', 'Revisión de componentes principales', 90, 80.00),
(4, 'Cambio de neumáticos', 'Sustitución de neumáticos desgastados', 45, 90.00),
(5, 'Alineación de dirección', 'Ajuste de la alineación de ruedas', 30, 60.00),
(6, 'Diagnóstico de motor', 'Análisis y diagnóstico de problemas del motor', 120, 150.00);

-- Datos para la tabla Pieza
INSERT INTO Pieza (id_Pieza, nombre_Producto, precio, unidades, num_Fabricante) VALUES
(1, 'Filtro de aceite', 10.00, 30, '12345'),
(2, 'Pastillas de freno', 25.00, 20, '67890'),
(3, 'Bujías', 8.00, 40, '54321'),
(4, 'Filtro de aire', 15.00, 25, '67890'),
(5, 'Batería de coche', 80.00, 15, '54321'),
(6, 'Correa de distribución', 30.00, 20, '98765');

-- Datos para la tabla Consumible
INSERT INTO Consumible (id_Consumible, nombre, precio, litros_por_unidad) VALUES
(1, 'Aceite de motor', 20.00, 4.5),
(2, 'Líquido de frenos', 15.00, 1.0),
(3, 'Limpiaparabrisas', 5.00, 1.5),
(4, 'Anticongelante', 12.00, 2.0),
(5, 'Aceite de transmisión', 25.00, 3.0),
(6, 'Aditivo para combustible', 8.00, 1.0);

-- Datos para la tabla Factura
INSERT INTO Factura (num_Referencia, porcentaje_Impuestos, coste_Total, fecha_Emision) VALUES
(1, 0.21, 200.00, '2023-01-15'),
(2, 0.18, 250.00, '2023-02-20'),
(3, 0.20, 180.00, '2023-03-10'),
(4, 0.15, 150.00, '2023-04-01'),
(5, 0.20, 200.00, '2023-04-05'),
(6, 0.18, 180.50, '2023-04-10');

-- Datos para la tabla Empleado
INSERT INTO Empleado (dni, nombre, turno, direccion, telefono, email, dni_encargado) VALUES
('12345678A', 'Juan Pérez', 'Mañana', 'Calle Principal 123', '987654321', 'juan@example.com', NULL),
('98765432B', 'María López', 'Tarde', 'Avenida Central 456', '123456789', 'maria@example.com', '12345678A'),
('11122233C', 'Pedro García', 'Nocturno', 'Avenida Principal 789', '666777888', 'pedro@example.com', '98765432B'),
('55566677D', 'Ana Martínez', 'Mañana', 'Calle Secundaria 234', '111222333', 'ana@example.com', NULL);

-- Datos para la tabla Cliente
INSERT INTO Cliente (dni, nombre, direccion, telefono, email) VALUES
('11122233E', 'Carlos Rodríguez', 'Plaza Mayor 789', '555666777', 'carlos@example.com'),
('44455566F', 'Laura Gómez', 'Calle Secundaria 234', '888999000', 'laura@example.com'),
('77788899G', 'Sara Jiménez', 'Plaza Pequeña 567', '333444555', 'sara@example.com'),
('88899900H', 'Pablo Rodríguez', 'Avenida Central 890', '999000111', 'pablo@example.com');

-- Datos para la tabla SolicitudCita
INSERT INTO SolicitudCita (fecha, hora, dni_cliente) VALUES
('2023-04-05', '10:00:00', '11122233E'),
('2023-04-10', '15:30:00', '44455566F'),
('2023-04-15', '14:30:00', '77788899G'),
('2023-04-20', '11:00:00', '88899900H');

-- Datos para la tabla Marca
INSERT INTO Marca (nombre) VALUES ('Toyota'), ('Ford'), ('Honda'),('Chevrolet'), ('Volkswagen'), ('Nissan');

-- Datos para la tabla Modelo
INSERT INTO Modelo (anyo, nombre, id_Marca) VALUES
(2022, 'Corolla', 1),
(2023, 'Fusion', 2),
(2021, 'Civic', 3),
(2023, 'Malibu', 4),
(2022, 'Golf', 5),
(2021, 'Altima', 6);

-- Datos para la tabla Vehiculo
INSERT INTO Vehiculo (anyo_Compra, anyo_Fabricacion, tipo_Vehiculo, num_Bastidor, matricula, num_KM, dni_cliente, id_Modelo) VALUES
(2022, 2021, 'Sedán', 'ABC123XYZ45678901', 'ABC-123', 15000, '11122233E', 1),
(2023, 2022, 'Sedán', 'DEF456XYZ12378901', 'DEF-456', 20000, '44455566F', 2),
(2023, 2022, 'Sedán', 'GHI789JKL01234567', 'GHI-789', 18000, '77788899G', 4),
(2022, 2021, 'Hatchback', 'MNO123PQR45678901', 'MNO-123', 22000, '88899900H', 5);

-- Datos para la tabla Proveedor
INSERT INTO Proveedor (codigo, nombre, direccion_CP, direccion_Calle) VALUES
(1, 'Proveedor1', 12345, 'Calle Proveedor1'),
(2, 'Proveedor2', 67890, 'Calle Proveedor2'),
(3, 'Proveedor3', 13579, 'Calle Proveedor3'),
(4, 'Proveedor4', 24680, 'Calle Proveedor4'),
(5, 'Proveedor5', 97531, 'Calle Proveedor5'),
(6, 'Proveedor6', 86420, 'Calle Proveedor6');

-- Datos para la tabla Revision
INSERT INTO Revision (codigo_Revision, fecha, hora, periodica, dni_empleado) VALUES
('REV001', '2023-05-10', '14:00:00', true, '12345678A'),
('REV002', '2023-06-20', '09:30:00', false, '12345678A'),
('REV003', '2023-07-05', '10:30:00', true, '11122233C'),
('REV004', '2023-08-15', '13:45:00', false, '98765432B');

-- Datos para la tabla Problema
INSERT INTO Problema (descripcion, codigo_Revision) VALUES
('Fallo en el sistema de frenos', 'REV001'),
('Fuga de aceite', 'REV002'),
('Problemas en el sistema eléctrico', 'REV003'),
('Fallo en la transmisión', 'REV004');

-- Datos para la tabla Modelo_Tarea
INSERT INTO Modelo_Tarea (id_Modelo, id_Tarea) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6);

-- Datos para la tabla Revision_Tarea
INSERT INTO Revision_Tarea (id_Revision, id_Tarea) VALUES
('REV001', 1),
('REV002', 3),
('REV003', 4),
('REV004', 6);

-- Datos para la tabla Reporte
INSERT INTO Reporte (num_Referencia, codigo_Revision, id_Tarea, descripcion) VALUES
(1, 'REV001', 1, 'Cambio de pastillas de freno'),
(2, 'REV002', 3, 'Revisión general del motor'),
(3, 'REV003', 4, 'Reemplazo del sistema eléctrico'),
(4, 'REV004', 6, 'Reparación de la transmisión');

-- Datos para la tabla no_Planificada
INSERT INTO no_Planificada (num_Referencia, id_Tarea) VALUES
(1, 2),
(2, 1),
(3, 5),
(4, 6);

-- Datos para la tabla Modelo_Pieza
INSERT INTO Modelo_Pieza (id_Modelo, id_Pieza) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6);

-- Datos para la tabla Cantidad_Pieza_Tarea
INSERT INTO Cantidad_Pieza_Tarea (cantidad, id_Pieza, id_Tarea) VALUES
(2, 1, 1),
(3, 2, 2),
(1, 3, 3),
(2, 4, 4),
(3, 5, 5),
(1, 6, 6);

-- Datos para la tabla Cantidad_Consumible_Tarea
INSERT INTO Cantidad_Consumible_Tarea (cantidad, id_Consumible, id_Tarea) VALUES
(1, 1, 1),
(2, 2, 2),
(1, 3, 3),
(1, 4, 4),
(2, 5, 5),
(1, 6, 6);

-- Datos para la tabla Cantidad_Consumible_Comanda
INSERT INTO Cantidad_Consumible_Comanda (cantidad, id_Consumible, id_Comanda) VALUES
(1, 1, 1),
(2, 2, 2),
(1, 3, 3),
(1, 4, 4),
(2, 5, 5),
(1, 6, 6);

-- Datos para la tabla Cantidad_Pieza_Comanda
INSERT INTO Cantidad_Pieza_Comanda (cantidad, id_Pieza, id_Comanda) VALUES
(2, 1, 1),
(3, 2, 2),
(1, 3, 3),
(2, 4, 4),
(3, 5, 5),
(1, 6, 6);

-- Datos para la tabla oferta_pieza
INSERT INTO oferta_pieza (id_oferta_pieza, id_Pieza, codigo_Proveedor, cantidad) VALUES
(4, 1, 1, 50),
(5, 2, 2, 30),
(6, 3, 3, 40),
(7, 4, 4, 25),
(8, 5, 5, 20),
(9, 6, 6, 30);

-- Datos para la tabla oferta_consumible
INSERT INTO oferta_consumible (id_oferta_consumible, id_Consumible, codigo_Proveedor, cantidad) VALUES
(4, 1, 1, 10),
(5, 2, 2, 15),
(6, 3, 3, 20),
(7, 4, 4, 5),
(8, 5, 5, 10),
(9, 6, 6, 8);

-- Datos para la tabla ProveedorTelefono
INSERT INTO ProveedorTelefono (telefono, codigo_proveedor) VALUES
('111-111-1111', 1),
('222-222-2222', 2),
('333-333-3333', 3),
('444-444-4444', 4),
('555-555-5555', 5),
('666-666-6666', 6);
