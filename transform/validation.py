import pandas as pd
"""Validacion de estructura minima

1-Hay columnas?

2-Hay header?

3-El archivo no esta vacio?

4-Existe la ruta del archivo?

en caso de ser una de las opciones, se rechaza el CSV.
"""

def validator_extract(pd, path: str):
    try:
        df = pd.read_csv(path)
        if len(df.columns) <= 3:
            print(f"Archivo valido pero sin columnas o muy pocas: {len(df.columns)} \n")
        else:
            print("Archivo cargado correctamente\n")
            return df
    except FileNotFoundError:
        print("No se encuentra la ruta del archivo\n")        
    except pd.errors.EmptyDataError:
        print("El archivo esta vacio\n")




# Agregar un validador que verifique que filas estan vacias o nullas o Nan

def validator_rows_column(df, filas: int, columns: list):
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
            # print(f"Valor del indice de la columna {i}: ", df.iloc[k, i])
            matriz_filas.append([df.iloc[k, i]])
    print(matriz_filas)
    # matriz_filas.append([df.iloc[filas, columns]])

    # return matriz_filas

