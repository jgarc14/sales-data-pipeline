import pandas as pd
from typing import Iterator

def read_sales(path: str) -> pd.DataFrame:
    return pd.read_csv(path, parse_dates=["order_date"])

def read_sales_large(path: str, chunk_size: int = 100_000) -> Iterator[pd.DataFrame]:
    return pd.read_csv(path, chunksize=chunk_size)