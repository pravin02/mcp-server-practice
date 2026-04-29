from fastmcp import FastMCP
import feedparser

rss_freecodecamp = "https://freecodecamp.org/news/rss/"

mcp = FastMCP(name="Feed Search parser MCP server")


@mcp.tool()
def search_feed(query: str, max_results: int = 3):
    feed = feedparser.parse(rss_freecodecamp)
    results = []
    query_lower = query.lower()
    for entry in feed.entries:
        title = entry.title
        description = entry.description        
        if query_lower in title or query_lower in description:
            results.append(
                {
                    "titel": title,
                    "description": description,
                    "url": entry.get("link", ""),
                }
            )
            if len(results) >= max_results:
                break
    return results or [{"message": "No results found"}]


# def main():
#     mcp.run(transport="http", host="localhost", port="8080")
#     # mcp.run() #STDIO


# if __name__ == "__main__":
#     main()
