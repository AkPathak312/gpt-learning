from PyPDF2 import PdfReader
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI

sample_pdf= open(r'D:\PythonProjects\chatgptlearning\static\pdffiles\8_Physical_Science.pdf',mode='rb')

def processPdf(queryText):
    openAiKey='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'
    os.environ["OPENAI_API_KEY"] = openAiKey
    if sample_pdf is not None:
    #  load_dotenv()
        pdf_reader= PdfReader(sample_pdf)
        text=""
        i=1
        for page in pdf_reader.pages:
            i=i+1
            text+=page.extract_text()
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap = 200,
                length_function = len
            )
            if(i%10==0):
                print('Reading pages...')

        chunks  = text_splitter.split_text(text=text)

        embeddings = OpenAIEmbeddings()
        VectorStore = FAISS.from_texts(chunks, embedding=embeddings)

        query=queryText
        if query:
            docs= VectorStore.similarity_search(query=query, k=5)
            llm= ChatOpenAI(model_name='gpt-3.5-turbo')
            chain =  load_qa_chain(llm=llm, chain_type='stuff')
            response = chain.run(input_documents = docs, question = query)
            return response
        sample_pdf.close()






