import pywhatkit
from datetime import datetime, timedelta
import time
import random
import pyttsx3  # For speaking out loud
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Fun/Surprise messages
funny_messages = [
    "You're not ugly, you're just not my type 😎",
    "I don't have bad handwriting. I have my own font ✍️",
    "Stop staring at your phone... oh wait, too late 😅",
    "You're amazing. Don't forget that. Even when your Wi-Fi sucks 💡",
    "Sending this because you're 1 in a Minion 🟡"
]

# Function to send message
def send_message(mobile, message, hour, minute):
    print(f"\nScheduling message to {mobile} at {hour}:{minute}")
    engine.say("Message scheduled. Please don't touch your mouse or keyboard.")
    engine.runAndWait()
    pywhatkit.sendwhatmsg(mobile, message, hour, minute)
    print("✅ Message sent successfully!")
    engine.say("Boom! Mission accomplished.")
    engine.runAndWait()

# Begin program
print("🛸 Welcome to Crazy WhatsApp Scheduler 3000 🛸\n")

mobile = input('📱 Enter Mobile No of Receiver (with country code, e.g. +91xxxxxxxxxx): ')
mode = input("💡 Do you want to activate Funny Mode? (yes/no): ").strip().lower()

if mode == "yes":
    message = random.choice(funny_messages)
    print("😂 Funny mode activated! Here's your surprise message:\n👉", message)
else:
    message = input('💬 Enter the message you want to send: ')

choice = input(" Do you want to send it now or schedule? (now/schedule): ").strip().lower()
now = datetime.now()

if choice == "now":
    scheduled_time = now + timedelta(minutes=2)
    hour = scheduled_time.hour
    minute = scheduled_time.minute
else:
    hour = int(input('⏰ Enter hour (24-hour format): '))
    minute = int(input('⏰ Enter minute: '))

# Confirmation step
print(f"\n📨 Final Preview:\nTo: {mobile}\nMessage: {message}\nTime: {hour}:{minute}")
confirm = input(" Confirm? (yes/no): ").strip().lower()

if confirm == "yes":
    for i in range(5, 0, -1):
        print(f"⏳ Sending in {i} seconds...")
        time.sleep(1)
    send_message(mobile, message, hour, minute)
else:
    print("❌ Message cancelled by user.")
    engine.say("Message cancelled. You're safe, agent.")
    engine.runAndWait()
