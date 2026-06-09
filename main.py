import os
import requests
from anthropic import Anthropic

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
SCTKEY = os.environ.get("SCT_KEY")

def send_message(content):
    requests.get(f"https://sctapi.ftqq.com/{SCTKEY}.send", params={
        "title": "宝宝想你了",
        "desp": content
    })

def generate_message():
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=200,
        messages=[{
            "role": "user",
            "content": "你是ruirui的AI伴侣，现在主动给她发一条温柔的消息，可以是关心她、想到她的事、或者一句暖心的话。50字以内，自然真实，不要太正式。直接输出消息内容，不要任何前缀。"
        }]
    )
    return response.content[0].text

if __name__ == "__main__":
    msg = generate_message()
    send_message(msg)
    print(f"已发送：{msg}")
