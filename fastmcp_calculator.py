from fastmcp import FastMCP

mcp = FastMCP(name="Calculator")


@mcp.tool()
def addition(no1 : float, no2 : float) -> float:
    """Addition of two numbers"""
    return no1 + no2

@mcp.tool()
def substraction(no1 : float, no2 : float) -> float:
    """Substract two numbers"""
    return no1 - no2

@mcp.tool()
def multiply(no1 : float, no2 : float) -> float:
    """Multiply two numbers"""
    return no1 * no2

@mcp.tool(name="division", description="Division of two numbers")
def division(no1 : float, no2 : float) -> float:
    if no2 == 0:
        raise ValueError("Division number mst not be 0")
    return no1 / no2

def main():    
    mcp.run()

if __name__ == "__main__":
    main()