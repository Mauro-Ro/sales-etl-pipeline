from extract.extract_data import df

def iterar_columns(columns)->list:
    """Iterador de columnas que guarda el nombre de todas las columnas
        en una lista y despues las retorna.

    Args:
        columns (Any): Aca ingresamos todas las columnas.

    Returns:
        list: La lista con todas las columnas existentes.
    """
    list_columns = []
    for i in range(len(columns)):
        list_columns.append(columns[i])
    return list_columns

 

def validator_rows_column(filas: int, columns: list):
    """Es un validador de filas segun una lista de columnas

    Args:
        filas (int): Cantidad de filas a validar.
        columns (list): Lista de columnas. 

    Returns:
        _type_: _description_
    """
    matriz_filas = []
    for i in range(len(columns)):
        for k in range(filas):
            matriz_filas.append([df.iloc[k, i]])
    # matriz_filas.append([df.iloc[filas, columns]])

    return matriz_filas



def validator_column(columns):
    pass


# Agregar un validador que verifique que filas estan vacias o nullas o Nan