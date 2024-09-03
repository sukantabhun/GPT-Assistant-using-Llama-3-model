from groq import Groq
from apikey import api_data
import speech_recognition as sr
import pyttsx3
import webbrowser

#Model and API settings
Model = "llama3-8b-8192"
client = Groq(api_key=api_data)

#API connection
def Reply(question):
    completion = client.chat.completions.create(
        model=Model,
        messages=[
            {'role':'system',"content":"You are a helpfull assisatant"},
            {'role':'user',"content":question}
        ],
        max_tokens=200
    )
    answer = completion.choices[0].message.content
    return answer


#text to speech for reply
engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(Text):
    engine.say(Text)
    engine.runAndWait()

speak("Hello, How may I help you today?")


#speech to text for input
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listining....')
        r.pause_threshold = 1 # Setting the wait time to 1 sec before listining
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language = 'en-in')
        print("User said: {} \n".format(query))
    except Exception as e:
        print('Say that again')
        return "None"
    return query

if __name__ == '__main__':
    while True:
        query = takeCommand().lower()
        if(query=='None'):
            continue
            
        ans = Reply(query)
        print(ans)
        speak(ans)

        # Broweser related tasks
        if 'Open youtube' in query:
            webbrowser.open('www.youtube.com')
        if 'Open google' in query:
            webbrowser.open('www.google.com')
        if 'bye' in query:
            break