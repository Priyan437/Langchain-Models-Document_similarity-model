import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"))

## This is a file to test if The dotenv is fetching the API correctly or not.
