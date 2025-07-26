import mysql.connector
from coramar_base import *


def mostrar_clientes(clientes):
    print("\nClientes:")
    print("| Cedula     | Nombre        | Apellido      | Telefono    | Categoria   | Estado Cliente |")
    print("|------------|---------------|---------------|-------------|-------------|----------------|")
    for cliente in clientes:
        print(
            f"| {cliente[0]:<10} | {cliente[1]:<13} | {cliente[2]:<13} | {cliente[3]:<11} | {cliente[4]:<11} | {cliente[5]:<14} |")
    print("\n")


def mostrar_facturas(facturas):
    print("\nFacturas:")
    print("| ID Factura | Fecha       | Monto Total | Estado   | Tipo Venta | Saldo Pendiente | Cliente |")
    print("|------------|-------------|-------------|----------|------------|-----------------|---------|")
    for factura in facturas:
        print(
            f"| {factura[0]:<10} | {factura[1]:<11} | {factura[2]:<12} | {factura[3]:<8} | {factura[4]:<10} | {factura[5]:<15} | {factura[6]:<7} |")
    print("\n")
