# 🤖 LangChain Gemini Agent with Tools

This project demonstrates how to build an **AI Agent using LangChain**, powered by **Google Gemini API** and custom tools.  
Here, we’ve added a simple tool that fetches a **random programming joke** from a public API. 🎭

---

## 🚀 Features
- 🔗 **LangChain Agent** setup with `AgentType.OPENAI_FUNCTIONS`
- 🤝 **Gemini LLM integration** via `langchain_google_genai`
- 🛠️ **Custom Tool Binding** (e.g., programming jokes)
- 🌍 **External API call** (Official Joke API)
- 📝 Easy to extend with more tools (weather, news, etc.)

---

## 📂 Project Structure
├── main.py # Entry point (LangChain agent + tool setup)
├── .env # Store your GEMINI_API_KEY
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## ⚙️ Setup & Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-username>/langchain-gemini-agent-tools.git
   cd langchain-gemini-agent-tools
2. **Create & activate virtual environment (recommended)**
  python -m venv venv
  source venv/bin/activate   # Mac/Linux
  venv\Scripts\activate      # Windows

3. **Install dependencies**
  pip install -r requirements.txt

4. **Set up environment variables**

Create a .env file in the root directory:
GEMINI_API_KEY=your_google_gemini_api_key

5. **RUN AGENT**
   python main.py

