from libretranslate.app import create_app
from libretranslate.default_values import DEFAULT_ARGUMENTS


class Args:
    def __init__(self):
        # Load every LibreTranslate default argument.
        for key, value in DEFAULT_ARGUMENTS.items():
            setattr(self, key, value)

        # Render's HTTP server settings.
        self.host = "0.0.0.0"
        self.port = 10000

        # Languages to make available.
        self.load_only = [
            "en",
            "sw",
            "fr",
            "es",
            "de",
            "pt",
            "it",
            "ar",
            "hi",
            "zh",
            "ja",
            "ko",
            "ru",
            "nl",
            "tr",
        ]


app = create_app(Args())