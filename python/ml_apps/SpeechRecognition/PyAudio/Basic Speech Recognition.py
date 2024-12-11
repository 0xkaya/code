import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Adjusting for ambient noise... Please wait")
    recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for noise
    print("Listening...")
    audio = recognizer.listen(source)  # Capture audio

try:
    # Recognize speech using Google Web Speech API
    print("Recognizing...")
    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")
