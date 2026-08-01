import unittest

from mcp_client_config_format_translator_20260801.cli import load


class LoadTests(unittest.TestCase):
    def test_loads_jsonc_mcp_servers(self):
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'config.jsonc'
            p.write_text('// comment\n{"mcpServers":{"git":{"command":"uvx","args":["mcp-git"],"env":{"TOKEN":"x"}}}}', encoding='utf-8')
            servers = load(str(p))
        self.assertEqual(servers[0]['name'], 'git')
        self.assertEqual(servers[0]['env_keys'], ['TOKEN'])


if __name__ == '__main__':
    unittest.main()
