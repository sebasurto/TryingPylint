import pandas as pd

def print_menu(path):
    try:
        data = pd.read_csv(path)
        print("Menú:")
        for index, row in data.iterrows():
            print(f"{index + 1}. {row['Nombre']} - Precio: ${row['Precio']} - Cantidad disponible: {row['Cantidad']}")
        return data
    except Exception as e:
        print(f"Ocurrió un error al mostrar el menú: {e}")


