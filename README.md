<h1 align="center">🛸 Crazy WhatsApp Scheduler 3000 🚀</h1>

<p align="center">
  <img src="https://media.giphy.com/media/ZZ0DTzXzYtS2g/giphy.gif" width="250" alt="Alien Typing">
</p>

<p align="center">
  <b>Why type when a script can do it for you? 💬💻</b><br>
  Send WhatsApp messages like a pro – or like a prankster. Your call. 😎
</p>

---

## 🤯 What It Does

This Python script is your **personal WhatsApp agent** that:
- 📅 **Schedules messages** for any time you want.
- 🎭 Has a hilarious **Funny Mode** to surprise your friends.
- 🗣️ **Speaks out loud** what it’s doing (just in case you weren’t impressed enough).
- 🤖 Simulates sending messages using WhatsApp Web — no manual typing needed!

---

## 🧠 How It Works — Flowchart

```mermaid
graph TD
A[Start Script 🛸] --> B{Funny Mode?}
B -- Yes 😂 --> C[Pick Random Funny Message 🎲]
B -- No 🙃 --> D[Ask for Custom Message 💬]
C --> E[Choose Time ⏰]
D --> E
E --> F{Send Now or Later?}
F -- Now 🚀 --> G[Add 2-Min Buffer ⏳]
F -- Schedule ⌛ --> H[Ask for Time]
G --> I[Confirm Details ✅]
H --> I
I --> J{User Confirms?}
J -- Yes 🙌 --> K[Countdown ⏳ -> Send via pywhatkit 💥]
J -- No ❌ --> L[Cancel & Exit 👋]
