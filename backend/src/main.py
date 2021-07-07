import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from settings import HOST, PORT
from handlers import app


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
