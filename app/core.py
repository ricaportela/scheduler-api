from flask import Flask

agendamento_app = Flask('agendamento_app')


@agendamento_app.route('/')
def home():
    return 'agendamentos'


