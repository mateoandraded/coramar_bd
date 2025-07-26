import mysql.connector

def conectar() :
    mydb = mysql.connector.connect(
        host="3.89.158.117",
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
