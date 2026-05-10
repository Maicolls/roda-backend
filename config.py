import os
from dotenv import load_dotenv

load_dotenv()  # lee el archivo .env y carga las variables

DATABASE_URL = os.getenv("DATABASE_URL")  # agarra solo la que necesitamos
