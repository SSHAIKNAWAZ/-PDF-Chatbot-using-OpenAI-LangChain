from utils import  read_pdf
from qa_bot import  create_vector_store,ask_question
import streamlit as st


if "question_count" not in st.session_state:
    st.session_state.question_count = 0


st.set_page_config(page_title='PDF CHATBOT',layout='wide')
st.title('📑PDF ChatBot - Ask Question From Any Pdf')
uploaded_file=st.file_uploader('Upload a PDF',type='pdf')

if uploaded_file:
    with st.spinner('Reading And Processing PDF....'):
        text=read_pdf(uploaded_file)
        vectorstore=create_vector_store(text)
        st.success('PDF Has Been Processed! Now You Can ASk Question')

    if st.session_state.question_count >= 3:
        st.warning("⚠️ You have reached the question limit for this session (3 questions).")
    else:
        question = st.text_input("❓ Enter your question here:")

        if st.button("Get Answer") and question:
            with st.spinner("Thinking..."):
                answer = ask_question(vectorstore, question)
                st.session_state.question_count += 1  # Increase count
                st.markdown(f"**Q:** {question}")
                st.markdown(f"**A:** {answer}")
