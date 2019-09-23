from order.settings import config
from .startup import AppStartup


application = AppStartup(config)
