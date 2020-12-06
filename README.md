# flair-flask-rest

## Quick Start

Install [flair NLP](https://github.com/flairNLP/flair)

Run Flair NER as REST Service, whereas make sure that port 5000 is available

```
python flair-ner-rest.py
```

Test it

```
curl --request POST --url http://localhost:5000/api/v1/ner --header 'content-type: application/json' --data '{ "message":"When were Alexander von Humboldt and Bernhard Riemann born?" }'
```

And you should receive the following response

```
{"entities":[{"score":0.9963508248329163,"text":"Alexander von Humboldt"},{"score":0.9994429349899292,"text":"Bernhard Riemann"}],"flair-version":"0.7","submitted-message":"When were Alexander von Humboldt and Bernhard Riemann born?"}
```

Run Flair Sentiment as REST Service, whereas make sure that port 5000 is available

```
python flair-sentiment-rest.py
```

Test it

```
curl --request POST --url http://localhost:5000/api/v1/analyzeSentiment --header 'content-type: application/json' --data '{ "message":"I could watch The Marriage over and over again. At 90 minutes, it'\''s just so delightfully heartbreaking." }'
```

And you should receive the following response

```
{"polarity":0.9978204965591431,"result":"POSITIVE"}
```
