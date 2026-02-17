from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS
from transformers import pipeline

print("Loading data...")

# Load data
loader = TextLoader("sample.txt")
documents = loader.load()

# Chunking
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
chunks = text_splitter.split_documents(documents)

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Vector store
vectorstore = FAISS.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever()

# Generator
generator = pipeline("text-generation", model="gpt2")

print("RAG system ready!")

# Query loop
while True:
    query = input("\nAsk a question (type 'exit' to quit): ")
    if query.lower() == "exit":
        break

    docs = retriever.invoke(query)

    context = docs[0].page_content

    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
    result = generator(prompt, max_length=100)

    print("\nAnswer:")
    print(result[0]['generated_text'])
