from libretranslate.app import create_app
from libretranslate.default_values import DEFAULT_ARGUMENTS


class Args:
    def __init__(self):
        # Load LibreTranslate's default arguments first
        for key, value in DEFAULT_ARGUMENTS.items():
            setattr(self, key, value)

        # Render configuration
        self.host = "0.0.0.0"
        self.port = 10000

        # Translation languages
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

        # Prevent model updates during every web-service startup
        self.update_models = False
        self.force_update_models = False


app = create_app(Args())