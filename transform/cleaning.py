
"""Limpieza estructural del header 

1-Eliminar columnas Unnamed:*

2-Eliminar espacios invisibles

3-Eliminar saltos de línea

headers corruptos
"""



def validar_nombre_columna(columns):
    """Validador de Nombres de Columnas, verifica si esta vacia o es "Unnamed"

    Args:
        columns (Any): Aca ingresamos todas las columnas.

    Returns:
        _type_: Retorna una lista de los indices de las columnas que estan vacias o se llaman "Unnamed".
    """    
    lista_validada = []
    for i in range(len(columns)):
        if(columns[i].strip() == "" or columns[i].startswith('Unnamed')):
            lista_validada.append(columns[i])

    return lista_validada


def eliminar_columnas_basura(df, columnas: list):
    for i in range(len(columnas)):
        print(f"Columna eliminada: {columnas[i]}")
        df = df.drop(columns=[columnas[i]])
    return df

