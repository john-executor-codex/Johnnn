import openai
import os

def gerar_codigo(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um programador sênior que gera código limpo e funcional em Python."},
            {"role": "user", "content": prompt}
        ]
    )
    return resposta['choices'][0]['message']['content']
