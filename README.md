# flair-flask-rest

## Quick Start

Install [flair NLP](https://github.com/flairNLP/flair)

```
pip3 install flair
```

or update

```
pip3 show flair
sudo pip3 install flair --upgrade
pip3 show flair
```

Run Flair NER as REST Service, whereas make sure that port 5000 is available

```
python3 flair-ner-rest.py
```

Test it

Check health

```
curl --request GET --url http://localhost:5000/api/v1/health
```

Get named entities

```
curl --request POST --url http://localhost:5000/api/v1/ner --header 'content-type: application/json' --data '{ "message":"When were Alexander von Humboldt and Bernhard Riemann born?" }'
```

And you should receive the following response

```
{"entities":[{"score":0.9963508248329163,"tag":"PER","text":"Alexander von Humboldt"},{"score":0.9994429349899292,"tag":"PER","text":"Bernhard Riemann"}],"flair-version":"0.7","submitted-message":"When were Alexander von Humboldt and Bernhard Riemann born?"}
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

## How to build and run Docker

### CPU

```bash
docker build -t flair-ner-cpu -f ./Dockerfile.cpu .
```

```bash
docker run -p 5000:5000 flair-ner-cpu
```

Test it

```
curl --request POST --url http://localhost:5000/api/v1/ner --header 'content-type: application/json' --data '{ "message":"When were Alexander von Humboldt and Bernhard Riemann born?" }'
```

## How to upload to Docker Hub

```
docker tag flair-ner-cpu USERNAME/REPONAME:flair-ner-cpu_VERSION
```

```
docker login -u USERNAME -p PASSWORD docker.io && docker push USERNAME/REPONAME:flair-ner-cpu_VERSION
```

whereas for example USERNAME is michaelwechner, REPONAME is public and VERSION is 0.7-1

https://hub.docker.com/r/michaelwechner/public/tags

## How to finetune flair

- Tagging / Labeling Dataset: https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)
- Adding new Entities to Flair NER models: https://discuss.huggingface.co/t/adding-new-entities-to-flair-ner-models/3913
