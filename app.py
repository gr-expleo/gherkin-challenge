from flask import Flask, request, jsonify
from gherkin_lexer import GherkinLexer, GherkinLexerError
from gherkin_parser import GherkinParser

# Initialize Flask
app = Flask(__name__)

# Initialize and build Lexer and Parser
lexer = GherkinLexer()
lexer.build()

parser = GherkinParser(lexer)
parser.build()  

@app.route('/parse', methods=['POST'])
def parse_gherkin():
    try:
        if not request.files:
            return jsonify({"error": "No file was uploaded uploaded"}), 400

        # Read file and content
        file = next(iter(request.files.values()))
        content = file.read().decode('utf-8')

        # Call our lexer and parser
        lexer.input(content)
        
        result = parser.parse(content)

        return jsonify(result), 200

    except SyntaxError as e:
        return jsonify({"error": str(e)}), 400

    except GherkinLexerError as e:
        return jsonify({"error": "Incorrect input", "details": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)