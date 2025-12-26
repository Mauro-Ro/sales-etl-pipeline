from transform.cleaning import validar_nombre_columna, eliminar_columnas_basura
from extract.extract_data import path_csv, extract, pd

df = extract(pd, path_csv)

def main_pipeline(df):
    # df = limpiar_header(df) 
    df = eliminar_columnas_basura(df, validar_nombre_columna(df.columns))
    return df



if __name__ == "__main__":
    
    main_pipeline(df)
