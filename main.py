# calculator MCP server
from fastmcp_calculator import mcp


def main():
    # mcp.run() # default it run as STDIO
    mcp.run(transport="http", host="localhost", port=8080, show_banner=True)


if __name__ == "__main__":
    main()
