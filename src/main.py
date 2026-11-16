import os

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")

if database_url is None:
    raise ValueError("DATABASE_URL environment variable is not set")

df = pd.read_csv(database_url)

pd.set_option('display.max_columns', 5)
pd.set_option('display.max_rows', 5)

print(df)