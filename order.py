import pandas as pd
def update_file(file_path, data, order_list):
    """
    Actualiza un archivo CSV con las cantidades reducidas después de un pedido.

    Args:
        file_path (str): La ruta del archivo CSV que se va a actualizar.
        data (pd.DataFrame): Un DataFrame que contiene los datos del menú.
        order_list (list): Una lista de tuplas que representan los platos y
         cantidades seleccionados en el pedido.

    Returns:
        None
    """
    try:
        for order in order_list:
            index, cantidad = order
            cantidad_actual = data.at[index, 'Cantidad']
            data.at[index, 'Cantidad'] = cantidad_actual - cantidad
        data.to_csv(file_path, index=False)
        print("Archivo actualizado con las cantidades reducidas.")
    except (KeyError, pd.errors.EmptyDataError, pd.errors.ParserError, FileNotFoundError) as e:
        print(f"Ocurrió un error al actualizar el archivo: {e}")

def take_costumer_order(data):
    """
    Permite al cliente tomar pedidos seleccionando platos y cantidades.

    Args:
        data (pd.DataFrame): Un DataFrame que contiene los datos del menú.

    Returns:
        list: Una lista de tuplas que representan los platos y cantidades seleccionados.
    """
    order_list = []
    total_cantidad = 0

    try:
        while True:
            choice = int(input("Elige un plato por su índice el pedido (0 para finalizar): "))
            if choice == 0:
                break
            if 1 <= choice <= len(data):
                cantidad_disponible = data.at[choice - 1, 'Cantidad']
                cantidad = int(input(f"Ingresa la cantidad (hasta {cantidad_disponible}): "))
                if cantidad < 1 or cantidad > cantidad_disponible:
                    print("No válida. Debe ser al menos 1 y no mayor que la cantidad disponible.")
                elif total_cantidad + cantidad > 100:
                    print("¡El límite es de 100 comidas! Por favor, reduce la cantidad.")
                else:
                    total_cantidad += cantidad
                    order_list.append((choice - 1, cantidad))
            else:
                print("Índice inválido. Por favor, elige un plato válido.")
        return order_list
    except (ValueError, IndexError) as e:
        print(f"Ocurrió un error al tomar pedidos: {e}")
        return None

def calculate_base_cost():
    """
    Tarifa base del restaurante
    """
    return 5.0

def calculate_total(data, order_list):
    """
    Calcula el costo total de un pedido basado en los datos del menú y 
    la lista de platos seleccionados.

    Args:
        data (pd.DataFrame): Un DataFrame que contiene los datos del menú.
        order_list (list): Una lista de tuplas que representan los platos 
        y cantidades seleccionados.

    Returns:
        float: El costo total del pedido, incluyendo descuentos si corresponde.
    """
    total = 0
    total_cantidad = sum([cantidad for _, cantidad in order_list])
    print("Orden del cliente:")
    for order in order_list:
        index, cantidad = order
        plato = data.at[index, 'Nombre']
        precio_unitario = data.at[index, 'Precio']
        total_plato = precio_unitario * cantidad
        total += total_plato
        print(f"{plato} - Cant: {cantidad} - Prec Unit: ${precio_unitario} - Total: ${total_plato}")
    print (f"Servicio por la experiencia: {calculate_base_cost()}")
    if total > 50:
        total -= 10
    if total > 100:
        total -= 25
    total += calculate_base_cost()
    print(f"Subtotal: ${total}")
    if total_cantidad > 5:
        total *= 0.9
    if total_cantidad > 10:
        total *= 0.8
    print(f"Total con descuentos: ${total}")
    return total
def confirm_order(data, order_list):
    """
    Muestra los detalles del pedido, permite al usuario confirmar o cancelar el pedido.

    Args:
        data (pd.DataFrame): Un DataFrame que contiene los datos del menú.
        order_list (list): Una lista de tuplas que representan los platos 
        y cantidades seleccionados.

    Returns:
        bool: True si el usuario confirma el pedido, False si lo cancela.
    """
    try:
        print("Detalles del pedido:")
        for order in order_list:
            index, cantidad = order
            plato = data.at[index, 'Nombre']
            precio_unitario = data.at[index, 'Precio']
            total_plato = precio_unitario * cantidad
        print(f"{plato} - Cant: {cantidad} - PrecUnit: ${precio_unitario} - Total: ${total_plato}")
        costo_base = calculate_base_cost()
        total = calculate_total(data, order_list)
        print(f"Costo Base: ${costo_base}")
        print(f"Costo Total: ${total}")
        while True:
            confirmar = input("¿Deseas confirmar el pedido? (Sí/No): ").strip().lower()
            if confirmar == "si":
                return True
            if confirmar == "no":
                return False
            print("Respuesta no válida. Por favor, ingresa 'Sí' o 'No'.")
    except (ValueError, KeyError) as e:
        print(f"Ocurrió un error al confirmar el pedido: {e}")
        return None
