import speech_recognition as sr

def listen_microphone():
    while(True):
        microphone = sr.Recognizer()
        sentence = ""

        with sr.Microphone() as source:
            microphone.adjust_for_ambient_noise(source)
            print(":")

            audio = microphone.listen(source)

        try:
            sentence = microphone.recognize_google(audio, language='pt-BR')

            print("said: ", sentence)

        except sr.UnknownValueError:
            print("não entendi")

        if(sentence): return sentence