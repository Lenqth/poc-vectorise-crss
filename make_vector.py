
import json
from langchain.docstore.document import Document

from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

MODEL_NAME = "mxbai-embed-large"

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", type=str)
    
    args = parser.parse_args()
    input_path = args.input_path
    
    embedder = OllamaEmbeddings(
        model=MODEL_NAME,
    )

    with open(input_path) as f:
        obj = json.load(f)

    documents = []
    for item in obj:
        meta = {**item}
        del meta["id"]
        del meta["text"]
        documents.append( Document(item["text"], metadata=meta, id=item["id"]) )
        
        
    vectorstore = InMemoryVectorStore.from_documents(
        documents,
        embedding=embedder,
    )

    vectorstore.dump("./vectors.json")

if __name__ == "__main__":
    main()