import pandas as pd

path_csv = "extract/data/Kaggle_Books-Selling-Records-.csv"

def extract(path: str):
    return pd.read_csv(path)

df = extract(path_csv)

# def extract_data()
