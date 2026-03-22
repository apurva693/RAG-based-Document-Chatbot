import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import tempfile
import os

st.set_page_config(page_title="Chat with Your Documents", layout="wide")

# ---------- SIDEBAR ----------
st.sidebar.title("📂 Upload PDF")
uploaded_file = st.sidebar.file_uploader("Upload a PDF", type=["pdf"])

# ---------- EMBEDDINGS + LLM ----------
embeddings = OllamaEmbeddings(model="nomic-embed-text")
llm = ChatOllama(model="llama3")

# ---------- SESSION STATE ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "db" not in st.session_state:
    st.session_state.db = None

# ---------- PROCESS PDF ----------
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    loader = PyPDFLoader(tmp_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(docs)

    db = FAISS.from_documents(chunks, embeddings)
    st.session_state.db = db

    os.remove(tmp_path)
    st.sidebar.success("✅ PDF processed successfully!")

# ---------- MAIN UI ----------
st.title("💬 Chat with Your Documents")

# Display previous chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
query = st.chat_input("Ask a question about your PDF...")

if query:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # Ensure DB exists
    if st.session_state.db is None:
        answer = "⚠️ Please upload a PDF first."
    else:
        retriever = st.session_state.db.as_retriever(search_kwargs={"k": 3})
        docs = retriever.invoke(query)
        context = "\n\n".join([d.page_content for d in docs])

        prompt = ChatPromptTemplate.from_template(
            """
You are a helpful assistant.
Answer ONLY from the provided context.
If the answer is not in context, say "I don't know".

Context:
{context}

Question:
{question}
"""
        )

        chain = prompt | llm | StrOutputParser()
        answer = chain.invoke({"context": context, "question": query})

    # Show assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
