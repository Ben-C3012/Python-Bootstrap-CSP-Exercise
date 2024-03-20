from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})

database = [
    {"name": "John", "comment": "Great Website!"},
    {"name": "Jane", "comment": "I learned a lot from this."},
    {"name": "Mike", "comment": "Thanks for sharing!"},
    {"name": "Hack3r", "comment": "<iframe src=\"https://giphy.com/embed/V4NSR1NG2p0KeJJyr5\" width=\"480\" height=\"360\" frameBorder=\"0\" class=\"giphy-embed\" allowFullScreen></iframe>"},
    {"name": "John", "comment": "<img src=\"a\" onerror=\"alert('XSS Attack')\">"},
    {"name": "Analyzer", "comment": "<iframe src=\"https://giphy.com/embed/LXfpI3nNbfCm91llsA\" width=\"480\" height=\"400\" frameBorder=\"0\">"}
]
@app.route('/comments', methods=['GET'])
def get_comments():
    try:
        return jsonify(database), 200
    except Exception as e:
        return str(e)

@app.route('/add-comment', methods=['POST'])
def add_comment():
    try:
        new_comment = request.get_json()
        database.append(new_comment)
        return jsonify(new_comment), 200
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(port=3000)