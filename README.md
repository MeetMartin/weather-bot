# weather-bot
Rasa NLU/Core Weather Bot

Current configuration supports training, command-line interface and HTTP server API.

## Dependencies

- pip install rasa_nlu
- pip install rasa-core
- pip install weather-api

## Train

First you need to train your bot. You can do that by simply running: *python trainer.py train-all*

This will train both the NLU and Stories using Tensorflow machine learning.

## Run CMD

To run in command line just call: *python bot.py run*

## Run Server

To run as a server you need to call: *python -m rasa_core.server -d models/dialogue -u models/nlu/default/current -o models/out.log*

You talk to the server through API as: *curl -XPOST localhost:5005/conversations/default/respond -d '{"query":"hi"}'*

Documentation: http://rasa.com/docs/core/http/

## 3rd Party Documentations

- Rasa NLU: http://rasa.com/docs/nlu/
- Rasa Core: http://rasa.com/docs/core/
- Weather API: https://pypi.org/project/weather-api/ (Yahoo! Weather)