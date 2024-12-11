import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import tkinter as tk
from tkinter import Label, Button, Text
import os

# Load the Whisper model
model = whisper.load_model("base")

# Function to record audio from the microphone
def record_audio(duration=5, filename="test.wav"):
    try:
        print("Recording...")
        fs = 16000  # Sampling frequency
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()  # Wait until recording is finished
        write(filename, fs, recording)  # Save as WAV file
        print("Recording complete. Saved as", filename)
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} was not created.")
        return filename
    except Exception as e:
        print("Error during recording:", e)
        return None

# Function to transcribe audio
def transcribe_speech():
    output_label.config(text="Recording...")
    filename = record_audio(duration=5, filename="test.wav")  # Record 5 seconds of audio
    output_label.config(text="Transcribing...")
    transcription = model.transcribe(filename)['text']  # Transcribe audio
    result_textbox.delete("1.0", tk.END)  # Clear previous text
    result_textbox.insert(tk.END, transcription)  # Display the transcription
    output_label.config(text="Transcription complete!")

# Create the GUI
app = tk.Tk()
app.title("Whisper Speech Recognition App")
app.geometry("500x400")

# Add UI elements
instruction_label = Label(app, text="Click the button to record and transcribe speech:", font=("Arial", 14))
instruction_label.pack(pady=10)

recognize_button = Button(app, text="Start Recording", command=transcribe_speech, font=("Arial", 12))
recognize_button.pack(pady=20)

output_label = Label(app, text="", font=("Arial", 12))
output_label.pack(pady=10)

result_textbox = Text(app, height=10, width=50, font=("Arial", 12))
result_textbox.pack(pady=10)

# Run the GUI application
app.mainloop()
