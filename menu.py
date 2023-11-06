import pandas as pd

def print_menu(path):
    """
    Muestra el menú a partir de un archivo CSV y devuelve los datos del menú.

    Args:
        file_path (str): La ruta del archivo CSV que contiene el menú.

    Returns:
        pd.DataFrame: Un DataFrame que contiene los datos del menú.
    """
    try:
        data = pd.read_csv(path)
        print("Menú:")
        for index, row in data.iterrows():
            print(f"{index + 1}. {row['Nombre']} -Prec:${row['Precio']}-CantDisp:{row['Cantidad']}")
        return data
    except (FileNotFoundError, pd.errors.EmptyDataError) as e:
        print(f"Ocurrió un error al mostrar el menú: {e}")
        return None