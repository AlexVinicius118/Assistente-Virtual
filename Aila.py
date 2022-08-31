import speech_recognition as sr
import playsound
from gtts import gTTS, tts
import random
import webbrowser
import pyttsx3
import os

class Virtual_assit():
    def __init__(self, assist_name, person):
        self.person = person
        self.assit_name = assist_name

        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()
        
        self.voice_data = ''

    def engine_speak(self, text):
        """
        Fala da assitente virtual
        """
        text = str(text)
        self.engine.say(text)
        self.engine.runAndWait()

    def record_audio(self, ask=""):


        with sr.Microphone() as source:
            if ask:
                print('Ouvindo...')
                #self.engine_speak(ask)
            
            audio = self.r.listen(source, 5, 5)# pega dados de auido
            print('Salvando, informações no banco de dados')
            try:
                self.voice_data = self.r.recognize_google(audio, language="pt-BR") #converte audio para texto

            except sr.UnknownValueError:
                self.engine_speak('Desculpa, não entendi o que você disse. Por favor, pode repetir?')

            except sr.RequestError:
                self.engine_speak('Desculpe, meu servidor está inativo') # recognizer is not connected

            print(">>",self.voice_data.lower()) #imprime o que vc disse
            self.voice_data = self.voice_data.lower()

            return self.voice_data.lower()

    def engine_speak(self, audio_strig):
        audio_strig = str(audio_strig)
        tts = gTTS(text=audio_strig, lang='pt-br')
        r = random.randint(1,20000)
        audio_file = 'audio' + str(r) + '.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(self.assit_name + ':', audio_strig)
        os.remove(audio_file)


    def there_exist(self, terms):
        """
        Função para identificar se o termo existe
        """
        for term in terms:
            if term in self.voice_data:
                return True


    def respond(self, voice_data):
        if self.there_exist(['hey', 'hi', 'hello', 'oi', 'holla', 'aila', 'oi aila']):
            greetigns = [f'Hi {self.person}, O que deseja fazer hoje?',
                        'Oi chefe, como posso te ajudar?',
                        'Olá chefe, o que precisa?']

            greet = greetigns[random.randint(0,len(greetigns)-1)]
            self.engine_speak(greet)
         
        #Situação da assistente
        if self.there_exist(['como você está', 'como voce esta', 'tudo bem']):
            greetigns = [f'Hi {self.person}, Estou ótima, obrigado por perguntar',
                        'Estou entediada, por favor me tire do tedio',
                        'Estou triste, você me esqueceu']

            greet = greetigns[random.randint(0,len(greetigns)-1)]
            self.engine_speak(greet)

        #Pesquisa no Google
        if self.there_exist(['procure']) and 'youtube' not in voice_data:
            search_term = voice_data.split("procure")[-1]
            url =  "http://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            self.engine_speak("Aqui está o que eu encontrei para " + search_term + 'on google')

        #Pesquisa no Youtube
        if self.there_exist(["procurar no youtube"]):
            search_term  = voice_data.split("procurar no")[-1]
            url = "http://www.youtube.com/results?search_query=" + search_term
            webbrowser.get().open(url)
            self.engine_speak("Aqui está o que eu encontrei para" + search_term + 'on youtube')

        #Calculos de matematica
        #if self.there_exist(['quanto é']):
        #
        #
        
        
        #spa entrar no sistema de fiscal
        if self.there_exist(['open sap']):
            pass


assistent = Virtual_assit('Ayla', 'Alex')

while True:

    voice_data = assistent.record_audio('Escutando...')
    assistent.respond(voice_data)

    if assistent.there_exist(['bye', 'obrigado', 'tchal', 'até logo', 'até logo', 'tchau', 'thanks']):
        assistent.engine_speak("Até logo")
        
        break