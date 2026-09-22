# MCP Playground

Laboratório mínimo para aprender Model Context Protocol sem LLM.

## O que existe aqui

- `server.py`: MCP Server com duas Tools: `somar` e `informacoes_computador`.
- `smoke_test.py`: cliente MCP real via stdio que descobre e chama as Tools.
- GitHub Actions: valida automaticamente o MCP em Linux/Python 3.12.

## Rodar no VS Code

Abra o terminal na pasta `mcp-playground`.

Crie e ative um ambiente virtual:

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Testar automaticamente

```bash
python smoke_test.py
```

Esse teste inicia o MCP Server como subprocesso via stdio, lista as Tools e chama `somar(10, 20)`.

## Testar com MCP Inspector

```bash
mcp dev server.py
```

O Inspector permite chamar manualmente as Tools sem usar Ollama ou qualquer LLM.

Teste:

- Tool: `somar`
- `a = 10`
- `b = 20`
- Resultado esperado: `30`

Depois teste `informacoes_computador`.

## Próximo passo

Depois que este laboratório estiver validado, conectar o mesmo MCP Server a um Host, como OpenCode, e então usar um modelo local servido pelo Ollama.
