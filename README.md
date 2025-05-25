# 🧠 BySaa ChatBot Backend (FastAPI + GPT + Pinecone)

Este proyecto es un backend inteligente para responder preguntas de usuarios usando OpenAI y búsqueda semántica con Pinecone.

## 🚀 Cómo desplegarlo

1. Sube este proyecto a tu cuenta de GitHub.
2. Crea un nuevo Web Service en [Render.com](https://render.com):
   - Runtime: Python
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn main:app --host 0.0.0.0 --port 10000`
   - Port: `10000`

3. En Render, agrega tus variables de entorno (`Environment`):
   - `OPENAI_API_KEY`
   - `PINECONE_API_KEY`
   - `PINECONE_ENV`
   - `PINECONE_INDEX`

4. Listo ✅ Tu API quedará accesible en `https://tuservicio.onrender.com`

## 🧪 Prueba básica

- Visita `/` para ver si está viva
- Envía POST a `/preguntar` con JSON:
```json
{
  "mensaje": "¿Tienen ecografías?"
}
```

Y recibirás una respuesta natural y profesional del asistente BySaa.
