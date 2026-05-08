import logging
import sys

# Configure standard logging to output to stdout for Docker
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(message)s',
    datefmt='%H:%M:%S',
    stream=sys.stdout
)

def log_action(msg):
    logging.info(f"🔎 {msg}")

def log_text(msg):
    logging.info(f"❕ {msg}")

def log_warn(msg):
    logging.warning(f"⚠️ {msg}")

def log_error(msg):
    logging.error(f"❌ {msg}")
