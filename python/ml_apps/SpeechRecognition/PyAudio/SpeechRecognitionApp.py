import speech_recognition as sr
import tkinter as tk
from tkinter import Label, Button, Text

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to recognize speech
def recognize_speech():
    try:
        # Capture audio from the microphone
        with sr.Microphone() as source:
            output_label.config(text="Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
            audio = recognizer.listen(source)  # Capture audio
            
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            result_textbox.delete("1.0", tk.END)  # Clear previous text
            result_textbox.insert(tk.END, text)  # Display the transcribed text
            output_label.config(text="Speech recognition complete!")
    except sr.UnknownValueError:
        output_label.config(text="Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        output_label.config(text=f"Could not request results: {e}")

# Create the GUI window
app = tk.Tk()
app.title("Speech Recognition App")
app.geometry("500x400")

# Add UI elements
instruction_label = Label(app, text="Click the button and start speaking:", font=("Arial", 14))
instruction_label.pack(pady=10)

recognize_button = Button(app, text="Start Speech Recognition", command=recognize_speech, font=("Arial", 12))
recognize_button.pack(pady=20)

output_label = Label(app, text="", font=("Arial", 12))
output_label.pack(pady=10)

result_textbox = Text(app, height=10, width=50, font=("Arial", 12))
result_textbox.pack(pady=10)

# Run the GUI application
app.mainloop()
