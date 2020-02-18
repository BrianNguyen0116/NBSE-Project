import speech_recognition as sr

r = sr.Recognizer()


def speech():
    with sr.Microphone() as source:
        print('Say something')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print('You said : {}'.format(text))
        except:
            print('didnt work')

    return text