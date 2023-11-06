import order
import menu

FILE_PATH = "meals.csv"

def system_restaurant ():
    """
    Gestiona el sistema de un restaurante, permitiendo a los clientes
    seleccionar platos y realizar pedidos.

    Esta función realiza las siguientes acciones:
    1. Muestra el menú al cliente.
    2. Permite al cliente seleccionar platos y cantidades.
    3. Muestra los detalles del pedido y permite al cliente confirmar o cancelar.
    4. Actualiza el archivo con las cantidades reducidas si el pedido es confirmado.

    Args:
        No recibe argumentos directamente, pero depende de las funciones
        del módulo "menu" y "order".

    Returns:
        None
    """
    menu_data = menu.print_menu(FILE_PATH)
    order_list = order.take_costumer_order(menu_data)
    if order_list:
        if order.confirm_order(menu_data, order_list):
            order.update_file(FILE_PATH, menu_data, order_list)
        else:
            print("Pedido cancelado.")
    else:
        print("No se han realizado pedidos.")
    