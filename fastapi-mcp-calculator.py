import uvicorn
from fastapi import FastAPI

app = FastAPI(title="FastAPI Server")


@app.get("/")
def home():
    return {"status", "Fast API server"}

def main():
    uvicorn.run(app, host="localhost", port=8080)

if __name__ == "__main__":
    main()