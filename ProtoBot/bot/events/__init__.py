from .ready import load_ready
from .errors import load_errors


def load_events(bot):
    load_ready(bot)
    load_errors(bot)