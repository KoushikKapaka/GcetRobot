from chatterbot import ChatBot
from chatterbot.comparisons import LevenshteinDistance
import pyttsx3
import speech_recognition as sr


bot = ChatBot('GreetBot',preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],logic_adapters=[{
                'import_path': 'chatterbot.logic.BestMatch',
                'threshold': 0.90,
                'default_response': 'I am sorry, I am new to it.'
            }
    ],statement_comparison_function=LevenshteinDistance)
engine = pyttsx3.init()
r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        audio = r.listen(source,timeout=10000)
        req = r.recognize_google(audio)
    engine.say(bot.get_response(req))
    engine.runAndWait()
