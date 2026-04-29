import uvicorn
from fastapi import FastAPI

# To convert fastapi server into MCP server
from fastapi_mcp import FastApiMCP

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


# Now convert fastapi application into MCP server
mcp = FastApiMCP(app, name="Calculator MCP Server")
mcp.mount_http() # to run MCP server as http


def main():
    uvicorn.run(app, host="localhost", port=8080)

if __name__ == "__main__":
    main()