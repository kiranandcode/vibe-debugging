import requests
import os

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")  # Put your key in env

def ask_llm(prompt):
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        }
        data = {
            "model": "mistralai/mistral-7b-instruct",  # or openchat/openchat-7b
            "messages": [
                {"role": "system", "content": "You're a helpful assistant helping a developer debug a C/C++ program via LLDB. The user may ask you to run lldb commands, in which case, you can send commands directly to lldb by prefixing them with `!lldb` (the response should contain no other text in this case.)"},
                {"role": "user", "content": prompt}
            ]
        }
        res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        res.raise_for_status()
        return res.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[LLM error] {str(e)}"
