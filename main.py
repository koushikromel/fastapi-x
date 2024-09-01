from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
def home():
    return "Welcome"

@app.get("/{name}")
def greet(name):
    return f"Welcome {name}!"


if __name__ == "__main__":
    uvicorn.run(app)