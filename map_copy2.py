from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

loader = UnstructuredPDFLoader("all_merged.pdf")
data = loader.load()
print (f'You have {len(data)} document(s) in your data')
print (f'There are {len(data[0].page_content)} characters in your document')

text_splitter = RecursiveCharacterTextSplitter(
  chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(data)

print (f'Now you have {len(texts)} documents')

embeddings = OpenAIEmbeddings(openai_api_key="")

pinecone.init(
    api_key="",  # find at app.pinecone.io
    environment="gcp-starter" # next to api key in console
)
index_name = "openaivector"
# namespace = "book"

docsearch = Pinecone.from_texts(
  [t.page_content for t in texts], embeddings,
  index_name=index_name)

llm = OpenAI(temperature=0, openai_api_key="")
chain = load_qa_chain(llm, chain_type="stuff")

query = "Cat costa biletul in spaniola?"
docs = docsearch.similarity_search(query)

print(chain.run(input_documents=docs, question=query))

query = "Cat costa biletul?"
docs = docsearch.similarity_search(query)

print(chain.run(input_documents=docs, question=query))

query = "Cat costa biletul in spaniola?"
docs = docsearch.similarity_search(query)

print(chain.run(input_documents=docs, question=query))