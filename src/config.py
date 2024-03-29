import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)  # pylint: disable=invalid-name

try:
    load_dotenv(dotenv_path=os.path.join(dirname, ".env"))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "data", DATABASE_FILENAME)

print(DATABASE_FILENAME, DATABASE_FILE_PATH)
