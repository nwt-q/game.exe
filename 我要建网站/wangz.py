import requests
import json

url = "https://api.openai-hk.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer hk-hk-6qvq2s1000005424c7176184c8f3c8c9d574402dbfba31b1"
}

data = {
    "max_tokens": 1200,
    "model": "gpt-3.5-turbo",
    "temperature": 0.8,
    "top_p": 1,
    "presence_penalty": 1,
    "messages": [
        {
            "role": "system",
            "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible."
        },
        {
            "role": "user",
            "content": "你是chatGPT多少？"
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data).encode('utf-8') )
result = response.content.decode("utf-8")

print(result)