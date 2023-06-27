from flask import Flask, request, jsonify
from flask_cors import CORS

from Transformer.model import Transformer

app = Flask(__name__)
CORS(app)


@app.route('/api/summarize', methods=['POST', 'GET'])
def summarize():
    global model
    if model == None:
        model = Transformer()
        model.load_model()
    print('$$$$$$$$$$$$$$$$$$$$$$$$', model)
    if request.method == 'POST':
        text = ""
        try:
            text = request.get_json()['content']  # @param {type:"string"}
            print(request.get_json())
        except:
            return {'status': "Data must have content field"}

        summary_text = model.summarize(text)[0]
        return jsonify({'summary_text': summary_text})
    else:
        summary_text = model.summarize(
            ' This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.')
        print(summary_text)
        return summary_text


if __name__ == "__main__":
    app.run()
