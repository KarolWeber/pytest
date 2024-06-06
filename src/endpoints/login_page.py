import os
from dotenv import load_dotenv
load_dotenv()

class LoginEndpoints:
    auth = f"{os.getenv('BASE_URL')}/auth"