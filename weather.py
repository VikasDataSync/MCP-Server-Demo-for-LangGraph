from mcp.server.fastmcp import FastMCPServer

mcp = FastMCPServer("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get the current weather for a given location."""
    # Here you would implement the logic to fetch weather data from an API
    # For demonstration purposes, we'll return a dummy response
    return f"The current weather in {location} is sunny with a temperature of 25°C."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
    
# transport="streamable-http" allows the server to communicate with clients using HTTP, which is a common protocol for web-based applications. This means that clients can send requests to the server over HTTP and receive responses in a streamable format, making it suitable for real-time applications like fetching weather data.