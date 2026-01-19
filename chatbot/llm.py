import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("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"))

def ask_llm(prompt):
    completion = client.chat.completions.create(
        model="llama3-70b-8192",   # or "mixtral-8x7b-32768"
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=512
    )

    return completion.choices[0].message.content
