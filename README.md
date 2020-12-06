# flair-flask-rest

## Quick Start

Requirements

Install flair NLP

```
https://github.com/flairNLP/flair
```

Run Flair NER as REST Service

```
python flair-ner-as-service.py
```

Test it

```
curl --request POST --url http://localhost:5000/api/v1/ner --header 'content-type: application/json' --data '{ "message":"When were Alexander von Humboldt and Bernhard Riemann born?" }'
```

And you should receive the following response

```
{"entities":"TODO","scores":[0.9963508248329163,0.9994429349899292],"submitted-message":"When were Alexander von Humboldt and Bernhard Riemann born?","texts":["Alexander von Humboldt","Bernhard Riemann"]}
```
