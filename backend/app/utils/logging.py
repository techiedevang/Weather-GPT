import logging
import sys

def setup_logging():
    """
    Configures structured JSON-like logging for production observability.
    """
    logger = logging.getLogger("weathergpt")
    logger.setLevel(logging.INFO)
    
    # Avoid duplicate logs if already configured
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        
        # Production style formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    return logger

logger = setup_logging()
