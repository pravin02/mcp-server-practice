from feed_search_mcp_server import mcp

def main():    
    mcp.run(transport="http", host="localhost", port=8080, show_banner=True)

if __name__ == "__main__":
    main()


"""
To run this applcation all the dependenecies using uv pip install -r pyproject.toml
and run MCP server using below commands
python main.py

run model context protocol inspector to test MCP server
npx @modelcontextprotocol/inspector http://localhost:8080/mcp
"""