# src/logger.py
import logging
import os
import time

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Set up and return a logger.

    Args:
        name (str): The name of the logger.
        level (int): The logging level.

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Ensure the logs directory exists
    if not os.path.exists("logs/"):
        os.makedirs("logs/" )

    # Creates a timestamped log path
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    log_path = os.path.join("logs", f"{timestamp}_{name}.log")

    # Creates logger and set its level
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Formatter for log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # File handler
    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

# Example usage:
# logger = setup_logger("data_processing")
# logger.info("This is an info message")
