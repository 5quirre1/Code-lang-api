from flask import Flask, jsonify

app = Flask(__name__)

extension_to_language = {
    '.py': 'Python',
    '.go': 'Golang',
    '.js': 'JavaScript',
    '.rb': 'Ruby',
    '.java': 'Java',
    '.cpp': 'C++',
    '.c': 'C',
    '.jl': 'Julia',
    '.r': 'R',
    '.html': 'HTML',
    '.css': 'CSS',
    '.php': 'PHP',
    '.ts': 'TypeScript',
    '.swift': 'Swift',
    '.kt': 'Kotlin',
    '.scala': 'Scala',
    '.sh': 'Shell',
    '.bash': 'Shell',
    '.dockerfile': 'Dockerfile',
    '.h': 'C Header',
    '.m': 'Objective-C',
    '.v': 'V',
    '.clj': 'Clojure',
    '.pl': 'Perl',
    '.lua': 'Lua',
    '.el': 'Elixir',
    '.dart': 'Dart',
    '.groovy': 'Groovy',
    '.asp': 'ASP',
    '.asm': 'Assembly',
    '.tex': 'TeX',
    '.md': 'Markdown',
    '.makefile': 'Makefile',
    '.yml': 'YAML',
    '.json': 'JSON',
    '.xml': 'XML',
    '.sql': 'SQL',
    '.csv': 'CSV',
    '.tsv': 'TSV',
    '.xaml': 'XAML',
    '.vhdl': 'VHDL',
    '.rhtml': 'Ruby HTML',
    '.erl': 'Erlang',
    '.nim': 'Nim',
    '.rexx': 'Rexx',
    '.pug': 'Pug',
    '.sass': 'Sass',
    '.stylus': 'Stylus',
}

@app.route('/languages', methods=['GET'])
def get_languages():
    return jsonify(extension_to_language)
  
def handler(request):
    return app(request)
