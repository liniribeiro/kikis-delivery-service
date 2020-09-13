import os

from decouple import config

TEST = config('TEST')

DB_URI = config('DB_URI')

BASE_DIR = os.path.dirname(os.path.dirname( os.path.abspath(__file__)))