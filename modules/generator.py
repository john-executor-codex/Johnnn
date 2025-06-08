import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_codigo(prompt):
    resposta = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um gerador de código. Retorne apenas o código limpo em Python, sem explicações."},
            {"role": "user", "content": prompt}
        ]
    )
    return resposta.choices[0].message.content.strip()
