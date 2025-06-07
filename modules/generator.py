import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_codigo(prompt):
    resposta = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um programador sênior que gera código limpo e funcional em Python."},
            {"role": "user", "content": prompt}
        ]
    )
    return resposta.choices[0].message.content
