import time
import pandas as pd
import tracemalloc

FILE = "data/sales_large.csv"


def benchmark_full_load_default():
    start = time.time()
    tracemalloc.start()

    df = pd.read_csv(FILE)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    duration = time.time() - start
    return duration, peak / 10**6


def benchmark_full_load_optimized():
    start = time.time()
    tracemalloc.start()

    dtypes = {
        "order_id": "int64",
        "customer_id": "int32",
        "product": "category",
        "category": "category",
        "amount": "float32",
    }

    df = pd.read_csv(
        FILE,
        dtype=dtypes,
        parse_dates=["order_date"]
    )

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    duration = time.time() - start
    return duration, peak / 10**6


def benchmark_chunked():
    start = time.time()
    tracemalloc.start()

    dtypes = {
        "order_id": "int64",
        "customer_id": "int32",
        "product": "category",
        "category": "category",
        "amount": "float32",
    }

    chunks = pd.read_csv(
        FILE,
        chunksize=100_000,
        dtype=dtypes,
        parse_dates=["order_date"]
    )

    total_rows = 0

    for chunk in chunks:
        total_rows += len(chunk)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    duration = time.time() - start
    return duration, peak / 10**6


if __name__ == "__main__":
    print("Running benchmarks...\n")

    t1, m1 = benchmark_full_load_default()
    print(f"Full Load Default → Time: {t1:.2f}s | Peak Memory: {m1:.2f} MB")

    t2, m2 = benchmark_full_load_optimized()
    print(f"Full Load Optimized → Time: {t2:.2f}s | Peak Memory: {m2:.2f} MB")

    t3, m3 = benchmark_chunked()
    print(f"Chunked Optimized → Time: {t3:.2f}s | Peak Memory: {m3:.2f} MB")