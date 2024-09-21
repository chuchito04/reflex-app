from sqlmodel import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

def connect():
    engine = create_engine(os.getenv("LOCALHOST"))
    return engine