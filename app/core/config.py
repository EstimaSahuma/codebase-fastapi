from dotenv import load_dotenv
from passlib.context import CryptContext
import os

# Load the .env file
load_dotenv()

# Get the value of DATABASE_URL from the .env file
DATABASE_URL = os.getenv("DATABASE_URL")

# define contexr encripting
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
