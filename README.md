📄 PDF Chatbot using OpenAI &amp; LangChain An AI-powered PDF Question-Answering Chatbot built with LangChain, OpenAI GPT-3.5, and Streamlit. Just upload any PDF document, ask up to 3 questions, and get instant answers based on the file’s content. Efficient chunking and embedding techniques ensure accurate context-aware responses.

`Note Download the File add your api key to .env file then you can run it`

# 🤖 PDF Chatbot using LangChain, OpenAI, and Streamlit

This is a simple yet powerful **PDF-based Question-Answering Chatbot** built using:

- **LangChain** for document parsing and vector search
- **OpenAI's GPT** model for question answering
- **FAISS** for vector storage and similarity search
- **Streamlit** for building a clean web interface

---

## 🚀 Features

- Upload any PDF document
- Ask questions about the content of the PDF
- Get intelligent answers powered by OpenAI's LLM
- Limited to **3 questions per session** to control API usage
- Chunk size optimized to reduce token consumption
- Ready for deployment on **Hugging Face Spaces**

---

## 🧠 Tech Stack

| Layer             | Technology         |
|------------------|--------------------|
| Language Model    | OpenAI GPT-3.5     |
| Vector Store      | FAISS (via LangChain) |
| Backend Logic     | Python + LangChain |
| Frontend UI       | Streamlit          |
| File Processing   | PyPDF2             |

---

## 📂 Project Structure
- pdf_chatbot/
  - ├── app.py # Streamlit web app
  - ├── qa_bot.py # Core QA logic and LangChain pipeline
  - ├── utils.py # PDF reading helper
  - ├── requirements.txt # All dependencies
  - └── .env (optional) # Your OpenAI API Key
 
## Install Dependencies
- pip install -r requirements.txt

## Run App Locally
- streamlit run app.py


## 🧑‍💻 Author
 - Shaik Nawaz
