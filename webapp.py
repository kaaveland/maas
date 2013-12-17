"""
Markov as a Service (MaaS) webapp, using flask.

Execute with $ python webapp.py
"""

from flask import Flask, jsonify # http://flask.pocoo.org/docs/
import html_parse
import text

app = Flask('MaaS')
app.config['JSON_AS_ASCII'] = False

@app.route('/hello-world', methods = ['GET'])
def hello_world():
    return jsonify(message='Hello, World!')

def httpify(url):
    pass

@app.route('/<string:urls>')
def index_headlines_from(urls):
    pass

if __name__ == '__main__':
    app.run(debug=True)
