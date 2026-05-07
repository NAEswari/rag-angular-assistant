from langchain_community.vectorstores import FAISS
# from langchain.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

VECTOR_PATH = "vectorstore"

class RAGEngine:
    def __init__(self):
        # self.embeddings = OpenAIEmbeddings()
        self.embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
)
        # self.db = FAISS.load_local(VECTOR_PATH, self.embeddings)
        self.db = FAISS.load_local(
            VECTOR_PATH,
            self.embeddings,
            allow_dangerous_deserialization=True
)
        self.llm = Ollama(model="llama3")

    def retrieve(self, query, k=5):
        return self.db.similarity_search(query, k=k)

    def generate(self, query, docs):
        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
        You are an Angular expert assistant.

        STRICT RULES:
        - Answer ONLY using the provided context
        - Do NOT use prior knowledge
        - If answer is not in context, say "I don't know"
        - Keep answer concise (max 5 lines)

        Context:
        {context}

        Question:
        {query}

        Answer:
        """
   

        # return self.llm.predict(prompt)
        return self.llm.invoke(prompt)

    def ask(self, query):
        docs = self.retrieve(query)
        answer = self.generate(query, docs)
        return answer, docs