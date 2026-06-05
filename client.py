import asyncio
import os
import sys
from pathlib import Path


def _ensure_venv_python() -> None:
    venv_python = Path(__file__).resolve().parent / ".venv" / "Scripts" / "python.exe"
    current_python = Path(sys.executable).resolve()

    if venv_python.exists() and current_python != venv_python.resolve():
        os.execv(str(venv_python), [str(venv_python), str(Path(__file__).resolve()), *sys.argv[1:]])


_ensure_venv_python()

from langchain_mcp_adapters.client import MultiServerMCPClient


async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": sys.executable,
                "args": ["mathserver.py"],
                "transport": "stdio",
            },
        }
    )
    

    tools = await client.get_tools()
    tool_by_name = {tool.name: tool for tool in tools}

    add_result = await tool_by_name["add"].ainvoke({"a": 5, "b": 3})
    add_value = int(add_result[0]["text"])

    multiply_result = await tool_by_name["multiply"].ainvoke({"a": add_value, "b": 2})
    multiply_value = int(multiply_result[0]["text"])

    print("Math Response:", multiply_value)


if __name__ == "__main__":
    asyncio.run(main())