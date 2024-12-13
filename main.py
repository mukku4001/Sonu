import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')  # Get list of available voices

# Use a valid index for voice
if len(voices) > 1:  # Check if there are at least 2 voices available
    engine.setProperty('voice', voices[1].id)  # Use the second voice
else:
    engine.setProperty('voice', voices[0].id)  # Use the first voice as fallback

engine.setProperty('rate', 150)  # Set the speech rate

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    content = ""  # Initialize content as an empty string
    while content == "":  # Corrected condition
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            speak( "bolo" )
            audio = r.listen(source)

        try:
            content = r.recognize_google(audio, language='en-in')
            print("You said: " + content)
            speak( content)
        except Exception as e:
            print("Mukku, can you speak again?")
            speak("Mukku, can you speak again?")
    return content

def main_process():
    while True:
        request = command().lower()
        if "hello baby" in request:
            speak("Welcome Mukku, Sonu tumhari seva me hajir hai.")
            while True:  
                request = command().lower()

                if "play music" in request:
                    speak("Playing your favorite music.")
                    try:
                        song = random.randint(1, 3)
                        if song == 1:
                            webbrowser.open("https://youtu.be/FwKDTtGO7FU?si=OytWmXjZvp8DMnAn")
                        elif song == 2:
                            webbrowser.open("https://youtu.be/dFSVuC_8fV0?si=_m6MJng1HFTqvCWR")
                        elif song == 3:
                            webbrowser.open("https://youtu.be/RV7aHXRGsX0?si=RWGzwS_C4IhuqKXq")
                    except Exception as e:
                        speak("Sorry Mukku, I couldn't open the music link.")
                elif "exit" in request:
                    speak("Goodbye Mukku!")
                    return
                elif "hello baby" in request:
                    speak("Sonu ab sun raha hai, aapka agla aadesh kya hai?")
                    break  
                elif "time batao" in request:
                    now_time = datetime.datetime.now().strftime("%H:%M")  # Get current time
                    speak("Abhi ka samay hai " + now_time)
                elif "date batao" in request:
                    now_date = datetime.datetime.now().strftime("%d:%m:%Y")  # Get current date
                    speak("Aaj ki taarikh hai " + now_date)
                elif "new task" in request:
                    task = request.replace("new task", "new task is ")
                    if task != "":
                        speak("adding task : " +task)
                        with open ("todo.txt","a") as file:
                            file.write(task)
main_process()
