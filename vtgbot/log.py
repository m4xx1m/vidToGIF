from loguru import logger

logger.add("warning.log", level="WARNING", rotation="100 MB")
logger.add("debug.log", level="DEBUG", rotation="100 MB")
