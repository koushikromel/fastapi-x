from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    return "Welcome"

@app.get("/{name}")
def home(name):
    return f"Welcome {name}!"

