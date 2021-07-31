import json
from robo import Robo
import sys

CONFIG_FILE = 'config.json'


def configure():
    global ASSISTENT_NAME
    global ACTIONS

    with open(CONFIG_FILE, "r") as config:
        configuracao = json.load(config)

        ASSISTENT_NAME = configuracao["name"]
        ACTIONS = configuracao["actions"]

        config.close()


def get_assistent_name():
    global ASSISTENT_NAME
    return ASSISTENT_NAME


def get_acction(text:str) -> str:
    global ACTIONS

    text = text.lower()

    for action in ACTIONS:
        for command in action['commands']:
            if command in text:
                return action['name']
        
    raise Exception(f'Comando {text} não encontrado!')


def execute_command(command: str, robo: Robo):
    if command == 'exit':
        print('Até a próxima!')
        sys.exit()

    if command == 'register_hour':
        robo.to_register_hour()

    if command == 'list_events':
        robo.list_events()