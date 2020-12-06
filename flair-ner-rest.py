from flask import abort, Flask, jsonify, request
from flair.models import SequenceTagger
from flair.data import Sentence

class NamedEntity():
    def __init__(self, text, score):
        self.t = text
        self.s = score
    def to_dict(self):
        return {"text": self.t, "score": self.s}
 
app = Flask(__name__)
 
tagger = SequenceTagger.load('ner')
 
@app.route('/api/v1/ner', methods=['POST'])
def namedEntityRecognition():
    if not request.json or not 'message' in request.json:
        abort(400)
    message = request.json['message']
    sentence = Sentence(message)
    tagger.predict(sentence)
    print('Analyzed: ', sentence)

    entities=[]
    for spanOfEntity in sentence.get_spans('ner'):
        print('Entity: ', spanOfEntity)
        print('Named entity: ', NamedEntity(spanOfEntity.text, spanOfEntity.score).to_dict())
        entities.append(NamedEntity(spanOfEntity.text, spanOfEntity.score).to_dict())

    response = {'submitted-message': message, 'entities': entities, 'flair-version': '0.7'}
    return jsonify(response), 200
 
if __name__ == "__main__":
    app.run()
