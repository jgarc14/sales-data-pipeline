import pandas as pd

def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # eliminar montos negativos
    df = df[df["amount"] > 0]

    # eliminar productos nulos
    df = df[df["product"].notna()]

    return df


def aggregate_sales(df: pd.DataFrame) -> pd.DataFrame:
    result = (
        df.groupby("category")
        .agg(
            total_sales=("amount", "sum"),
            avg_sales=("amount", "mean"),
            total_orders=("order_id", "count"),
        )
        .reset_index()
    )

    return result