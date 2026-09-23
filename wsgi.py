import sys

from libretranslate.main import get_args
from libretranslate.app import create_app

sys.argv = [
    "libretranslate",
    "--host", "0.0.0.0",
    "--port", "10000",
    "--load-only", "en,sw,fr",
    "--threads", "1",
]

args = get_args()
app = create_app(args)