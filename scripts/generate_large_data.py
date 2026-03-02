import pandas as pd
import numpy as np

def generate_data(rows: int = 1_000_000):
    df = pd.DataFrame({
        "order_id": np.arange(rows),
        "customer_id": np.random.randint(1, 10000, rows),
        "order_date": pd.date_range(
            start="2024-01-01",
            periods=rows,
            freq="min"
        ),
        "product": np.random.choice(["A", "B", "C", "D"], rows),
        "category": np.random.choice(["Tech", "Home", "Sports"], rows),
        "amount": np.random.uniform(10, 500, rows),
    })

    df.to_csv("data/sales_large.csv", index=False)

if __name__ == "__main__":
    generate_data()