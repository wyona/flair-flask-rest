# https://github.com/flairNLP/flair/blob/master/resources/docs/TUTORIAL_7_TRAINING_A_MODEL.md
import flair.datasets

corpus = flair.datasets.UD_ENGLISH()

print('')

# print the number of Sentences in the train split
print('Length corpus train: ',len(corpus.train))

# print the number of Sentences in the test split
print('Length corpus test: ',len(corpus.test))

# print the number of Sentences in the dev split
print('Length corpus dev: ',len(corpus.dev))

# print the first Sentence in the training split
print('')
print(corpus.test[0])

# print the first Sentence in the training split
print('')
print('PoS tags: ',corpus.test[0].to_tagged_string('pos'))
