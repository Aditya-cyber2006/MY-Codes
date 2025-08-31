import speech_recognition as sr
import webbrowser
import pyttsx3
import music
import requests
import os

engine=pyttsx3.init()
r = sr.Recognizer()
run=True
def speak(text):
    engine.setProperty("rate",160)
    engine.say( text )
    engine.runAndWait()


def processing(task):
    if ("open " in task.lower()):
        l=task.lower().split()
        i=l.index("open")
        speak("copy that sir")
        webbrowser.open(f"https://www.{l[i+1]}.com/")   
    
    elif ("play"in task.lower()):
        speak("copy that sir")
        song=task.lower().split(" ")[1]
        link=music.music_library[song]
        webbrowser.open(link)

    
    elif ("shut down" in task.lower() or "shutdown" in task.lower()):
        
                speak("Shutting down now.")
                os.system("shutdown /s /t 1")
        
        

    elif "restart" in task.lower():
        speak("Restarting your PC")
        
        os.system("shutdown /r /t 1")


    elif "lock" in task.lower():
        print("processing...")
        os.system("rundll32.exe user32.dll,LockWorkStation")
        speak("Locking the computer now.")
                
        
    else : # (  "ai" in command.lower() ):
        print('Asking AI.')
        # with sr.Microphone() as source:
        #             audio = r.listen(source)
        print('Recognizing....')
        prompt=task            
        prompt=r.recognize_google(audio)
        print(f"Command:{prompt}")
        prompt=prompt+" give short response"
# Encode the prompt for a URL
        encoded_prompt = prompt.replace(" ", "%20")

# Create the URL
        url = f"https://text.pollinations.ai/{encoded_prompt}"

# Make the GET request
        response = requests.get(url)

        # Get the response text
        if response.status_code == 200:
            print(f"Response :{response.text}")
            speak( response.text)
        else:
            print("Error:", response.status_code)
                    
if __name__=="__main__":
    speak("Hello I am  Jarvis , Say jarvis to Activate me ")
while run:    
    r = sr.Recognizer()
        # recognize speech using Google Speech Recognition

    try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source)
            #Listen for the key word "Jarvis" to activate jarvis
            key_word=r.recognize_google(audio)

            if ("jarvis" in key_word.lower()):
                speak("Yes  Boss ")
            while run:
                try:
                    with sr.Microphone() as source:
                        print("Jarvis Activated....")
                        audio = r.listen(source)

                    command=r.recognize_google(audio)
                    print(command) 
                    processing(command)
                     
                except:
                    print(" Speech Recognition could not understand audio")
    except Exception as e:
            print(" Speech Recognition could not understand audio")
        

                   

                
        
