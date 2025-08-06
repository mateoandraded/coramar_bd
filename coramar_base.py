import mysql.connector

def conectar() :
    mydb = mysql.connector.connect(
        host="54.145.65.73",
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