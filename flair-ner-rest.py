import logging

from flask import Flask, jsonify, request
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

# Get named entitities
@app.route('/api/v1/ner', methods=['POST'])
def namedEntityRecognition():

    message = None
    try:
        logger.info(f"Try to parse request body as JSON ...")
        message = request.json['message']
    except:
        logger.error("Request body does not seem to be correct JSON")
        response = {'error_message': 'Flair: Get named entities: Request body does not seem to be correct JSON', 'error_code':'NO_JSON'}
        return jsonify(response), 400

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
# end def

# Health check endpoint
@app.route('/api/v1/health', methods=['GET'])
def checkHealth():
    logger.info("Check health ...")

    response = {'status':'UP','version':__version__}
    # TODO: Get model from SequenceTagger flair/models/sequence_tagger_model.py
    #response = {'status':'UP','version':__version__, 'model-name':'TODO'}

    return jsonify(response), 200
# end def

if __name__ == "__main__":
    logger.info(f"Starting server ...")
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
    #app.run(host='0.0.0.0', port=5000)
