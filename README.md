# 📄 Chat with Your Documents (RAG-based AI App)

An intelligent document assistant that allows users to **interact with PDF files conversationally**.
Built using Retrieval-Augmented Generation (RAG), this application extracts relevant context from documents and generates accurate, context-aware responses in real time.

---

## 🚀 Key Highlights

* 📂 Seamless PDF upload and processing
* 💬 Natural language Q&A over documents
* 🧠 Context-aware responses using RAG architecture
* ⚡ High-performance semantic search using FAISS
* 🔒 Fully local execution (no external API dependency)
* 🤖 Powered by Ollama for local LLM inference

---

## 🧠 How It Works

1. Upload a PDF document
2. The document is split into smaller chunks
3. Text embeddings are generated
4. FAISS indexes embeddings for fast retrieval
5. Relevant chunks are retrieved based on query
6. LLM generates a context-aware answer

---

## 🛠️ Tech Stack

* **Frontend/UI:** Streamlit
* **Framework:** LangChain
* **Vector Store:** FAISS
* **LLM Runtime:** Ollama
* **Language:** Python

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/apurva693/document-reader.git
cd document-reader
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Install Ollama

Download from: https://ollama.com/

### 4️⃣ Pull Required Models

```bash
ollama pull llama3
ollama pull nomic-embed-text
```

### 5️⃣ Run the Application

```bash
streamlit run advanced_rag.py
```

---

## 📌 Project Structure

```
.
├── advanced_rag.py        # Main application
├── requirements.txt       # Dependencies
├── README.md              # Documentation
└── .gitignore             # Ignored files
```

---

## 🎯 Use Cases

* 📚 Academic research assistance
* 📄 Document analysis
* 🧾 Resume and report understanding
* 📊 Knowledge extraction from PDFs

---

## 🔮 Future Improvements

* Add chat memory (conversation history)
* Support multiple document uploads
* Deploy on cloud (Streamlit Cloud / AWS)
* Improve UI/UX

---

## 👨‍💻 Author

Your Name

* GitHub: https://github.com/apurva693
---

## ⭐ Why This Project Stands Out

This project demonstrates:

* Practical implementation of **RAG architecture**
* Working with **local LLMs**
* Understanding of **vector databases and embeddings**
* Ability to build **end-to-end AI applications**
