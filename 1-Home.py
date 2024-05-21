import streamlit as st
from groq import Groq
import pdfplumber

# Get the Groq API key from Streamlit secrets
api_key = st.secrets["groq"]["api_key"]

client = Groq(api_key=api_key)
# import necessary libraries for colbert method

# Load and convert document into embeddings
doc_path = "documents\\critical-minerals-africa-senior-study-group-final-report.pdf"

# Create Streamlit app
st.title("Ultra-Fast Document Chatbot")
st.header("Executive Summary")
# Generate and display TLDR summary
client = Groq(api_key="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")

# Load the document content

@st.cache_data
def get_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

doc_content = get_text_from_pdf(doc_path)

summary_completion = client.chat.completions.create(
    model="gemma-7b-it",
    messages=[
        {
            "role": "user",
            "content": "Summarize this long document"
        },
        {
            "role": "assistant",
            "content": f"Load the document from {doc_path} and summarize it"
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)
summary = ""
for chunk in summary_completion:
    summary += chunk.choices[0].delta.content or ""
st.write(summary)

# Implement chat interface
st.header("Chat with the Document")
user_input = st.text_input("Your question")
suggestions = ["What is the primary concern of the US regarding critical minerals?", 
               "Why are critical minerals important for modern economies?", 
               "What role does Africa play in the global supply chain of critical minerals?",
               "What challenges are associated with mining critical minerals in Africa?", 
               "What are the recommendations made by the study group to address the challenges in critical mineral supply chains?",
               "How does the reliance on critical minerals imports affect U.S. national security?", 
               "What actions are suggested to strengthen US-Africa partnerships in critical minerals?", 
               "What impact does the extraction of critical minerals have on local communities in Africa?", 
               "What is the significance of forming strategic partnerships for the development of Africa's critical minerals?"] 
suggestion = st.selectbox("Or choose a suggestion", suggestions)
if st.button("Ask"):
    query = user_input or suggestion
    # Generate response
    response_completion = client.chat.completions.create(
        model="gemma-7b-it",
        messages=[
            {
                "role": "user",
                "content": query
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    response = ""
    for chunk in response_completion:
        response += chunk.choices[0].delta.content or ""
    st.write("Chatbot: ", response)