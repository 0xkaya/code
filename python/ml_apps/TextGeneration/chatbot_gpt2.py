import tkinter as tk
from tkinter import scrolledtext
from transformers import pipeline

# Load GPT-2 pipeline
print("Loading GPT-2 model. This may take a while...")
generator = pipeline("text-generation", model="openai-community/gpt2")
# Function to generate GPT-2 response
def get_gpt2_response(prompt):
    try:
        # Generate response with GPT-2
        response = generator(prompt, max_length=100, num_return_sequences=1)
        return response[0]['generated_text'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Function to handle user input and display chatbot responses
def send_message():
    user_message = user_input.get()
    if user_message.strip():  # Ensure input is not empty
        chat_history.insert(tk.END, "You: " + user_message + "\n")
        user_input.delete(0, tk.END)  # Clear input field

        # Generate GPT-2 response
        response = get_gpt2_response(user_message)
        # Display chatbot response
        chat_history.insert(tk.END, "Chatbot: " + response + "\n")
        chat_history.see(tk.END)  # Scroll to the end of chat history

# Create the main GUI window
root = tk.Tk()
root.title("GPT-2 Chatbot")
root.geometry("700x500")

# Chat history display
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.NORMAL, font=("Arial", 12))
chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# User input frame
user_input_frame = tk.Frame(root)
user_input_frame.pack(pady=5, padx=10, fill=tk.X)

user_input = tk.Entry(user_input_frame, font=("Arial", 12))
user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

# Send button
send_button = tk.Button(user_input_frame, text="Send", font=("Arial", 12), command=send_message)
send_button.pack(side=tk.RIGHT)

# Start the Tkinter event loop
root.mainloop()
