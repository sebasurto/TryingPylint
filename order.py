import pandas as pd
import menu

def update_file(file_path, data, order_list):
    try:
        for order in order_list:
            index, cantidad = order
            cantidad_actual = data.at[index, 'Cantidad']
            data.at[index, 'Cantidad'] = cantidad_actual - cantidad
        data.to_csv(file_path, index=False)
        print("Archivo actualizado con las cantidades reducidas.")
    except Exception as e:
        print(f"Ocurrió un error al actualizar el archivo: {e}")

def take_costumer_order(data):
    order_list = []
    try:
        while True:
            choice = int(input("Elige un plato por su índice para agregar al pedido (0 para finalizar): "))
            if choice == 0:
                break
            elif 1 <= choice <= len(data):
                cantidad_disponible = data.at[choice - 1, 'Cantidad']
                cantidad = int(input(f"Ingresa la cantidad que deseas (hasta {cantidad_disponible}): "))
                if cantidad < 1 or cantidad > cantidad_disponible:
                    print("Cantidad no válida. Debe ser al menos 1 y no mayor que la cantidad disponible.")
                else:
                    order_list.append((choice - 1, cantidad))
            else:
                print("Índice inválido. Por favor, elige un plato válido.")
        return order_list
    except Exception as e:
        print(f"Ocurrió un error al tomar pedidos: {e}")

def calculate_base_cost():
    return 5.0

def calculate_total(data, order_list):
    total = 0
    print("Orden del cliente:")
    for order in order_list:
        index, cantidad = order
        plato = data.at[index, 'Nombre']
        precio_unitario = data.at[index, 'Precio']
        total_plato = precio_unitario * cantidad
        total += total_plato
        print(f"{plato} - Cantidad: {cantidad} - Precio Unitario: ${precio_unitario} - Total: ${total_plato}")
    print (f"Servicio por la experiencia: {calculate_base_cost()}")
    total += calculate_base_cost()  
    print(f"Subtotal: ${total}")
    if len(order_list) > 5:
        total *= 0.9  
    if len(order_list) > 10:
        total *= 0.8  
    print(f"Total con descuentos: ${total}")
    return total