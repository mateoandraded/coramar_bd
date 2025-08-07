from coramar_base import *
from tabulate import tabulate

def menu_crud(nombre_tabla, insertar_func, consultar_func, actualizar_func, eliminar_func, campos_insertar, campos_actualizar, campos_eliminar, buscar_func=None):
    while True:
        print(f"\n--- {nombre_tabla} ---")
        print("1. Insertar")
        print("2. Consultar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            datos = [input(f"Ingrese {campo}: ") for campo in campos_insertar]
            insertar_func(*datos)
            print(f"{nombre_tabla} insertado correctamente.")

        elif opcion == "2":
            if buscar_func:
                print("\n1. Ver todos")
                print("2. Buscar por nombre")
                subop = input("Seleccione una opción: ")
                if subop == "1":
                    registros = consultar_func()
                elif subop == "2":
                    nombre = input("Ingrese nombre completo: ")
                    registros = buscar_func(nombre)
                else:
                    print("Opción inválida.")
                    continue
            else:
                registros = consultar_func()

            if registros:
                print(tabulate(registros, headers=campos_insertar, tablefmt="grid"))
            else:
                print("No hay registros.")

        elif opcion == "3":
            datos = [input(f"Ingrese {campo}: ") for campo in campos_actualizar]
            actualizar_func(*datos)
            print(f"{nombre_tabla} actualizado correctamente.")

        elif opcion == "4":
            datos = [input(f"Ingrese {campo}: ") for campo in campos_eliminar]
            eliminar_func(*datos)
            print(f"{nombre_tabla} eliminado correctamente.")

        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

def main():
    while True:
        print("\n=== MENÚ PRINCIPAL CORAMAR ===")
        print("1. Zonas")
        print("2. Proveedores")
        print("3. Productos")
        print("4. Clientes")
        print("5. Empleados")
        print("6. Tarifas")
        print("7. Rutas")
        print("8. Recorridos")
        print("9. Asignaciones")
        print("10. Facturas")
        print("11. Pagos")
        print("12. Detalles de Factura")
        print("13. Detalles de Compra")
        print("14. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_crud("Zona", insertar_zona, consultar_zonas, actualizar_zona, eliminar_zona,
                      ["ID_Zona", "Nombre_Zona", "Cantidad_Clientes", "Estado_Zona"],
                      ["ID_Zona", "Nombre_Zona", "Cantidad_Clientes", "Estado_Zona"],
                      ["ID_Zona"], buscar_func=buscar_zona_por_nombre)

        elif opcion == "2":
            menu_crud("Proveedor", insertar_proveedor, consultar_proveedores, actualizar_proveedor, eliminar_proveedor,
                      ["RUC", "Nombre_Proveedor", "Dir_Proveedor", "Contacto_Proveedor", "Correo", "Estado_Proveedor"],
                      ["RUC", "Nombre_Proveedor", "Dir_Proveedor", "Contacto_Proveedor", "Correo", "Estado_Proveedor"],
                      ["RUC"], buscar_func=buscar_proveedor_por_nombre)

        elif opcion == "3":
            menu_crud("Producto", insertar_producto, consultar_productos, actualizar_producto, eliminar_producto,
                      ["ID_Producto", "Nombre_Producto", "Presentacion", "Stock_Actual", "Precio_Base", "Marca"],
                      ["ID_Producto", "Nombre_Producto", "Presentacion", "Stock_Actual", "Precio_Base", "Marca"],
                      ["ID_Producto"], buscar_func=buscar_producto_por_nombre)

        elif opcion == "4":
            menu_crud("Cliente", insertar_cliente, consultar_clientes, actualizar_cliente, eliminar_cliente,
                      ["Cedula", "Primer_Nombre", "Apellido", "Telefono", "Categoria", "Estado_cliente", "Direccion", "Cod_Zona", "Cod_Tarifa"],
                      ["Cedula", "Primer_Nombre", "Apellido", "Telefono", "Categoria", "Estado_cliente", "Direccion", "Cod_Zona", "Cod_Tarifa"],
                      ["Cedula"], buscar_func=buscar_cliente_por_nombre_apellido)

        elif opcion == "5":
            menu_crud("Empleado", insertar_empleado, consultar_empleados, actualizar_empleado, eliminar_empleado,
                      ["Cedula", "Primer_Nombre", "Apellido", "Telefono", "Cuenta_Bancaria", "Rol", "Estado_Empleado", "ID_Encargado"],
                      ["Cedula", "Primer_Nombre", "Apellido", "Telefono", "Cuenta_Bancaria", "Rol", "Estado_Empleado", "ID_Encargado"],
                      ["Cedula"], buscar_func=buscar_empleado_por_nombre_apellido)

        elif opcion == "6":
            menu_crud("Tarifa", insertar_tarifa, consultar_tarifas, actualizar_tarifa, eliminar_tarifa,
                      ["ID_Tarifa", "Valor_Base", "Cliente", "Fecha_Tarifa"],
                      ["ID_Tarifa", "Valor_Base", "Cliente", "Fecha_Tarifa"],
                      ["ID_Tarifa"])

        elif opcion == "7":
            menu_crud("Ruta", insertar_ruta, consultar_rutas, actualizar_ruta, eliminar_ruta,
                      ["ID_Ruta", "Descripcion_Ruta", "Estado_Ruta", "Nombre_Ruta"],
                      ["ID_Ruta", "Descripcion_Ruta", "Estado_Ruta", "Nombre_Ruta"],
                      ["ID_Ruta"])

        elif opcion == "8":
            menu_crud("Recorrido", insertar_recorrido, consultar_recorridos, actualizar_recorrido, eliminar_recorrido,
                      ["Cod_Zona", "Cod_Ruta", "Estado_Rec"],
                      ["Cod_Zona", "Cod_Ruta", "Estado_Rec"],
                      ["Cod_Zona", "Cod_Ruta"])

        elif opcion == "9":
            menu_crud("Asignacion", insertar_asignacion, consultar_asignaciones, actualizar_asignacion, eliminar_asignacion,
                      ["Cod_Ruta", "Repartidor", "Estado_Asignacion", "Fecha_Asignacion", "Hora_Inicio", "Hora_Fin"],
                      ["Cod_Ruta", "Repartidor", "Estado_Asignacion", "Fecha_Asignacion", "Hora_Inicio", "Hora_Fin"],
                      ["Cod_Ruta", "Repartidor"])

        elif opcion == "10":
            menu_crud("Factura", insertar_factura, consultar_facturas, actualizar_factura, eliminar_factura,
                      ["ID_Factura", "Fecha_Factura", "Monto_Total", "Estado", "Tipo_Venta", "Saldo_Pendiente", "Observaciones", "Repartidor", "Cliente"],
                      ["ID_Factura", "Fecha_Factura", "Monto_Total", "Estado", "Tipo_Venta", "Saldo_Pendiente", "Observaciones", "Repartidor", "Cliente"],
                      ["ID_Factura"])

        elif opcion == "11":
            menu_crud("Pago", insertar_pago, consultar_pagos, actualizar_pago, eliminar_pago,
                      ["Numero_Pago", "Fecha_Pago", "Metodo", "Monto", "Cod_Factura"],
                      ["Numero_Pago", "Fecha_Pago", "Metodo", "Monto", "Cod_Factura"],
                      ["Numero_Pago"])

        elif opcion == "12":
            menu_crud("Detalle Factura", insertar_detalle_factura, consultar_detalles_factura, actualizar_detalle_factura, eliminar_detalle_factura,
                      ["Numero_de_producto", "Cantidad", "Subtotal_Detalle", "Cod_Factura", "Cod_Tarifa", "Cod_Producto"],
                      ["Numero_de_producto", "Cantidad", "Subtotal_Detalle", "Cod_Factura", "Cod_Tarifa", "Cod_Producto"],
                      ["Numero_de_producto"])

        elif opcion == "13":
            menu_crud("Detalle Compra", insertar_detalle_compra, consultar_detalles_compra, actualizar_detalle_compra, eliminar_detalle_compra,
                      ["ID_Compra", "Cantidad", "Estado_Pago", "Metodo_Pago", "Fecha_Compra", "Fecha_Pago_Compra", "Subtotal_Detalle", "Provedor", "Encargado", "Cod_Producto"],
                      ["ID_Compra", "Cantidad", "Estado_Pago", "Metodo_Pago", "Fecha_Compra", "Fecha_Pago_Compra", "Subtotal_Detalle", "Provedor", "Encargado", "Cod_Producto"],
                      ["ID_Compra"])

        elif opcion == "14":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    main()
