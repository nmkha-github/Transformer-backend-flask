from flask import Flask, request, jsonify
from flask_cors import CORS

from Transformer.model import Transformer

app = Flask(__name__)
CORS(app)

model = Transformer()
model.load_model()


@app.route('/api/summarize')
def SummarizePage():
    return '<h1>Hello</h1>'


@app.get('/api/summarize')
def get():
    text = model.summarize('abcasc masckas maskc mckmkc')
    print(text)
    return text


@app.post('/api/summarize')
def summarize():
    global model
    text = ""
    try:
        text = request.get_json()['content']  # @param {type:"string"}
    except:
        return {'status': "Data must have content field"}

    summary_text = model.summarize(text)[0]
    return jsonify({'summary_text': summary_text})


if __name__ == '__main__':

    app.run(debug=False)
