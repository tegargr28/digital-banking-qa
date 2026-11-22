import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv(
    "BASE_URL",
    "https://parabank.parasoft.com/parabank/index.htm",
)
BROWSER = os.getenv("BROWSER", "chrome").lower()
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

# Public ParaBank demo account, published by Parasoft for the demo site.
# These are not real banking credentials; override via environment if needed.
PARABANK_USERNAME = os.getenv("PARABANK_USERNAME", "john")
PARABANK_PASSWORD = os.getenv("PARABANK_PASSWORD", "demo")
