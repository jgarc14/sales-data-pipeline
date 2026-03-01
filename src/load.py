def save_dataframe(df, path: str):
    df.to_parquet(path, index=False)