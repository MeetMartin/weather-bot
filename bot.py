from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import warnings

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.channels.console import ConsoleInputChannel


def run(serve_forever=True):
    interpreter = RasaNLUInterpreter("models/nlu/default/current")
    agent = Agent.load("models/dialogue", interpreter=interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent


if __name__ == '__main__':
    warnings.filterwarnings(action='ignore', category=DeprecationWarning)
    utils.configure_colored_logging(loglevel="INFO")

    parser = argparse.ArgumentParser(
            description='starts the bot')

    parser.add_argument(
            'task',
            choices=["train-nlu", "train-dialogue", "run"],
            help="what the bot should do?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "run":
        run()
