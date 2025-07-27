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