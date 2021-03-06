import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.route import router
from config.env import *

app = FastAPI(
    redoc_url=False
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv('CORS_ALLOW_ORIGINS'),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "Hello": "Welcome to the Spending API",
        "Github": "https://github.com/Paulo-Lopes-Estevao/expensecontrol",
        "Documentation Swegger": "https://fast-hamlet-77449.herokuapp.com/docs"
        }
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=os.getenv("PORT"))