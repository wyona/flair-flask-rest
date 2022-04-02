from flair.data import Sentence
from flair.models import SequenceTagger

tagger = SequenceTagger.load('ner')

#sentence = Sentence('When was Alexander von Humboldt born?')
sentence = Sentence('When were Alexander von Humboldt and Bernhard Riemann born?')

tagger.predict(sentence)

for entity in sentence.get_spans('ner'):
    print(entity)
