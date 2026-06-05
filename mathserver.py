from mcp.server.fastmcp import FastMCP 

mcp=FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

# the tranport="stdio" means that the server will communicate with the client using standard input and output, which is a common way for language models to interact with tools and servers.

#use stdio to recieve requests from the client and send responses back to the client. This allows the server to be easily integrated with various clients, including language models, without needing to set up complex communication protocols.

if __name__ == "__main__":
    mcp.run(transport="stdio")

