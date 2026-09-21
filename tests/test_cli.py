import unittest

from mcp_client_config_format_translator_20260801.cli import diff, load


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

    def test_diff_reports_added_removed_and_changed_servers(self):
        left = [
            {'name': 'git', 'command': 'uvx', 'args': ['mcp-git'], 'env_keys': [], 'transport': 'stdio', 'url': None},
            {'name': 'old', 'command': 'node', 'args': [], 'env_keys': [], 'transport': 'stdio', 'url': None},
        ]
        right = [
            {'name': 'git', 'command': 'uvx', 'args': ['mcp-git', '--readonly'], 'env_keys': [], 'transport': 'stdio', 'url': None},
            {'name': 'new', 'command': 'npx', 'args': [], 'env_keys': [], 'transport': 'stdio', 'url': None},
        ]
        result = diff(left, right)
        self.assertEqual(result['added'], ['new'])
        self.assertEqual(result['removed'], ['old'])
        self.assertEqual(result['changed'][0]['name'], 'git')
        self.assertEqual(result['changed'][0]['fields']['args']['after'], ['mcp-git', '--readonly'])


if __name__ == '__main__':
    unittest.main()
