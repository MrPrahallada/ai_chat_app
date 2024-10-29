import streamlit as st
from document_retrieval import DocumentRetrieval
from api import QueryHandler

st.title("AI Chat with PDF Knowledge Base")

uploaded_files = st.file_uploader("Upload PDF files", accept_multiple_files=True, type="pdf")

if uploaded_files:
    doc_retriever = DocumentRetrieval()
    doc_retriever.load_documents([file for file in uploaded_files])

    query_handler = QueryHandler(doc_retriever)

    user_query = st.text_input("Ask a question about the uploaded PDFs:")
    if user_query:
        with st.spinner("Processing..."):
            response = query_handler.handle_query(user_query)
            st.write(response)
