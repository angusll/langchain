import os
from dataclasses import dataclass

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(filename="keys.env"))


@dataclass
class Credentials:
    openai_api_key: str = str(os.environ.get("OPENAI_API_KEY"))
    pinecone_api_key: str = str(os.environ.get("PINECONE_API_KEY"))
    pinecone_env: str = str(os.environ.get("PINECONE_ENV"))
