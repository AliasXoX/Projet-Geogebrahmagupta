import getpass
import os
import bs4
from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.llms import Ollama
from langchain_community.embeddings import LlamaCppEmbeddings
from torch import cuda
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from sentence_transformers import SentenceTransformer


#llm = Ollama(model="llama2")

embed_model_id = "dangvantuan/sentence-camembert-large"

device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu'

embed_model = HuggingFaceEmbeddings(
    model_name=embed_model_id,
    model_kwargs={'device': device},
    encode_kwargs={'device': device, 'batch_size': 32}
)

# Load, chunk and index the contents of the blog.
loader = TextLoader("./Liste_de_commandes.md")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
splits = text_splitter.split_documents(docs)
#print(splits)
vectorstore = Chroma.from_documents(documents=splits, embedding=embed_model)

# Retrieve and generate using the relevant snippets of the blog.
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 1})

phrase = "Dessine une droite qui va passer par les points A et ensuite par le point (0,1)"

retriever_docs = retriever.invoke(phrase)
print(retriever_docs[0])