import os
from dotenv import load_dotenv

load_dotenv()


class Endpoints:
    login = f"{os.getenv('BASE_URL')}/auth"
    booking = f"{os.getenv('BASE_URL')}/booking"
