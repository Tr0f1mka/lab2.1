from logging import config, getLogger

from src.config import LOGGING_CONFIG

config.dictConfig(LOGGING_CONFIG)
logger = getLogger(__name__)
