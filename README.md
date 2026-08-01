# MCP Client Config Format Translator

Developers now run several AI clients at once, and each stores MCP server configuration slightly differently. This CLI normalizes JSON/JSONC MCP configs into a portable inventory or a clean `mcpServers` snippet.

## Why now

MCP adoption is accelerating, while Chinese and global developer communities keep reporting configuration fragmentation across Claude Code, Cursor, Goose, desktop agents, and local-first clients. Portability is a daily pain.

## Install and run

```bash
python -m mcp_client_config_format_translator_20260801.cli examples/cursor-mcp.jsonc
python -m mcp_client_config_format_translator_20260801.cli examples/cursor-mcp.jsonc --target mcpServers
python -m unittest discover -s tests
```

## Example

```json
{
  "servers": [
    {"name": "filesystem", "command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem"], "env_keys": []}
  ]
}
```

## Roadmap

- Import presets for more clients
- Diff two client configs
- Redacted HTML reports for team review
