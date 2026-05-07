from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
# from langchain.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

DATA_PATH = "data/angular_docs.txt"
VECTOR_PATH = "vectorstore"

def ingest():
    print("📥 Loading documents...")
    loader = TextLoader(DATA_PATH)
    documents = loader.load()

    print("✂️ Splitting into chunks...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    docs = splitter.split_documents(documents)

    print(f"📊 Total chunks: {len(docs)}")

    print("🧠 Creating embeddings...")
    # embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

    print("💾 Storing in FAISS...")
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(VECTOR_PATH)

    print("✅ Ingestion complete!")

if __name__ == "__main__":
    ingest()