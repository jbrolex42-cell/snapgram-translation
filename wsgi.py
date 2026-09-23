from libretranslate.app import create_app
from libretranslate.default_values import DEFAULT_ARGUMENTS


class Args:
    def __init__(self):
        for key, value in DEFAULT_ARGUMENTS.items():
            setattr(self, key, value)

        self.host = "0.0.0.0"
        self.port = 10000

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

        # Required by LibreTranslate's create_app().
        self.update_models = False
        self.force_update_models = False


app = create_app(Args())