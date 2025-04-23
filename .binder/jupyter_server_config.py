c.ServerProxy.servers = {
    'vscode': {
        'command': ['code-server', '--auth', 'none', '--disable-telemetry', '--port', '{port}'],
        'timeout': 30,
        'launcher_entry': {
            'title': 'VS Code',
            'icon_path': '/usr/share/pixmaps/code.png',  # optional
        },
    }
}