from dotenv import dotenv_values
from .base import *



config = dotenv_values(".env")

My_PROJECT = config.get("PROJECT_SETTINGS")

if My_PROJECT == 'prod':
   from .production import *
else:
   from .development import *