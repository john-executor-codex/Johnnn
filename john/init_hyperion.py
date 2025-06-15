import json
import sys
from pathlib import Path

def carregar_protocolo(modulo_id=None):
    caminho = Path("knowledge/protocolo_hyperion_v1.json")
    if not caminho.exists():
        print("❌ Arquivo 'protocolo_hyperion_v1.json' não encontrado.")
        return

    with open(caminho, "r", encoding="utf-8") as f:
        protocolo = json.load(f)

    modulos = protocolo.get("conteudo", {}).get("modulos", [])

    if modulo_id is None:
        print("✅ Protocolo carregado. Nenhum módulo específico solicitado.")
        print(f"Total de módulos disponíveis: {len(modulos)}")
        return

    modulo = next((m for m in modulos if m["id"] == modulo_id), None)
    if modulo:
        print(f"🔹 Módulo {modulo_id} encontrado:")
        print(f"📘 Título: {modulo['titulo']}")
        print(f"📝 Descrição: {modulo['descricao']}")
    else:
        print(f"⚠️ Módulo {modulo_id} não encontrado no protocolo.")

if __name__ == "__main__":
    modulo = None
    if len(sys.argv) > 1:
        try:
            modulo = int(sys.argv[1])
        except ValueError:
            print("⚠️ O parâmetro fornecido não é um número inteiro válido.")
    carregar_protocolo(modulo)
