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


def mostrar_repartidores(repartidores):
    print("\nRepartidores y Asignaciones:")
    print("| Cedula     | Primer Nombre | Apellido     | Total Repartos |")
    print("|------------|----------------|--------------|----------------|")
    for repartidor in repartidores:
        print(f"| {repartidor[0]:<10} | {repartidor[1]:<14} | {repartidor[2]:<12} | {repartidor[3]:<14} |")
    print("\n")


def main():
    while True:
        print("\n------------------------------")
        print("       MENÚ PRINCIPAL")
        print("------------------------------")
        print("1. Ver Clientes")
        print("2. Ver Facturas")
        print("3. Ver Repartidores")
        print("4. Ingresar Nuevo Cliente")
        print("5. Salir")
        print("------------------------------")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            clientes = get_clientes()
            mostrar_clientes(clientes)

        elif opcion == '2':
            facturas = get_factura()
            mostrar_facturas(facturas)

        elif opcion == '3':
            repartidores = get_repartidores()
            mostrar_repartidores(repartidores)

        elif opcion == '4':
            ingresar_cliente()

        elif opcion == '5':
            print("Saliendo...")
            break

        else:
            print("Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    main()