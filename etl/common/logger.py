import logging


def get_logger(name: str):

    logger = logging.getLogger(name)

    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        console = logging.StreamHandler()
        console.setFormatter(formatter)

        logger.addHandler(console)

        logger.setLevel(logging.INFO)

    return logger