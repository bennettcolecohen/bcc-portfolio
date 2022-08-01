from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Setup
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# def connect_to_db(): 
#     try: 
#         engine = create_engine(
#             "postgres://uecxoerwcedqby:10eaaf94acd25999e959949659a95e33cc3766802e01d5990e6e38f50ba740ec@ec2-34-235-31-124.compute-1.amazonaws.com:5432/d94n2pv9om0d09", 
#             connect_args = {'connect_timeout': 10}, 
#             echo = False, pool_size = 20, max_overflow = 0)
#         print('Connection Initiated')
#     except:
#         raise ValueError("Can't connect to Heroku PostgreSQL! You must be so embarrassed")
#     return engine

@app.get("/")
def index(request: Request): 
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/projects")
def projects(request: Request): 
    return templates.TemplateResponse("projects.html", {"request": request})

@app.get("/blog")
def projects(request: Request): 
    return templates.TemplateResponse("blog.html", {"request": request})



# @app.get("/projects")
# def projects(request: Request): 
#     return templates.TemplateResponse("projects.html", {"request": request})

# @app.get('/blog')
# def blog(request: Request): 
#     return templates.TemplateResponse('blog.html', {"request": request})

# @app.get("/projects/{project_name}")
# def betml(project_name: str, request: Request): 
#     return templates.TemplateResponse(f"{project_name}.html", {"request": request})

# @app.get("/header")
# def header(request: Request): 
#     return templates.TemplateResponse("header.html", {"request": request})

# @app.get("/footer")
# def footer(request: Request): 
#     return templates.TemplateResponse("footer.html", {"request": request})
