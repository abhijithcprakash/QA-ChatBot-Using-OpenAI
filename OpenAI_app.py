import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Langsmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = "Simple Q&A Chatbot with OpenAI"

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Answer the questions to the best of your knowledge."),
        ("user", "Question: {question}")
    ]
)

# Function to generate answer
def generate_answer(question, api_key, llm_model, temperature, max_token):
    openai.api_key = api_key
    llm = ChatOpenAI(model=llm_model, temperature=temperature, max_tokens=max_token)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

# Streamlit page config
st.set_page_config(page_title="AI Q&A Assistant", page_icon="🧠", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
    body {
        background-color: #F5F7FA;
    }
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #333333;
    }
    .sub-font {
        font-size:18px !important;
        color: #555555;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown('<p class="big-font">🧠 AI Q&A ChatBot</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-font">Ask anything and get smart answers powered by OpenAI models.</p>', unsafe_allow_html=True)

# Sidebar Settings
with st.sidebar:
    st.title("⚙️ Settings")
    api_key = st.text_input("🔑 Enter your OpenAI API Key:", type="password")
    llm_model = st.selectbox("🤖 Choose Model", ["gpt-4o", "gpt-4-turbo", "gpt-4"])
    temperature = st.slider("🎯 Creativity (Temperature)", min_value=0.0, max_value=1.0, value=0.7)
    max_token = st.slider("📝 Max Tokens", min_value=50, max_value=400, value=150)

# User Input Section
st.markdown("---")
st.write("👨‍💻 **Type your question below:**")
user_input = st.text_input("You:")

# If user gives input
if user_input:
    if not api_key:
        st.error("🔒 Please enter your OpenAI API Key in the sidebar.")
    else:
        with st.spinner("Generating a smart answer... 🚀"):
            response = generate_answer(user_input, api_key, llm_model, temperature, max_token)

        # Display in a nice card
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(f"**You asked:** {user_input}")
        st.markdown("---")
        st.markdown(f"**🧠 Assistant:** {response}")
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("💬 Please ask a question above to get started.")

