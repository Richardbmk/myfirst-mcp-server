from mcp.server.fastmcp import FastMCP
import time

mcp = FastMCP("add_integers")

class MCPError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(f"Error {code}: {message}")

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

@mcp.tool()
def divide(a: float, b: float) -> float:
    """
    Divide two floating-point numbers and return the result.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of the division.
    """
    if b == 0:
        raise MCPError(code=400, message="Division by zero is not allowed.")
    return a / b

@mcp.tool()
def long_process(steps: int):
    """
    Simulate a long-running process by sleeping for a short duration multiple times.

    Args:
        steps (int): The number of steps to simulate.
    """
    for step in range(steps):
        print(f"Processing step {step + 1}/{steps}...")
        time.sleep(1)  # Simulate work by sleeping for 1 second
    return "Process completed."


if __name__ == "__main__":
    mcp.run(transport="stdio")


