import uvicorn
from fastapi import FastAPI
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware
from router.route import router
from config.env import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv('CORS_ALLOW_ORIGINS'),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
"""

"""
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)