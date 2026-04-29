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