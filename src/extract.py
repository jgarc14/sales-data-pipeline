import pandas as pd
from typing import Iterator

def read_sales(path: str) -> pd.DataFrame:
    return pd.read_csv(path, parse_dates=["order_date"])

def read_sales_large(path: str, chunk_size: int = 100_000):
    dtypes = {
        "order_id": "int64",
        "customer_id": "int64",
        "product": "category",
        "category": "category",
        "amount": "float64",
    }

    return pd.read_csv(
        path,
        chunksize=chunk_size,
        dtype=dtypes,
        parse_dates=["order_date"]
    )