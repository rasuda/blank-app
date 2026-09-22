import sys

import anyio
from mcp import Client, StdioServerParameters


async def main() -> None:
    server = StdioServerParameters(
        command=sys.executable,
        args=["server.py"],
    )

    async with Client(server) as client:
        tools_result = await client.list_tools()
        tool_names = {tool.name for tool in tools_result.tools}

        assert "somar" in tool_names
        assert "informacoes_computador" in tool_names

        soma = await client.call_tool("somar", {"a": 10, "b": 20})
        assert not soma.is_error
        assert soma.structured_content == {"result": 30}

        info = await client.call_tool("informacoes_computador", {})
        assert not info.is_error
        assert info.structured_content is not None
        assert "sistema" in info.structured_content

        print("MCP smoke test OK")
        print(f"Tools encontradas: {sorted(tool_names)}")
        print(f"Resultado somar(10, 20): {soma.structured_content}")


if __name__ == "__main__":
    anyio.run(main)
