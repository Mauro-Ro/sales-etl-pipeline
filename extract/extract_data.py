from transform.validation import validator_extract
import requests
import pandas as pd


path_csv = "extract/data/Kaggle_Books-Selling-Records-.csv"

def extract(pd, path: str):
    return validator_extract(pd, path)




def request_path(path: str):
    return requests.get(path).json()

carts = request_path("https://dummyjson.com/carts")

users = request_path("https://dummyjson.com/users")

products = request_path("https://dummyjson.com/products")






