import mysql.connector

def conectar() :
    mydb = mysql.connector.connect(
        host="ec2-184-73-56-205.compute-1.amazonaws.com",
        user="coramar_bd",
        passwd="Adminroot12*",
        database="coramar",
        port = "3306")
    return mydb

def get_clientes() :
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM cliente")
    myresult = cursor.fetchall()
    return myresult

def get_factura() :
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM factura")
    myresult = cursor.fetchall()

    return myresult

def get_repartidores():
    mydb = conectar()
    cursor = mydb.cursor()

    # Consulta para obtener la cantidad de asignaciones (repartos) por repartidor
    cursor.execute("""
                   SELECT E.Cedula, E.Primer_Nombre, E.Apellido, COUNT(A.Cod_Ruta) AS Total_Repartos
                   FROM Empleado E
                   LEFT JOIN Asignacion A ON E.Cedula = A.Repartidor
                   GROUP BY E.Cedula ,E.Primer_Nombre, E.Apellido
                   ORDER BY Total_Repartos DESC
                   """)

    myresult = cursor.fetchall()
    return myresult


def ingresar_cliente():
    mydb = conectar()
    cursor = mydb.cursor()
    cedula = input("Ingrese la cédula del cliente (10 caracteres): ")
    nombre = input("Ingrese el primer nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    categoria = input("Ingrese la categoría del cliente: ")
    estado_cliente = input("Ingrese el estado del cliente (Activo/Inactivo): ")
    direccion = input("Ingrese la dirección del cliente: ")
    cod_zona = input("Ingrese el código de la zona: ")
    cod_tarifa = input("Ingrese el código de tarifa: ")

    try:
        cursor.execute("""
            INSERT INTO Cliente (Cedula, Primer_Nombre, Apellido, Telefono, Categoria, Estado_cliente, Direccion, Cod_Zona, Cod_Tarifa)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (cedula, nombre, apellido, telefono, categoria, estado_cliente, direccion, cod_zona, cod_tarifa))

        mydb.commit()  # Confirmar la transacción
        print("¡Cliente ingresado con éxito!")
    except mysql.connector.Error as err:
        print(f"Error al insertar cliente: {err}")
        
def insertar_empleado(cedula, primer_nombre, apellido, telefono, cuenta_bancaria, rol, estado_empleado, id_encargado):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO Empleado VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                   (cedula, primer_nombre, apellido, telefono, cuenta_bancaria, rol, estado_empleado, id_encargado))
    mydb.commit()

def consultar_empleados():
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Empleado")
    return cursor.fetchall()

def actualizar_empleado(cedula, primer_nombre, apellido, telefono, cuenta_bancaria, rol, estado_empleado, id_encargado):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("""
        UPDATE Empleado
        SET Primer_Nombre=%s, Apellido=%s, Telefono=%s, Cuenta_Bancaria=%s, Rol=%s, Estado_Empleado=%s, ID_Encargado=%s
        WHERE Cedula=%s
    """, (primer_nombre, apellido, telefono, cuenta_bancaria, rol, estado_empleado, id_encargado, cedula))
    mydb.commit()

def eliminar_empleado(cedula):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM Empleado WHERE Cedula=%s", (cedula,))
    mydb.commit()

def buscar_empleado_por_nombre_apellido(nombre_o_apellido):
    mydb = conectar()
    cursor = mydb.cursor()
    nombre, apellido = nombre_o_apellido.strip().split(" ", 1)
    cursor.execute("""
        SELECT * FROM Empleado
        WHERE Primer_Nombre LIKE %s AND Apellido LIKE %s
    """, ('%' + nombre + '%', '%' + apellido + '%'))
    return cursor.fetchall()

def insertar_zona(id_zona, nombre_zona, cantidad_clientes, estado_zona):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO Zona VALUES (%s, %s, %s, %s)", (id_zona, nombre_zona, cantidad_clientes, estado_zona))
    mydb.commit()

def consultar_zonas():
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Zona")
    return cursor.fetchall()

def actualizar_zona(id_zona, nombre_zona, cantidad_clientes, estado_zona):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("UPDATE Zona SET Nombre_Zona=%s, Cantidad_Clientes=%s, Estado_Zona=%s WHERE ID_Zona=%s", (nombre_zona, cantidad_clientes, estado_zona, id_zona))
    mydb.commit()

def eliminar_zona(id_zona):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM Zona WHERE ID_Zona=%s", (id_zona,))
    mydb.commit()

def buscar_zona_por_nombre(nombre_zona):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Zona WHERE Nombre_Zona LIKE %s", ('%' + nombre_zona + '%',))
    return cursor.fetchall()

def insertar_proveedor(ruc, nombre, direccion, contacto, correo, estado):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO Proveedor VALUES (%s, %s, %s, %s, %s, %s)", (ruc, nombre, direccion, contacto, correo, estado))
    mydb.commit()

def buscar_proveedor_por_nombre(nombre_proveedor):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Proveedor WHERE Nombre_Proveedor LIKE %s", ('%' + nombre_proveedor + '%',))
    return cursor.fetchall()

def consultar_proveedores():
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Proveedor")
    return cursor.fetchall()

def actualizar_proveedor(ruc, nombre, direccion, contacto, correo, estado):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("UPDATE Proveedor SET Nombre_Proveedor=%s, Dir_Proveedor=%s, Contacto_Proveedor=%s, Correo=%s, Estado_Proveedor=%s WHERE RUC=%s", (nombre, direccion, contacto, correo, estado, ruc))
    mydb.commit()

def eliminar_proveedor(ruc):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM Proveedor WHERE RUC=%s", (ruc,))
    mydb.commit()

def insertar_producto(id_producto, nombre, presentacion, stock, precio, marca):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO Producto VALUES (%s, %s, %s, %s, %s, %s)", (id_producto, nombre, presentacion, stock, precio, marca))
    mydb.commit()


def buscar_producto_por_nombre(nombre_producto):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Producto WHERE Nombre_Producto LIKE %s", ('%' + nombre_producto + '%',))
    return cursor.fetchall()


def consultar_productos():
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Producto")
    return cursor.fetchall()

def actualizar_producto(id_producto, nombre, presentacion, stock, precio, marca):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("UPDATE Producto SET Nombre_Producto=%s, Presentacion=%s, Stock_Actual=%s, Precio_Base=%s, Marca=%s WHERE ID_Producto=%s", (nombre, presentacion, stock, precio, marca, id_producto))
    mydb.commit()

def eliminar_producto(id_producto):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM Producto WHERE ID_Producto=%s", (id_producto,))
    mydb.commit()

def insertar_cliente(cedula, nombre, apellido, telefono, categoria, estado, direccion, cod_zona, cod_tarifa):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO Cliente VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (cedula, nombre, apellido, telefono, categoria, estado, direccion, cod_zona, cod_tarifa))
    mydb.commit()

def buscar_cliente_por_nombre_apellido(nombre_o_apellido):
    mydb = conectar()
    cursor = mydb.cursor()
    nombre, apellido = nombre_o_apellido.strip().split(" ", 1)
    cursor.execute("""
        SELECT * FROM Cliente
        WHERE Primer_Nombre LIKE %s AND Apellido LIKE %s
    """, ('%' + nombre + '%', '%' + apellido + '%'))
    return cursor.fetchall()


def consultar_clientes():
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Cliente")
    return cursor.fetchall()

def actualizar_cliente(cedula, nombre, apellido, telefono, categoria, estado, direccion, cod_zona, cod_tarifa):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("UPDATE Cliente SET Primer_Nombre=%s, Apellido=%s, Telefono=%s, Categoria=%s, Estado_cliente=%s, Direccion=%s, Cod_Zona=%s, Cod_Tarifa=%s WHERE Cedula=%s", (nombre, apellido, telefono, categoria, estado, direccion, cod_zona, cod_tarifa, cedula))
    mydb.commit()

def eliminar_cliente(cedula):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM Cliente WHERE Cedula=%s", (cedula,))
    mydb.commit()


def insertar_tarifa(id_tarifa, valor_base, cliente, fecha):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO Tarifa VALUES (%s, %s, %s, %s)", (id_tarifa, valor_base, cliente, fecha))
    mydb.commit()

def consultar_tarifas():
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Tarifa")
    return cursor.fetchall()

def actualizar_tarifa(id_tarifa, valor_base, cliente, fecha):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("UPDATE Tarifa SET Valor_Base=%s, Cliente=%s, Fecha_Tarifa=%s WHERE ID_Tarifa=%s", (valor_base, cliente, fecha, id_tarifa))
    mydb.commit()

def eliminar_tarifa(id_tarifa):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM Tarifa WHERE ID_Tarifa=%s", (id_tarifa,))
    mydb.commit()

def insertar_ruta(id_ruta, descripcion, estado, nombre):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO Ruta VALUES (%s, %s, %s, %s)", (id_ruta, descripcion, estado, nombre))
    mydb.commit()

def consultar_rutas():
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Ruta")
    return cursor.fetchall()

def actualizar_ruta(id_ruta, descripcion, estado, nombre):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("UPDATE Ruta SET Descripcion_Ruta=%s, Estado_Ruta=%s, Nombre_Ruta=%s WHERE ID_Ruta=%s", (descripcion, estado, nombre, id_ruta))
    mydb.commit()

def eliminar_ruta(id_ruta):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM Ruta WHERE ID_Ruta=%s", (id_ruta,))
    mydb.commit()

def insertar_recorrido(cod_zona, cod_ruta, estado):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO Recorrido VALUES (%s, %s, %s)", (cod_zona, cod_ruta, estado))
    mydb.commit()

def consultar_recorridos():
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Recorrido")
    return cursor.fetchall()

def actualizar_recorrido(cod_zona, cod_ruta, estado):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("UPDATE Recorrido SET Estado_Rec=%s WHERE Cod_Zona=%s AND Cod_Ruta=%s", (estado, cod_zona, cod_ruta))
    mydb.commit()

def eliminar_recorrido(cod_zona, cod_ruta):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM Recorrido WHERE Cod_Zona=%s AND Cod_Ruta=%s", (cod_zona, cod_ruta))
    mydb.commit()

def insertar_asignacion(cod_ruta, repartidor, estado, fecha, hora_inicio, hora_fin):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO Asignacion VALUES (%s, %s, %s, %s, %s, %s)", (cod_ruta, repartidor, estado, fecha, hora_inicio, hora_fin))
    mydb.commit()

def consultar_asignaciones():
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Asignacion")
    return cursor.fetchall()

def actualizar_asignacion(cod_ruta, repartidor, estado, fecha, hora_inicio, hora_fin):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("UPDATE Asignacion SET Estado_Asignacion=%s, Fecha_Asignacion=%s, Hora_Inicio=%s, Hora_Fin=%s WHERE Cod_Ruta=%s AND Repartidor=%s", (estado, fecha, hora_inicio, hora_fin, cod_ruta, repartidor))
    mydb.commit()

def eliminar_asignacion(cod_ruta, repartidor):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM Asignacion WHERE Cod_Ruta=%s AND Repartidor=%s", (cod_ruta, repartidor))
    mydb.commit()

def insertar_factura(id_factura, fecha, monto, estado, tipo, saldo, observaciones, repartidor, cliente):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO Factura VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id_factura, fecha, monto, estado, tipo, saldo, observaciones, repartidor, cliente))
    mydb.commit()

def consultar_facturas():
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Factura")
    return cursor.fetchall()

def actualizar_factura(id_factura, fecha, monto, estado, tipo, saldo, observaciones, repartidor, cliente):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("UPDATE Factura SET Fecha_Factura=%s, Monto_Total=%s, Estado=%s, Tipo_Venta=%s, Saldo_Pendiente=%s, Observaciones=%s, Repartidor=%s, Cliente=%s WHERE ID_Factura=%s", (fecha, monto, estado, tipo, saldo, observaciones, repartidor, cliente, id_factura))
    mydb.commit()

def eliminar_factura(id_factura):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM Factura WHERE ID_Factura=%s", (id_factura,))
    mydb.commit()

def insertar_pago(num_pago, fecha, metodo, monto, cod_factura):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO Pago VALUES (%s, %s, %s, %s, %s)", (num_pago, fecha, metodo, monto, cod_factura))
    mydb.commit()

def consultar_pagos():
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Pago")
    return cursor.fetchall()

def actualizar_pago(num_pago, fecha, metodo, monto, cod_factura):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("UPDATE Pago SET Fecha_Pago=%s, Metodo=%s, Monto=%s, Cod_Factura=%s WHERE Numero_Pago=%s", (fecha, metodo, monto, cod_factura, num_pago))
    mydb.commit()

def eliminar_pago(num_pago):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM Pago WHERE Numero_Pago=%s", (num_pago,))
    mydb.commit()

def insertar_detalle_factura(num_producto, cantidad, subtotal, cod_factura, cod_tarifa, cod_producto):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO Detalle_Factura VALUES (%s, %s, %s, %s, %s, %s)", (num_producto, cantidad, subtotal, cod_factura, cod_tarifa, cod_producto))
    mydb.commit()

def consultar_detalles_factura():
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Detalle_Factura")
    return cursor.fetchall()

def actualizar_detalle_factura(num_producto, cantidad, subtotal, cod_factura, cod_tarifa, cod_producto):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("UPDATE Detalle_Factura SET Cantidad=%s, Subtotal_Detalle=%s, Cod_Factura=%s, Cod_Tarifa=%s, Cod_Producto=%s WHERE Numero_de_producto=%s", (cantidad, subtotal, cod_factura, cod_tarifa, cod_producto, num_producto))
    mydb.commit()

def eliminar_detalle_factura(num_producto):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM Detalle_Factura WHERE Numero_de_producto=%s", (num_producto,))
    mydb.commit()

def insertar_detalle_compra(id_compra, cantidad, estado_pago, metodo_pago, fecha_compra, fecha_pago_compra, subtotal, provedor, encargado, cod_producto):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO Detalle_Compra VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (id_compra, cantidad, estado_pago, metodo_pago, fecha_compra, fecha_pago_compra, subtotal, provedor, encargado, cod_producto))
    mydb.commit()

def consultar_detalles_compra():
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Detalle_Compra")
    return cursor.fetchall()

def actualizar_detalle_compra(id_compra, cantidad, estado_pago, metodo_pago, fecha_compra, fecha_pago_compra, subtotal, provedor, encargado, cod_producto):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("UPDATE Detalle_Compra SET Cantidad=%s, Estado_Pago=%s, Metodo_Pago=%s, Fecha_Compra=%s, Fecha_Pago_Compra=%s, Subtotal_Detalle=%s, Provedor=%s, Encargado=%s, Cod_Producto=%s WHERE ID_Compra=%s", (cantidad, estado_pago, metodo_pago, fecha_compra, fecha_pago_compra, subtotal, provedor, encargado, cod_producto, id_compra))
    mydb.commit()

def eliminar_detalle_compra(id_compra):
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM Detalle_Compra WHERE ID_Compra=%s", (id_compra,))
    mydb.commit()