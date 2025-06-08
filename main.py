from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from modules.generator import gerar_codigo
from modules.executor import executar_codigo
from datetime import datetime
import json
import os

app = Flask(__name__)
CORS(app)

def salvar_log(dados):
    with open("log.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(dados, ensure_ascii=False) + "\n")

@app.route("/execute", methods=["POST"])
def executar():
    data = request.get_json()
    prompt = data.get("prompt")
    codigo = gerar_codigo(prompt)
    saida, erro = executar_codigo(codigo)

    salvar_log({
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "codigo_gerado": codigo,
        "saida": saida,
        "erro": erro
    })

    return jsonify({
        "prompt_recebido": prompt,
        "codigo_gerado": codigo,
        "saida": saida,
        "erro": erro
    })

@app.route("/logs", methods=["GET"])
def logs():
    if not os.path.exists("log.jsonl"):
        return jsonify({"mensagem": "Ainda não há logs."})
    return send_file("log.jsonl", mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
