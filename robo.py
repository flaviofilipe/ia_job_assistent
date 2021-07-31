from datetime import datetime
from schedule import current_schedule
import speech_recognition as sr


class Robo:
    def __init__(self, name:str) -> None:
        self.name = name
        self.language = "pt-BR"
        self.recognizer = sr.Recognizer()

    def __str__(self) -> str:
        return f'Eu sou {self.name}'
        
    def listen(self) -> str:
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("\nFale alguma coisa...")
            audio_data = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
            return self._speak(audio_data)
        

    def _speak(self, audio_data: sr.AudioData):
        try:
            print("\nProcessando...\n")
            texto = self.recognizer.recognize_google(audio_data, language=self.language)
            print("Você falou:", texto)
            return(texto)

        except sr.UnknownValueError:
            raise Exception("Não entendi o que você disse!")


    def to_register_hour(self):
        now = datetime.today()
        print('Registrando ponto', now.isoformat(' ', 'minutes'))


    def list_events(self):
        for event in current_schedule:
            date = event['date'].isoformat(' ', 'minutes')
            msg = f"{event['title']} | {date}"
            print(msg, '\n')
