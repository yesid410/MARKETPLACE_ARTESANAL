from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)

API_GATEWAY_URL = os.getenv("API_GATEWAY_URL", "http://api-gateway:8000")

def gw(path):
    return f"{API_GATEWAY_URL.rstrip('/')}/{path.lstrip('/')}"

@app.route("/")
def index():
    return render_template("index.html", gateway_url=API_GATEWAY_URL)

# Panel del Gateway
@app.route("/gateway")
def gateway():
    # Intenta leer /health del gateway
    try:
        r = requests.get(gw("/health"), timeout=3)
        health = r.json() if r.headers.get("content-type","").startswith("application/json") else r.text
    except Exception as e:
        health = {"error": str(e)}
    return render_template("gateway.html", gateway_url=API_GATEWAY_URL, health=health)

# Pagos UI
@app.route("/pagos")
def pagos():
    return render_template("pagos.html", gateway_url=API_GATEWAY_URL)

# Pedidos UI
@app.route("/pedidos")
def pedidos():
    return render_template("pedidos.html", gateway_url=API_GATEWAY_URL)

# Productos UI
@app.route("/productos")
def productos():
    return render_template("productos.html", gateway_url=API_GATEWAY_URL)

# Auth UI
@app.route("/auth")
def auth():
    return render_template("auth.html", gateway_url=API_GATEWAY_URL)