from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Setup
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request): 
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/work")
def work(request: Request): 
    return templates.TemplateResponse("work.html", {"request": request})

@app.get("/betml")
def betml(request: Request): 
    return templates.TemplateResponse("betml.html", {"request": request})

@app.get("/betmlb")
def betmlb(request: Request):
    return templates.TemplateResponse("betmlb.html", {"request": Request})