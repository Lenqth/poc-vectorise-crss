
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings

MODEL_NAME = "mxbai-embed-large"

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str)
    
    args = parser.parse_args()
    
    text = args.text

    embedder = OllamaEmbeddings(
        model=MODEL_NAME,
    )

    vectorstore = InMemoryVectorStore.load(
        "./vectors.json",
        embedding=embedder
    )
    
    result = vectorstore.similarity_search_with_score(text)
    result = [ {**item.model_dump(), "similarity": sim} for item, sim in result]
    
    print(
        result
    )

if __name__ == "__main__":
    main()