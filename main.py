from mcp.server.fastmcp import FastMCP

mcp = FastMCP("add_integers")

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two integers and return the result.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of the two integers.
    """
    return a + b


if __name__ == "__main__":
    mcp.run(transport="stdio")