from dotenv import load_dotenv
import os, sys

load_dotenv('../.env')
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, '.env'))
sys.path.append(BASE_DIR)