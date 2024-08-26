from os import getenv
from redis import Redis
from dotenv import load_dotenv

load_dotenv()

REDIS = Redis(host=getenv('HOST'), port=getenv('PORT'))
