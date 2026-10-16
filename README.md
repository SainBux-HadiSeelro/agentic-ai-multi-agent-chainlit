# 🤖 Multi-Agent Orchestration System with OpenAI Agents SDK & Gemini

An intelligent multi-agent conversational platform powered by **OpenAI Agents SDK**, **Google Gemini (2.5 Flash Lite)**, and **Chainlit**.

## 🌟 Features
- **Central Manager Agent**: Analyzes user intent and automatically delegates tasks to specialist agents.
- **Specialized Agents**:
  - 🌐 **Web Developer Agent**: Builds responsive, modern, and performant web apps.
  - 📱 **App Developer Agent**: Mobile and cross-platform app design & architecture.
  - 📈 **Marketing Expert Agent**: Creates launch strategies and marketing campaigns.
- **Dynamic Handoffs**: Bidirectional handoffs allow smooth transitions between agents across multi-turn chats.
- **Interactive Web Interface**: Real-time conversational UI built with Chainlit.

---

## 🛠️ Tech Stack
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python)
- [Google Gemini API](https://ai.google.dev/)
- [Chainlit](https://chainlit.io/)
- Python 3.12+

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/SainBux-HadiSeelro/agentic-ai-multi-agent-chainlit.git
cd agentic-ai-multi-agent-chainlit
```

### 2. Configure Environment Variables
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. Run the Application
In Windows:
```cmd
run
```
Or directly with Python:
```cmd
.venv\Scripts\python.exe -m chainlit run main.py -w
```
Or using `uv`:
```bash
uv run python -m chainlit run main.py -w
```

Access the interface in your browser at `http://localhost:8000`.
