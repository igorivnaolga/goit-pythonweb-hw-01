import logging
import sys

# Configure global logger
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    stream=sys.stdout,
    force=True,
)

logger = logging.getLogger(__name__)
