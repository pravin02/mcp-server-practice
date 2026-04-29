import uvicorn
from fastapi import FastAPI

app = FastAPI(title="FastAPI Server")


@app.get("/")
def home():
    return {"status", "Fast API server"}

@app.post("/addition")
def addition(no1 : float, no2: float):
    """
    no1 : flaot
    no2 : float
    returns addition of two numbers
    """
    return {"result": no1 + no2}

@app.post("/substraction")
def substraction(no1 : float, no2: float):
    """
    no1 : flaot
    no2 : float
    returns substraction of two numbers
    """
    return {"result": no1 - no2}

@app.post("/multiply")
def multiply(no1 : float, no2: float):
    """
    no1 : flaot
    no2 : float
    returns multiply of two numbers
    """
    return {"result": no1 * no2}

def main():
    uvicorn.run(app, host="localhost", port=8080)

if __name__ == "__main__":
    main()