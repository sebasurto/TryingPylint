import order
import menu

file_path = "meals.csv"

def system_restaurant ():
    menu_data = menu.print_menu(file_path)
    order_list = order.take_costumer_order(menu_data)
    order.calculate_total(menu_data, order_list)
    order.update_file(file_path, menu_data, order_list)
    