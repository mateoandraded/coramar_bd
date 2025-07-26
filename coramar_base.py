import mysql.connector

def conectar() :
    mydb = mysql.connector.connect(
        host="3.89.158.117",
        user="coramar_bd",
        passwd="Adinroot12*",
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