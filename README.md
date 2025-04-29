# 🧠 AI Q&A ChatBot

A simple, clean, and interactive chatbot built with **Streamlit**, **LangChain**, and **OpenAI** models like `gpt-4o`, `gpt-4-turbo`, and `gpt-4`.  
This chatbot can answer user questions smartly by directly integrating with OpenAI APIs, while giving users full control over model settings through a friendly web interface.

---

## 🚀 Project Flow

1. **Environment Setup**:  
   - We use `.env` file to store environment variables like `LANGCHAIN_API_KEY`. (⚡Note: The **OpenAI API Key** is entered by the user at runtime, not hardcoded.)

2. **LangChain Setup**:  
   - LangChain's `ChatPromptTemplate` is used to design the chat prompt.
   - The `ChatOpenAI` LLM (Language Learning Model) is initialized dynamically based on user-selected settings like model name, temperature, and max tokens.

3. **Backend Processing**:  
   - A simple pipeline is built: **Prompt** ➔ **LLM Model** ➔ **Output Parser** ➔ **Final Answer**.
   - The backend function `generate_answer()` handles this flow when a user submits a question.

4. **Frontend UI with Streamlit**:  
   - Sidebar: Allows users to input their **OpenAI API Key**, choose the **LLM model**, and adjust **creativity (temperature)** and **maximum tokens**.
   - Main Page: Provides a clean text input for asking questions and displays the AI-generated response inside a styled card.

5. **User API Key Handling**:  
   - Users **input** their **OpenAI API Key** directly into the sidebar (frontend).  
   - **Important**: The API Key is **NOT saved** anywhere. It is only used during the session for generating responses.

---

## 🛠 How to Run This Project

Follow these simple steps:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-qa-chatbot.git
cd ai-qa-chatbot
```

### 2. Create and Activate a Virtual Environment
```bash
# Create a virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File
Inside the project root, create a `.env` file and add:
```
LANGCHAIN_API_KEY=your-langchain-api-key-here
```
(You can get a free key by signing up for [LangChain](https://www.langchain.com/).)

⚡ **Note**: You don't need to add your OpenAI API Key here. You'll enter it at runtime through the sidebar.

---

### 5. Run the App
```bash
streamlit run app.py
```
(assuming your file is named `app.py`.)

---

## ✨ Features

- 🛡️ Secure API Key Input: Users directly input OpenAI keys — no backend storage.
- 🎨 Adjustable Creativity: Choose how "creative" or "precise" you want the AI to be.
- 🚀 Multiple Model Choices: GPT-4o, GPT-4-Turbo, GPT-4.
- ⚙️ Configurable Max Token Output: Control how long or short the responses are.
- 🖥️ Clean and Responsive UI: Stylish cards and custom fonts.

---

## 📷 Preview

| Ask a question | Get the response |
|:--------------:|:----------------:|
| ![User Input](https://via.placeholder.com/300x200.png?text=User+Question) | ![Bot Response](https://via.placeholder.com/300x200.png?text=Assistant+Response) |

---

## 📌 Important Notes
- **OpenAI API Key** must have sufficient quota or usage limits.
- **LangChain API Key** is required for internal tracing/debugging (optional but recommended).
- No API keys are stored on the server — 100% user-controlled sessions.

---

## 📚 Tech Stack

- [Streamlit](https://streamlit.io/) — For building fast interactive web apps
- [OpenAI API](https://platform.openai.com/) — LLM model responses
- [LangChain](https://www.langchain.com/) — To chain prompts and models elegantly
- [Python Dotenv](https://pypi.org/project/python-dotenv/) — For managing environment variables securely

---

---

## 📄 License

This project is licensed under the MIT License.

---
