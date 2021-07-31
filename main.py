import sys
from assistent import list_events, to_register_hour
import speech_recognition as sr


def interpreter_microfone():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        text = listen(recognizer, source)
        execute_command(text)
        interpreter_microfone()


def listen(recognizer: sr.Recognizer, source: sr.Microphone):
    print("Fale alguma coisa...")
    fala = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("\nProcessando...\n")
        texto = recognizer.recognize_google(fala, language="pt-BR")
        print("Você falou:", texto)
        return(texto)

    except sr.UnknownValueError:
        msg = "Não entendi o que você disse!"
        print(msg)
        interpreter_microfone()


def execute_command(text: str):
    text = text.lower()
    salutation_words = ['bom dia', 'boa noite']
    events_words = ['agenda', 'eventos', 'reuniões']

    if 'tchau' in text:
        print('Até a próxima!')
        sys.exit()

    for word in salutation_words:
        if word in text:
            to_register_hour()

    for word in events_words:
        if word in text:
            list_events()



if __name__ == '__main__':
    interpreter_microfone()
