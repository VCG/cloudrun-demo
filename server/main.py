import json
from typing import Optional

import uvicorn
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from fastapi import WebSocket
from requests.exceptions import HTTPError
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return "Hello World!"


def start():
    uvicorn.run("main:app", host="127.0.0.1", port=4244, reload=True, log_level="info", app_dir="/")


if __name__ == "__main__":
    start()
