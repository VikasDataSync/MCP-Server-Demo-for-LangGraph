# MCP Server Demo

This project is a small Model Context Protocol (MCP) demo built with Python, LangGraph, and `langchain-mcp-adapters`.

It includes:

- `mathserver.py`: a local MCP server with `add` and `multiply` tools
- `client.py`: a client that loads the math tools and prints the result of `(5 + 3) * 2`
- `weather.py`: an additional MCP server example that is not wired into the current client

## Requirements

- Python 3.13 or newer
- A virtual environment at `.venv`

## Setup

If the virtual environment does not exist yet, create it and install the project dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If you already have the virtual environment, activate it with:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Run

Run the client:

```powershell
python client.py
```

Expected output:

```text
Math Response: 16
```

The client is written to relaunch itself with the workspace virtual environment if it is started from another interpreter, so `python client.py` is usually enough.

## How It Works

`client.py` starts the math MCP server over stdio, loads the exported tools, calls `add(5, 3)`, then passes the result into `multiply(..., 2)`.

## Notes

- The math server uses stdio transport.
- The weather server uses streamable HTTP, but it is not currently started by the client.
- If you want to connect the weather server, start it separately and add it back to the client configuration.
# MCP-Server-Demo-for-LangGraph
