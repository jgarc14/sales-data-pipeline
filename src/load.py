def save_dataframe(df, path: str):
    df.to_csv(path, index=False)