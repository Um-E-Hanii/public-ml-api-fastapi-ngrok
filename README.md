# Public ML API Deployment using FastAPI and Ngrok

This project demonstrates how to deploy a Machine Learning model as a public API using FastAPI and Ngrok in Google Colab.

The trained ML model is loaded using Pickle and exposed through FastAPI endpoints. Ngrok is used to generate a temporary public URL so the API can be accessed from anywhere.

---

# Features

- Machine Learning model deployment
- FastAPI backend API
- Public API exposure using Ngrok
- Google Colab deployment
- Swagger UI API testing
- JSON request handling
- Real-time prediction endpoint

---

# Technologies Used

- Python
- FastAPI
- Uvicorn
- Scikit-learn
- Pandas
- NumPy
- Pickle
- Ngrok
- Google Colab

# Installation

Install required libraries:

pip install fastapi uvicorn pyngrok nest-asyncio
Running the Project
# 1. Import libraries
from pyngrok import ngrok
import nest_asyncio
import uvicorn
# 2. Apply event loop fix
nest_asyncio.apply()
# 3. Set Ngrok token
ngrok.set_auth_token("YOUR_NGROK_TOKEN")
# 4. Create public tunnel
ngrok_tunnel = ngrok.connect(8000)
print(ngrok_tunnel.public_url)
# 5. Run FastAPI server
config = uvicorn.Config(app, host="0.0.0.0", port=8000)
server = uvicorn.Server(config)

await server.serve()
# API Documentation

# After deployment, open:

PUBLIC_URL/docs

# Example:

https://abcd1234.ngrok-free.app/docs

# Important Note

# Ngrok public URLs are temporary and may change after restarting the session.
