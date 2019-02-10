import os
import pymongo
from pymongo import MongoClient

from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / 'sacred_setup' / '.env'
load_dotenv(dotenv_path=env_path)

DB_NAME = os.environ['MONGO_DATABASE']

client = MongoClient(f'mongodb://{os.environ["MONGO_INITDB_ROOT_USERNAME"]}:{os.environ["MONGO_INITDB_ROOT_PASSWORD"]}@localhost:27017/?authMechanism=SCRAM-SHA-1')
client.drop_database(DB_NAME)
print(f'Database {DB_NAME} successfully deleted.')
