from flask import Flask, render_template, request, jsonify
from regex_nlp import extract_info, tokenize, clean_text, validate, custom_match

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract():
    text = request.json.get('text', '')
    return jsonify(extract_info(text))

@app.route('/tokenize', methods=['POST'])
def tokenize_route():
    data = request.json
    return jsonify(tokenize(data.get('text', ''), data.get('mode', 'word')))

@app.route('/clean', methods=['POST'])
def clean():
    data = request.json
    return jsonify(clean_text(
        data.get('text', ''),
        remove_urls=data.get('urls', True),
        remove_html=data.get('html', True),
        remove_emojis=data.get('emojis', True),
        remove_social=data.get('social', True),
        remove_special=data.get('special', True),
        normalize_spaces=data.get('spaces', True)
    ))

@app.route('/validate', methods=['POST'])
def validate_route():
    data = request.json
    return jsonify(validate(data.get('field', ''), data.get('value', '')))

@app.route('/custom', methods=['POST'])
def custom():
    data = request.json
    return jsonify(custom_match(
        data.get('pattern', ''),
        data.get('text', ''),
        data.get('flags', 'g')
    ))

if __name__ == '__main__':
    app.run(debug=True)