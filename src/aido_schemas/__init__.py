__version__ = "5.0.59"

from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)
logger.info(f"aido-protocols {__version__}")

from .protocols import *
from .protocol_agent import *
from .protocol_simulator import *
from .schemas import *
