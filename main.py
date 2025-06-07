from flask import Flask, request, jsonify
from modules.generator import gerar_codigo
from modules.executor import executar_codigo

app = Flask(__name__)

@app.route("/execute", methods=["POST"])
def executar():
    data = request.get_json()
    prompt = data.get("prompt")
    codigo = gerar_codigo(prompt)
    saida, erro = executar_codigo(codigo)
    return jsonify({
        "prompt_recebido": prompt,
        "codigo_gerado": codigo,
        "saida": saida,
        "erro": erro
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
