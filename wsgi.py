from libretranslate.app import create_app
from libretranslate.default_values import DEFAULT_ARGUMENTS


class Args:
    def __init__(self):
        # Load LibreTranslate's default arguments first so we always have
        # every attribute the installed version's boot()/create_app() expects
        for key, value in DEFAULT_ARGUMENTS.items():
            setattr(self, key, value)

        # Render configuration
        self.host = "0.0.0.0"
        self.port = 10000

        # Translation languages
        # IMPORTANT: each language here pulls in a translation model (roughly
        # 50-150MB each) for its pair(s) with English. On a 512Mi instance
        # you have room for only a handful of languages before you hit OOM
        # before the server ever binds its port. Start small, confirm it
        # boots and stays under the memory limit, then add languages back
        # one at a time while watching memory usage in the Render dashboard.
        self.load_only = [
            "en",
            "sw",
            "fr",
        ]

        # Keep threads at 1 - each thread/worker can load its own copy of
        # models, which multiplies memory usage on a constrained instance
        self.threads = 1

        # Prevent model updates/downloads during every web-service startup
        self.update_models = False
        self.force_update_models = False


app = create_app(Args())