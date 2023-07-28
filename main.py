import os
import argparse
import cv2
import numpy as np
import requests
from io import BytesIO
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Optional
from ascii_gen import url_to_ascii, make_filename

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/ascii/")
async def get_ascii_art(request: Request, url: Optional[str] = "https://www.alleycat.org/wp-content/uploads/2019/03/FELV-cat.jpg", canny: Optional[bool] = False):
    try:
        ascii_art = url_to_ascii(url, canny=canny)
        return templates.TemplateResponse("index.html", {"request": request, "ascii_art": ascii_art})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
