from flask import Flask, request
from flask_cors import CORS

import json
from Transformer.Model import Model

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

model = Model()

model.load_model('question-answering')


@app.route('/api/question_answering', methods=['POST', 'GET'])
def question_answering():
    global model
    if request.method == 'POST':
        context = ''
        question = ''
        try:
            data = request.get_json()
            context = data['context']
            print(context)
            question = data['question']
            print(question)
        except:
            return {'status': "Data must have content field"}

        answer_json = model.question_answering(
            context=context, question=question)
        return answer_json
    else:
        context_sample = 'A is 5 years old and lives with her mother in Ha Noi city'
        question_sample = 'where does A live?'
        result = model.question_answering(
            context=context_sample, question=question_sample)
        return "<p><strong>context:</strong> " + context_sample \
            + "<br><strong>question:</strong> " + question_sample \
            + "<br><strong>answer:</strong> " + result['answer'] \
            + "<br>" + json.dumps(result) + \
            "</p>"

# uncomment for summarization api
# model.load_model('summarization')


@app.route('/api/summarization', methods=['POST', 'GET'])
def summarization():
    global model
    if request.method == 'POST':
        text = ""
        try:
            text = request.get_json()['content']  # @param {type:"string"}
            print(request.get_json())
        except:
            return {'status': "Data must have content field"}

        summary_text = model.summarization(text)[0]
        return summary_text
    else:
        summary_text = model.summarization(
            "National Archives Yes, it’s that time again, folks. It’s the first Friday of the month, when for one ever-so-brief moment the interests of Wall Street, Washington and Main Street are all aligned on one thing: Jobs. A fresh update on the U.S. employment situation for January hits the wires at 8:30 a.m. New York time offering one of the most important snapshots on how the economy fared during the previous month. Expectations are for 203,000 new jobs to be created, according to economists polled by Dow Jones Newswires, compared to 227,000 jobs added in February. The unemployment rate is expected to hold steady at 8.3%. Here at MarketBeat HQ, we’ll be offering color commentary before and after the data crosses the wires. Feel free to weigh-in yourself, via the comments section. And while you’re here, why don’t you sign up to follow us on Twitter. Enjoy the show. ||||| Employers pulled back sharply on hiring last month, a reminder that the U.S. economy may not be growing fast enough to sustain robust job growth. The unemployment rate dipped, but mostly because more Americans stopped looking for work. The Labor Department says the economy added 120,000 jobs in March, down from more than 200,000 in each of the previous three months. The unemployment rate fell to 8.2 percent, the lowest since January 2009. The rate dropped because fewer people searched for jobs. The official unemployment tally only includes those seeking work. The economy has added 858,000 jobs since December _ the best four months of hiring in two years. But Federal Reserve Chairman Ben Bernanke has cautioned that the current hiring pace is unlikely to continue without more consumer spending.")
        print(summary_text)
        return summary_text


if __name__ == "__main__":
    app.run()
