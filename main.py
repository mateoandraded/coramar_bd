from coramar_base import *
from tabulate import tabulate


def menu_crud(nombre_tabla, insertar_func, consultar_func, actualizar_func, eliminar_func, campos_insertar,
              campos_actualizar, campos_eliminar, buscar_func=None, usar_sp=False):
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
            if usar_sp:

                if nombre_tabla == "Cliente" and usar_sp:

                    nombre_zona = datos[6]
                    cod_zona = obtener_id_zona_por_nombre_sp(nombre_zona)

                    if not cod_zona:
                        print("Error: Zona no encontrada")
                        print("Zonas disponibles:")
                        zonas = consultar_zonas()
                        for zona in zonas:
                            print(f"- {zona[1]}")
                        continue

                    datos_para_sp = datos[:5] + [datos[5]] + [cod_zona] + [datos[7]]
                    insertar_cliente_sp(*datos_para_sp)

                elif nombre_tabla == "Pago":
                    # numero_pago, fecha_pago, metodo, monto, cod_factura
                    registrar_pago_sp(*datos)
                elif nombre_tabla == "Detalle Compra":
                    # id_compra, cantidad, estado_pago, metodo_pago, fecha_compra, fecha_pago_compra, subtotal, proveedor, encargado, cod_producto
                    registrar_compra_sp(*datos)
                elif nombre_tabla == "Detalle Factura":
                    # num_producto, cantidad, subtotal, cod_factura, cod_producto
                    insertar_detalle_factura_sp(*datos)
            else:
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
                    if nombre_tabla == "Cliente":
                        nombre = input("Ingrese nombre: ")
                        apellido = input("Ingrese apellido: ")
                        registros = buscar_cliente_por_nombre_sp(nombre, apellido)
                    else:
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
            if nombre_tabla == "Cliente":
                nombre = input("Ingrese nombre del cliente: ")
                apellido = input("Ingrese apellido del cliente: ")
                eliminar_cliente_por_nombre_sp(nombre, apellido)
            else:
                datos = [input(f"Ingrese {campo}: ") for campo in campos_eliminar]
                eliminar_func(*datos)
            print(f"{nombre_tabla} eliminado correctamente.")

        elif opcion == "5":
            break
        else:
            print("Opción inválida.")


def menu_reportes():
    while True:
        print("\n=== REPORTES ===")
        print("1. Ventas por Zona")
        print("2. Deudas por Zona")
        print("3. Rendimiento de Repartidores")
        print("4. Inventario Crítico")
        print("5. Volver al Menú Principal")

        opcion = input("Seleccione un reporte: ")

        if opcion == "1":
            datos = consultar_ventas_por_zona()
            print("\n--- VENTAS POR ZONA ---")
            print(tabulate(datos, headers=["Zona", "Total Ventas", "N° Facturas"], tablefmt="grid"))

        elif opcion == "2":
            datos = consultar_deudas_por_zona()
            print("\n--- DEUDAS POR ZONA ---")
            print(tabulate(datos, headers=["Zona", "Total Deuda", "Facturas Pendientes"], tablefmt="grid"))

        elif opcion == "3":
            datos = consultar_rendimiento_repartidores()
            print("\n--- RENDIMIENTO DE REPARTIDORES ---")
            print(
                tabulate(datos, headers=["Nombre", "Apellido", "Pedidos Entregados", "Total Vendido"], tablefmt="grid"))

        elif opcion == "4":
            datos = consultar_inventario_critico()
            print("\n--- INVENTARIO CRÍTICO ---")
            print(tabulate(datos, headers=["Producto", "Stock Actual", "Proveedor", "Contacto"], tablefmt="grid"))

        elif opcion == "5":
            break
        else:
            print("Opción inválida, intente nuevamente.")

def menu_gestion_compras():
    while True:
        print("\n=== GESTIÓN DE COMPRAS ===")
        print("1. Registrar nueva compra a proveedor")
        print("2. Ver historial de compras")
        print("3. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_compra_interactivo()
        elif opcion == "2":
            registros = consultar_detalles_compra()
            campos_insertar = [
                "ID_Compra",
                "Cantidad",
                "Estado_Pago",
                "Metodo_Pago",
                "Fecha_Compra",
                "Fecha_Pago_Compra",
                "Subtotal_Detalle",
                "Provedor",
                "Encargado",
                "Cod_Producto"
            ]
            print(tabulate(registros, headers=campos_insertar, tablefmt="grid"))
        elif opcion == "3":
            break
        else:
            print("Opción inválida")


def registrar_compra_interactivo():
    """Interfaz interactiva para registrar compras"""
    print("\n--- REGISTRAR NUEVA COMPRA ---")

    # Mostrar proveedores activos
    print("\nProveedores disponibles:")
    proveedores = obtener_proveedores_activos()
    for p in proveedores:
        print(f"{p[0]} - {p[1]}")

    # Mostrar productos
    print("\nProductos disponibles:")
    productos = obtener_productos()
    for prod in productos:
        print(f"{prod[0]} - {prod[1]} - Precio: ${prod[2]} - Stock: {prod[3]}")

    # Capturar datos
    id_compra = input("\nIngrese ID de compra: ")
    proveedor = input("Ingrese RUC del proveedor: ")
    encargado = input("Ingrese cédula del encargado: ")
    cod_producto = input("Ingrese código del producto: ")
    cantidad = int(input("Ingrese cantidad: "))
    metodo_pago = input("Método de pago (Efectivo/Transferencia/Tarjeta): ")
    estado_pago = input("¿Pagado? (true/false): ").lower() in ('true', '1', 'si', 'yes')

    # Calcular subtotal (aquí podrías obtener el precio del producto)
    precio = obtener_precio_producto(cod_producto)
    subtotal = precio * cantidad if precio else 0

    # Fechas
    fecha_compra = input("Fecha de compra (YYYY-MM-DD): ")
    fecha_pago = input("Fecha de pago (YYYY-MM-DD) o dejar vacío: ")
    fecha_pago = fecha_pago if fecha_pago else None

    # Registrar compra
    try:
        registrar_compra_sp(id_compra, cantidad, estado_pago, metodo_pago,
                            fecha_compra, fecha_pago, subtotal, proveedor,
                            encargado, cod_producto)
    except Exception as e:
        print(f"Error al registrar compra: {e}")


def menu_ventas_productos():
    while True:
        print("\n=== VENTA DE PRODUCTOS ===")
        print("1. Consultar ventas")
        print("2. Registrar venta")
        print("3. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_consultar_ventas()
        elif opcion == "2":
            registrar_venta_unificada()
        elif opcion == "3":
            break
        else:
            print("Opción inválida")


def menu_consultar_ventas():
    print("\n--- CONSULTAR VENTAS ---")
    print("1. Buscar facturas por cliente")
    print("2. Mostrar todas las facturas")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cedula = input("Ingrese cédula del cliente: ")
        facturas = buscar_facturas_por_cliente(cedula)
        if facturas:
            headers = ["ID Factura", "Fecha", "Monto Total", "Estado", "Tipo Venta", "Saldo Pend", "Repartidor",
                       "Cliente", "Nombre"]
            print(tabulate(facturas, headers=headers, tablefmt="grid"))
        else:
            print("No se encontraron facturas para este cliente.")
    elif opcion == "2":
        facturas = consultar_facturas()
        if facturas:
            headers = ["ID Factura", "Fecha", "Monto Total", "Estado", "Tipo Venta", "Saldo Pend", "Observaciones",
                       "Repartidor", "Cliente"]
            print(tabulate(facturas, headers=headers, tablefmt="grid"))
        else:
            print("No hay facturas registradas.")


def registrar_venta_unificada():
    print("\n--- REGISTRAR VENTA ---")

    # Mostrar clientes
    print("\nClientes disponibles:")
    clientes = consultar_clientes()
    for c in clientes:
        print(f"{c[0]} - {c[1]} {c[2]}")

    # Mostrar productos
    print("\nProductos disponibles:")
    productos = obtener_productos()
    for p in productos:
        print(f"{p[0]} - {p[1]} - Precio: ${p[2]} - Stock: {p[3]}")

    # Mostrar repartidores
    print("\nRepartidores disponibles:")
    repartidores = consultar_empleados()
    for r in repartidores:
        if r[5] == 'Repartidor':  # Solo mostrar repartidores
            print(f"{r[0]} - {r[1]} {r[2]}")

    # Capturar datos
    cedula_cliente = input("\nIngrese cédula del cliente: ")
    cod_producto = input("Ingrese código del producto: ")
    cantidad = int(input("Ingrese cantidad: "))
    cedula_repartidor = input("Ingrese cédula del repartidor: ")
    tipo_venta = input("Tipo de venta (Contado/Credito): ")
    observaciones = input("Observaciones (opcional): ")
    try:
        factura_id, monto = registrar_venta(cedula_cliente, cod_producto, cantidad, cedula_repartidor, tipo_venta,
                                            observaciones)
        print("¡Venta registrada exitosamente!")
        print(f"Factura: {factura_id}")
        print(f"Monto: ${monto:.2f}")
    except Exception as e:
        print(f"Error al registrar venta: {e}")





def main():
    if not conectar():
        print("No se puede conectar a la base de datos. Saliendo...")
        return

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
        print("10. Ventas de productos")
        print("11. Pagos")
        print("12. Compras de Stock")
        print("13. Reportes")
        print("14. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_crud("Zona", insertar_zona, consultar_zonas, actualizar_zona, eliminar_zona,
                      ["ID_Zona", "Nombre_Zona", "Cantidad_Clientes", "Estado_Zona"],
                      ["ID_Zona", "Nombre_Zona", "Cantidad_Clientes", "Estado_Zona ('Activo', 'Inactivo')"],
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
                      ["Cedula", "Primer_Nombre", "Apellido", "Telefono", "Categoria", "Direccion", "Nombre_Zona",
                       "Cod_Tarifa"],
                      ["Cedula", "Primer_Nombre", "Apellido", "Telefono", "Categoria", "Estado_cliente", "Direccion",
                       "Cod_Zona", "Cod_Tarifa"],
                      ["Cedula"], buscar_func=buscar_cliente_por_nombre_apellido, usar_sp=True)

        elif opcion == "5":
            menu_crud("Empleado", insertar_empleado, consultar_empleados, actualizar_empleado, eliminar_empleado,
                      ["Cedula", "Primer_Nombre", "Apellido", "Telefono", "Cuenta_Bancaria", "Rol", "Estado_Empleado",
                       "ID_Encargado"],
                      ["Cedula", "Primer_Nombre", "Apellido", "Telefono", "Cuenta_Bancaria", "Rol", "Estado_Empleado",
                       "ID_Encargado"],
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
            menu_crud("Asignacion", insertar_asignacion, consultar_asignaciones, actualizar_asignacion,
                      eliminar_asignacion,
                      ["Cod_Ruta", "Repartidor", "Estado_Asignacion", "Fecha_Asignacion", "Hora_Inicio", "Hora_Fin"],
                      ["Cod_Ruta", "Repartidor", "Estado_Asignacion", "Fecha_Asignacion", "Hora_Inicio", "Hora_Fin"],
                      ["Cod_Ruta", "Repartidor"])

        elif opcion == "10":
            menu_ventas_productos()

        elif opcion == "11":
            menu_crud("Pago", insertar_pago, consultar_pagos, actualizar_pago, eliminar_pago,
                      ["Numero_Pago", "Fecha_Pago", "Metodo", "Monto", "Cod_Factura"],
                      ["Numero_Pago", "Fecha_Pago", "Metodo", "Monto", "Cod_Factura"],
                      ["Numero_Pago"], usar_sp=True)


        elif opcion == "12":
            menu_gestion_compras()

        # OPCIÓN 15: REPORTES - antes era 14
        elif opcion == "13":
            menu_reportes()

        # OPCIÓN 16: SALIR - antes era 15
        elif opcion == "14":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente nuevamente.")


if __name__ == "__main__":
    main()