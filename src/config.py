import logging

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='{"time":"%(asctime)s","level":"%(levelname)s","message":"%(message)s"}'
    )