from fastapi import FastAPI, Request
from pydantic import BaseModel
import openai
import os
from pinecone_utils import buscar_productos
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class Consulta(BaseModel):
    mensaje: str

@app.get("/")
def home():
    return {"status": "API BySaa lista 🎉"}

@app.post("/preguntar")
def preguntar(data: Consulta):
    consulta_usuario = data.mensaje
    coincidencias = buscar_productos(consulta_usuario)
    contexto = "\n".join([f"- {c['nombre']} / ${c['precio']}" for c in coincidencias])

    prompt = f'''
Eres un asesor profesional y amable de la tienda BySaa.

Contexto de productos relacionados:
{contexto}

Pregunta del cliente: "{consulta_usuario}"

Responde en máximo 3 frases. Sé concreto, amable y útil.
Si el producto existe, ofrécelo con precio. Si no, sugiere otro o pregunta más.
'''
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Responde como asesor experto de salud y productos de bienestar."},
            {"role": "user", "content": prompt}
        ]
    )
    return {"respuesta": response['choices'][0]['message']['content']}
