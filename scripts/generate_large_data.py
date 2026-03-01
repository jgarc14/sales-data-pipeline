import pandas as pd
import numpy as np

def generate_data(rows: int = 1_000_000):
    df = pd.DataFrame({
        "product": np.random.choice(["A", "B", "C", "D"], rows),
        "amount": np.random.uniform(10, 500, rows),
        "quantity": np.random.randint(1, 10, rows),
    })

    df.to_csv("data/sales_large.csv", index=False)

if __name__ == "__main__":
    generate_data()