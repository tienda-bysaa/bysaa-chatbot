import os
import openai
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index(os.getenv("PINECONE_INDEX"))

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
