from transform.validation import validator_extract
import pandas as pd


path_csv = "extract/data/Kaggle_Books-Selling-Records-.csv"

def extract(pd, path: str):
    return validator_extract(pd, path)



