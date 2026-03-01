import pandas as pd
from src.transform import clean_sales

def test_clean_sales():
    data = {
        "order_id": [1, 2],
        "product": ["Laptop", None],
        "amount": [100, -50]
    }

    df = pd.DataFrame(data)
    result = clean_sales(df)

    assert len(result) == 1