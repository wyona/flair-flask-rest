# See https://shekhargulati.com/2019/01/04/building-a-sentiment-analysis-python-microservice-with-flair-and-flask/
from flask import abort, Flask, jsonify, request
from flair.models import TextClassifier
from flair.data import Sentence

app = Flask(__name__)

classifier = TextClassifier.load('en-sentiment')

@app.route('/api/v1/analyzeSentiment', methods=['POST'])
def analyzeSentiment():
    if not request.json or not 'message' in request.json:
        abort(400)
    message = request.json['message']
    sentence = Sentence(message)
    classifier.predict(sentence)
    print('Sentence sentiment: ', sentence.labels)
    label = sentence.labels[0]
    response = {'result': label.value, 'polarity':label.score}
    return jsonify(response), 200

if __name__ == "__main__":
    app.run()
