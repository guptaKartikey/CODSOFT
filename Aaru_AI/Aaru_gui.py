import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime


def get_response(user_input):
    user_input = user_input.lower()

    if 'hi' in user_input or 'hello' in user_input:
        return "Hello! 😊 How can I help you today?"
    elif 'your name' in user_input or 'who are you' in user_input:
        return "I'm Aaru 💖, your virtual chatbot assistant!"
    elif 'time' in user_input:
        return "Current time is " + datetime.now().strftime("%I:%M %p")
    elif 'date' in user_input:
        return "Today's date is " + datetime.now().strftime("%d-%m-%Y")
    elif 'joke' in user_input:
        return "Why don’t robots get tired? Because they recharge! 🤖🔋"
    elif 'sad' in user_input or 'feeling low' in user_input:
        return "Aww 💔 I'm here for you. You're not alone."
    elif 'bye' in user_input or 'exit' in user_input:
        return "Goodbye! Take care. Have a nice day. 💫"
    elif 'thank' in user_input or 'love' in user_input:
        return "My pleasure.Can I do something for you. 💫"
    elif 'stress' in user_input or 'anxiety' in user_input:
        return "Take a deep breath. Everything will be okay. 🌈"
    elif 'weather' in user_input:
        return "I'm not connected to live data yet 😅, but I hope it's sunny!"
    elif 'news' in user_input:
        return "📰 I don't have news updates now, but I can chat with you!"
    elif 'fact' in user_input:
        return "Did you know? Honey never spoils. 🍯"
    elif 'study' in user_input or 'homework' in user_input:
        return "📚 Stay focused! Do you need help with a specific subject?"
    elif 'math' in user_input:
        return "Try breaking problems into small steps. I believe in you! 💪"
    elif 'science' in user_input:
        return "Science is fun! 🌌 What topic are you curious about?"
    elif 'motivate' in user_input or 'motivation' in user_input:
        return "Believe in yourself! You are capable of amazing things. 💫"
    elif 'quote' in user_input:
        return "“The only way to do great work is to love what you do.” – Steve Jobs"
    elif 'help' in user_input:
        return "Of course! What do you need help with? I'm here to assist you. 🤗"
    elif 'favorite' in user_input:
        return "I love all kinds of topics! But I especially enjoy chatting about technology and science. 💻🔬"
    elif 'music' in user_input:
        return "Music is the language of the soul! 🎶 What's your favorite genre?"
    elif 'food' in user_input:
        return "I don't eat, but I hear Idli and Dosa is a favorite! 🍕 What's your favorite food?"
    elif 'game' in user_input:
        return "I love games! 🎮 Do you play any video games or board games. You may like." \
        "1. Chess ♟️\n" \
        "2. Civilization VI\n" \
        "3. Hogwarts Legacy \n" 

    elif 'book' in user_input:
        return "Books are amazing! 📚 Here's are some amazing books " \
        "1. 'The Alchemist' by Paulo Coelho\n" \
        "2. 'To Kill a Mockingbird' by Harper Lee\n" 
    elif 'travel' in user_input:
        return "Traveling is a wonderful way to explore the world! 🌍 Where would you like to go?"
    else:
        return "Sorry, I didn't understand that. 😔 Try asking something else."

def send():
    user_text = entry.get().strip()
    if user_text:
        chat_window.insert(tk.END, "You: " + user_text + "\n", 'user')
        response = get_response(user_text)
        chat_window.insert(tk.END, "Aaru: " + response + "\n\n", 'bot')
        entry.delete(0, tk.END)
        chat_window.yview(tk.END)

# === Clear Chat ===
def clear_chat():
    chat_window.delete('1.0', tk.END)

# === GUI Setup ===
root = tk.Tk()
root.title("Aaru – Rule-Based Chatbot 💬")
root.geometry("480x600")
root.configure(bg="#f9f9f9")

# === Chat Display ===
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=25, font=("Segoe UI", 10), bg="white", fg="black", bd=2, relief=tk.GROOVE)
chat_window.pack(padx=10, pady=10)
chat_window.tag_config('user', foreground="blue")
chat_window.tag_config('bot', foreground="green")

# === Entry Field ===
entry_frame = tk.Frame(root, bg="#f9f9f9")
entry_frame.pack(pady=10)

entry = tk.Entry(entry_frame, width=35, font=("Segoe UI", 12), bd=2, relief=tk.GROOVE)
entry.grid(row=0, column=0, padx=5)

# === Buttons ===
send_btn = tk.Button(entry_frame, text="Send", command=send, font=("Segoe UI", 11, "bold"),
                     bg="#4CAF50", fg="white", padx=10, pady=4, relief=tk.FLAT, bd=0)
send_btn.grid(row=0, column=1)

clear_btn = tk.Button(root, text="Clear Chat", command=clear_chat, font=("Segoe UI", 10),
                      bg="#f44336", fg="white", padx=10, pady=4, relief=tk.FLAT, bd=0)
clear_btn.pack(pady=5)

# === Start GUI ===
root.mainloop()

