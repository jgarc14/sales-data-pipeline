import pandera.pandas as pa
from pandera import Column, DataFrameSchema
import pandas as pd

sales_schema = DataFrameSchema({
    "product": Column(str),
    "amount": Column(float, checks=pa.Check.ge(0)),
})

def validate_sales(df: pd.DataFrame) -> pd.DataFrame:
    return sales_schema.validate(df)

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