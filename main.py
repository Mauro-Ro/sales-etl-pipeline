# from transform.cleaning import 
from transform.validation import validator_rows_column, iterar_columns
from extract.extract_data import *

if __name__ == "__main__":
    # print(all_columns)
    # df = extract(path_csv)

    all_columns = iterar_columns(df.columns)

    # print(all_columns)
    print(validator_rows_column(4, all_columns))


    # print(iterar_columns(df.columns))

    # print(iterar_columns(df.rows))
