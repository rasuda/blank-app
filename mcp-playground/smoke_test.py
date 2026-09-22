import asyncio
import sys

from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client


async def main() -> None:
    server = StdioServerParameters(
        command=sys.executable,
        args=["server.py"],
    )

    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools_result = await session.list_tools()
            tool_names = {tool.name for tool in tools_result.tools}

            assert "somar" in tool_names
            assert "informacoes_computador" in tool_names

            soma = await session.call_tool("somar", arguments={"a": 10, "b": 20})
            assert not soma.isError

            soma_text = next(
                block.text
                for block in soma.content
                if isinstance(block, types.TextContent)
            )
            assert "30" in soma_text

            info = await session.call_tool("informacoes_computador", arguments={})
            assert not info.isError

            print("MCP smoke test OK")
            print(f"Tools encontradas: {sorted(tool_names)}")
            print(f"Resultado somar(10, 20): {soma_text}")


if __name__ == "__main__":
    asyncio.run(main())
