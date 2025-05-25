import pinecone
import os
from dotenv import load_dotenv
import openai

load_dotenv()

pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENV"))

index = pinecone.Index(os.getenv("PINECONE_INDEX"))

def get_embedding(text):
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=[text]
    )
    return response['data'][0]['embedding']

def buscar_productos(query):
    vector = get_embedding(query)
    resultado = index.query(vector=vector, top_k=5, include_metadata=True)

    productos = []
    for match in resultado['matches']:
        metadata = match['metadata']
        productos.append({
            "nombre": metadata.get("nombre"),
            "precio": metadata.get("precio"),
            "url": metadata.get("url")
        })

    return productos
