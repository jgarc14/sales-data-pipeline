import logging
from pathlib import Path

from src.config import setup_logger
from src.extract import read_sales
from src.transform import clean_sales, aggregate_sales
from src.load import save_dataframe

def main():
    setup_logger()
    logging.info("Starting pipeline")

    df = read_sales("data/sales.csv")
    logging.info(f"Raw rows: {len(df)}")

    df_clean = clean_sales(df)
    logging.info(f"Clean rows: {len(df_clean)}")

    df_agg = aggregate_sales(df_clean)
    logging.info("Aggregation completed")

    output_path = Path("data") / "sales_aggregated.parquet"
    save_dataframe(df_agg, output_path)

    print(f"Saved to absolute path: {output_path.resolve()}")
    logging.info("Pipeline finished successfully")

if __name__ == "__main__":
    main()