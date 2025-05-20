**🤖 Rule Based Chatbot**

    This is a smart chatbot application built using **Streamlit** that combines **rule-based responses** with **Groq’s LLaMA 3 (8B)** API as a fallback when the chatbot doesn't recognize an input. It provides a real-time, interactive chat experience with both fixed and AI-generated answers.

**🚀 Features**

      - ✅ Rule-Based Pattern Matching
      - 🤖 LLM Fallback using Groq's LLaMA 3
      - 💬 Chat-style UI with Streamlit
      - 🧪 PyTest for Unit Testing
      - 🧼 Clean & Modular Codebase

**📂 Project Structure**


├── app.py               # Streamlit UI
├── chatbot.py           # Rule-based + LLM fallback logic
├── test_chatbot.py      # Unit tests using PyTest
├── requirements.txt     # Python dependencies              
└── README.md            # Full project documentation

**🛠️ Getting Started**

1. Clone the Repo
  git clone https://github.com/ManasPatni/Rule-Based-Chatbot
  cd Rule-Based-Chatbot

2. Install Requirements
   pip install -r requirements.txt

3. Run the Chatbot (Main Version)
   streamlit run app.py

**🧪 Run Tests**
    pytest

**👨‍💻 Author**
  Built with ❤️ by Manas Patni



