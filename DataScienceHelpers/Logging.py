import logging
import os


def get_logger(path, file):
    """Creates a file to log into it and sets-up a logger.
    Args:
        path (string) -- log file folder path.
        file (string) -- log file name.
    Returns:
        [obj] -- logger.
    """
    log_file = os.path.join(path, file)
    if not os.path.isfile(log_file):
        open(log_file, "w+").close()
  
    file_logging_format = "%(levelname)s: %(asctime)s: %(message)s"
  
    logging.basicConfig(
        level=logging.INFO, 
        format = file_logging_format
    )
    logger = logging.getLogger()
  
    handler = logging.FileHandler(log_file)
    handler.setLevel(logging.INFO)  
    formatter = logging.Formatter(file_logging_format)
    handler.setFormatter(formatter)
  
    logger.addHandler(handler)
    return logger