from fastmcp import FastMCP
import feedparser

rss_freecodecamp = "https://freecodecamp.org/news/rss/"

freecodecamp_youtube_rss_feed = "UC8butISFwT-Wl7EV0hUK0BQ"

rss_youtube = "https://youtube.com/feeds/videos.xml?channel_id="

mcp = FastMCP(name="Feed Search parser MCP server", version="0.1.0")

@mcp.tool(
    name="freecodecamp_rss_feed_tool",
    description="This tool help to pull freecodecamp.org/news rss feeds",
    tags={"Education", "Information Technology"},
)
def freecodecamp_rss_feed_tool(query: str, max_results: int = 3):
    feed = feedparser.parse(f"{rss_freecodecamp}")
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
    return results or ({"message": "No results found"})

@mcp.tool(
    name="youtube_rss_feed_tool",
    description="This tool pulls freecodecamp.org youtube channels videos rss feeds",
    tags={"Education", "Information Technology"},
)
def youtube_rss_feed_tool(query: str, max_results: int = 3):
    feed = feedparser.parse(f"{rss_youtube}{freecodecamp_youtube_rss_feed}")
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
    return results or ({"message": "No results found"})

@mcp.tool(
    name="youtube_dynamic_rss_feed_tool",
    description="This tool pulls provided youtube {cahnnel_id} videos rss feeds",
    tags={"Education", "Information Technology"},
)
def youtube_dynamic_rss_feed_tool(channel_id: str, query: str, max_results: int = 3):
    try:
        feed_url = f"{rss_youtube}{channel_id}"
        print(f"Feed Url : {feed_url}")
        feed = feedparser.parse(feed_url)
        print(f"No of feeds retrived: {len(feed.entries)}")
        results = []
        query_lower = query.lower()
        for entry in feed.entries:
            title = entry.title
            description = entry.description
            print(f"Title: {title}")
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
        return results or ({"message": "No results found"})
    except Exception as e:
        return {"status": False, "error": e}


def main():    
    mcp.run(transport="http", host="localhost", port=8080, show_banner=True)

if __name__ == "__main__":
    main()