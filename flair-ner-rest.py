import logging

from flask import abort, Flask, jsonify, request
from flair.models import SequenceTagger
from flair.data import Sentence
from flair import __version__

class NamedEntity():
    def __init__(self, text, tag, score):
        self.t = text
        self.tag = tag
        self.s = score
    def to_dict(self):
        return {"text": self.t, "tag": self.tag, "score": self.s}
 
app = Flask(__name__)
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
 
tagger = SequenceTagger.load('ner')
 
@app.route('/api/v1/ner', methods=['POST'])
def namedEntityRecognition():
    if not request.json or not 'message' in request.json:
        abort(400)

    message = request.json['message']
    sentence = Sentence(message)
    tagger.predict(sentence)
    logger.info(f"Analyzed: {sentence}")

    entities=[]
    for spanOfEntity in sentence.get_spans('ner'):
        logger.info(f"Entity: {spanOfEntity}")
        logger.info(f"Labels: {spanOfEntity.labels}")
        logger.info(f"Tag: {spanOfEntity.tag}")
        namedEntity = NamedEntity(spanOfEntity.text, spanOfEntity.tag, spanOfEntity.score)
        logger.info(f"Named entity: {namedEntity.to_dict()}")
        entities.append(namedEntity.to_dict())
        #entities.append(spanOfEntity.to_dict())

    response = {'submitted-message': message, 'entities': entities, 'flair-version': __version__}
    return jsonify(response), 200
 
if __name__ == "__main__":
    logger.info(f"Starting server ...")
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
    #app.run(host='0.0.0.0', port=5000)
