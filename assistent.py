from datetime import datetime

current_schedule = [
    {
        'title': 'Reunião Marketing',
        'date': datetime(2021, 8, 20, 10, 15)
    },
    {
        'title': 'Reunião de projetos',
        'date': datetime(2021, 8, 20, 11)
    },
    {
        'title': 'Aula de IA',
        'date': datetime(2021, 8, 10, 19, 20)
    },
]


def to_register_hour():
    now = datetime.today()
    print('Registrando ponto', now.isoformat(' ', 'minutes'))


def list_events():
    for event in current_schedule:
        date = event['date'].isoformat(' ', 'minutes')
        msg = f"{event['title']} | {date}"
        print(msg, '\n')
