from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():

    return {"title": "Hello World - LB Modul 169"}