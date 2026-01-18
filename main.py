from mcp.server.fastmcp import FastMCP
import time
import logging

mcp = FastMCP("add_integers")

class MCPError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(f"Error {code}: {message}")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="./mcp_server.log", # Log file to store server logs
    filemode="a", # Use 'a' to append to the log file or 'w' to overwrite
    force=True
)

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
    logging.info(f"Adding {a} and {b}")
    result = a + b
    logging.info(f"Result: {result}")
    return result

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


