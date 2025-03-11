# This python file will help to store vector to Pinecone Vector DataBase



from src.helper import load_pdf, text_split, HuggingFaceEmbeddings
import pinecone
from langchain_community.vectorstores import Pinecone  
from dotenv import load_dotenv
import os

# Load API keys from .env
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_API_ENV = os.getenv("PINECONE_API_ENV")

# Initialize Pinecone
pc = pinecone.Pinecone(api_key=PINECONE_API_KEY)

# Define index name
index_name = "medicalchatbot"


# Load and process data
extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)

# Create embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Store text embeddings in Pinecone
from langchain_pinecone import PineconeVectorStore
vectorstore_from_docs = PineconeVectorStore.from_documents(
    text_chunks,
    index_name=index_name,
    embedding=embeddings
)


