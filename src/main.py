import logging
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

    save_dataframe(df_agg, "data/sales_aggregated.parquet")
    logging.info("Pipeline finished successfully")

if __name__ == "__main__":
    main()