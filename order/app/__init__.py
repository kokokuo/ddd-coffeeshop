from orders.settings import config
from .startup import AppStartup


app = AppStartup(config)
