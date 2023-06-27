from flask import Flask, request, jsonify

from Transformer.model import Transformer

app = Flask(__name__)

model = Transformer()
model.load_model()


@app.get('/api/summarize')
def get():
    return '<h1>Hello</h1>'


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
