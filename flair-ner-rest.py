from flask import abort, Flask, jsonify, request
from flair.models import SequenceTagger
from flair.data import Sentence

class NamedEntity():
    def __init__(self, text, tag, score):
        self.t = text
        self.tag = tag
        self.s = score
    def to_dict(self):
        return {"text": self.t, "tag": self.tag, "score": self.s}
 
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
        print('Labels: ', spanOfEntity.labels)
        print('Tag: ', spanOfEntity.tag)
        namedEntity = NamedEntity(spanOfEntity.text, spanOfEntity.tag, spanOfEntity.score)
        print('Named entity: ', namedEntity.to_dict())
        entities.append(namedEntity.to_dict())
        #entities.append(spanOfEntity.to_dict())

    response = {'submitted-message': message, 'entities': entities, 'flair-version': '0.7'}
    return jsonify(response), 200
 
if __name__ == "__main__":
    app.run()
