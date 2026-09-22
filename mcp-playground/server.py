import platform

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MCP Playground")


@mcp.tool()
def somar(a: int, b: int) -> int:
    """Soma dois números inteiros."""
    return a + b


@mcp.tool()
def informacoes_computador() -> dict[str, str]:
    """Retorna informações básicas da máquina onde o MCP Server está rodando."""
    return {
        "sistema": platform.system(),
        "versao": platform.version(),
        "arquitetura": platform.machine(),
        "processador": platform.processor(),
    }


if __name__ == "__main__":
    mcp.run()
