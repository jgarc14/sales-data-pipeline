import pandas as pd

def read_sales(path: str) -> pd.DataFrame:
    return pd.read_csv(path, parse_dates=["order_date"])