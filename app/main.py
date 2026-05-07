from app.rag import RAGEngine

def run():
    rag = RAGEngine()

    print("🤖 Angular AI Assistant (RAG + LLaMA3)")
    print("Type 'exit' to quit\n")

    while True:
        query = input("You: ")

        if query.lower() == "exit":
            print("👋 Exiting...")
            break

        answer, docs = rag.ask(query)

        print("\n🤖 Answer:")
        print(answer)

        print("\n📚 Sources (retrieved chunks):")
        for i, doc in enumerate(docs):
            print(f"{i+1}. {doc.page_content.strip()}")
            print("\n" + "-"*50)


if __name__ == "__main__":
    run()