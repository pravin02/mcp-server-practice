# mcp-server-practice
This repo contains examples of MCP server and its usage and integration with tool and how it can tested.

### STDIO Calculator MCP Server

#### Dependencies:
`uv add fastmcp`

How to run:
`npx @modelcontextprotocol/inspector python main.py`

### Fast API
#### Dependencies
`uv add fastapi fastapi-mcp uvicorn[standard]`

#### How to run application
`python fastapi-mcp-calculator.py` it will bring up fastapi server on localhost 8080 port number.

##### To access Open API Documentationf of FastAPI use below url.

`http://lcoalhost:8080/docs`

### Converting Fast API server into MCP Server

#### To Convert Fast API server into MCP server import below dependency
`from fastapi-mcp import FastApiMCP`

#### To convert fast api app as MCP sever ingest app to FastApiMCP
`mcp = FastApiMCP(app, name="Name of the MCP Server")`

### To run MCP server as Http Server
`mcp.mount_http()`

### To verify use below URL
`http://localhost:8080/mcp`

Response:

> {
    "jsonrpc":"2.0","id":"server-error","error":{"code":-32600,"message":"Not Acceptable: Client must accept text/event-stream"}}