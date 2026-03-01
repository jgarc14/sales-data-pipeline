import logging
from pathlib import Path

import pandas as pd

from src.config import setup_logger
from src.extract import read_sales_large
from src.transform import clean_sales, aggregate_sales, validate_sales
from src.load import save_dataframe

def main():
    setup_logger()
    logging.info("Starting pipeline")

    frames = []

    for chunk in read_sales_large("data/sales.csv"):

        invalid_rows = chunk[chunk["amount"] < 0]

        if not invalid_rows.empty:
            logging.warning(
                f"Found {len(invalid_rows)} negative amounts"
            )
            invalid_rows.to_parquet(
                "data/invalid_sales.parquet",
                index=False,
                compression="snappy"
            )
        # eliminamos solo los inválidos
        chunk = chunk[chunk["amount"] >= 0]

        validated = validate_sales(chunk)
        cleaned = clean_sales(validated)
        logging.info(f"Clean rows: {len(cleaned)}")
        frames.append(cleaned)

    df_all = pd.concat(frames, ignore_index=True)
    df_agg = aggregate_sales(df_all)
    logging.info("Aggregation completed")

    output_path = Path("data") / "sales_aggregated.parquet"
    save_dataframe(df_agg, output_path)

    print(f"Saved to absolute path: {output_path.resolve()}")
    logging.info("Pipeline finished successfully")

if __name__ == "__main__":
    main()