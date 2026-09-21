# MCP Client Config Format Translator

开发者经常同时使用多个 AI 客户端，而每个客户端保存 MCP 服务器配置的方式都有差异。这个 CLI 可以把 JSON/JSONC MCP 配置规范化成可迁移清单，或输出干净的 `mcpServers` 片段。

## 为什么现在值得做

MCP 采用速度很快，但中英文开发者社区都在反馈 Claude Code、Cursor、Goose、桌面 Agent、本地优先客户端之间配置碎片化。可迁移性已经是日常痛点。

## 安装与运行

```bash
python -m mcp_client_config_format_translator_20260801.cli examples/cursor-mcp.jsonc
python -m mcp_client_config_format_translator_20260801.cli examples/cursor-mcp.jsonc --target mcpServers
python -m mcp_client_config_format_translator_20260801.cli examples/cursor-mcp.jsonc --diff examples/claude-mcp.json
python -m unittest discover -s tests
```

## 示例

```json
{
  "servers": [
    {"name": "filesystem", "command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem"], "env_keys": []}
  ]
}
```

## 路线图

- 增加更多客户端导入预设
- 生成脱敏 HTML 团队审阅报告
