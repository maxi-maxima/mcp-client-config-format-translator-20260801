import argparse, json, re, sys

def strip_jsonc(text):
    text=re.sub(r'/\*.*?\*/','',text,flags=re.S)
    text=re.sub(r'(^|\s)//.*','',text)
    return text

def load(path):
    with open(path, encoding='utf-8') as handle:
        data=json.loads(strip_jsonc(handle.read()))
    servers=data.get('mcpServers') or data.get('servers') or data.get('mcp',{}).get('servers') or {}
    if isinstance(servers, list):
        servers={s.get('name',f'server-{i+1}'):s for i,s in enumerate(servers)}
    out=[]
    for name,cfg in servers.items():
        out.append({'name':name,'command':cfg.get('command') or cfg.get('cmd'),'args':cfg.get('args',[]),'env_keys':sorted((cfg.get('env') or {}).keys()),'transport':cfg.get('transport','stdio' if cfg.get('command') else 'http'),'url':cfg.get('url')})
    return out

def emit(servers, target):
    if target=='inventory':
        return json.dumps({'servers':servers},indent=2)
    mcp={s['name']:{k:v for k,v in {'command':s['command'],'args':s['args'],'url':s['url']}.items() if v} for s in servers}
    return json.dumps({'mcpServers':mcp}, indent=2)

def main(argv=None):
    ap=argparse.ArgumentParser(description='Translate MCP client config formats into a portable inventory.')
    ap.add_argument('config')
    ap.add_argument('--target', choices=['inventory','mcpServers'], default='inventory')
    ns=ap.parse_args(argv)
    print(emit(load(ns.config), ns.target))
if __name__=='__main__': main()
