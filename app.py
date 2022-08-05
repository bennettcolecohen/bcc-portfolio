from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Setup
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request: Request): 
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/projects")
def projects(request: Request): 
    return templates.TemplateResponse("projects.html", {"request": request})

@app.get("/blog")
def projects(request: Request): 
    return templates.TemplateResponse("blog.html", {"request": request})

@app.get("/projects/{project_name}")
def betml(project_name: str, request: Request): 
    return templates.TemplateResponse(f"projects/{project_name}.html", {"request": request})

@app.get("/header")
def header(request: Request): 
    return templates.TemplateResponse("header.html", {"request": request})

# @app.get("/footer")
# def footer(request: Request): 
#     return templates.TemplateResponse("footer.html", {"request": request})
