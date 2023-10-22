from flask import Flask, render_template, request, jsonify
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    try:
        # Get the question from the frontend
        query = request.json.get('question')

        # Perform similarity search and question answering
        docs = docsearch.similarity_search(query)
        answer = chain.run(input_documents=docs, question=query)
        # translator = Translator()
        # answer = translator.translate(answer, src='fr', dest='en')


        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500




loader = UnstructuredPDFLoader("fr_en_ro_final.pdf")
data = loader.load()
print (f'You have {len(data)} document(s) in your data')
print (f'There are {len(data[0].page_content)} characters in your document')

text_splitter = RecursiveCharacterTextSplitter(
  chunk_size=800, chunk_overlap=0)
texts = text_splitter.split_documents(data)

print (f'Now you have {len(texts)} documents')

embeddings = OpenAIEmbeddings(openai_api_key="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")

pinecone.init(
    api_key="39c7ae80-bf2d-48fa-b2a5-02c2dde48086",  # find at app.pinecone.io
    environment="gcp-starter" # next to api key in console
)
index_name = "openaivector"
# namespace = "book"

docsearch = Pinecone.from_texts(
  [t.page_content for t in texts], embeddings,
  index_name=index_name)

llm = OpenAI(temperature=0, openai_api_key="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")
chain = load_qa_chain(llm, chain_type="stuff")


if __name__ == '__main__':
    app.run(debug=True)

# query = input()
# docs = docsearch.similarity_search(query)
# print(chain.run(input_documents=docs, question=query))


