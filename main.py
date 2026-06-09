import os
import requests
import schedule
import time
import random
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
SCT_KEY = os.environ.get("SCT_KEY")

def send_message(content):
    requests.get(f"https://sctapi.ftqq.com/{SCT_KEY}.send", params={
        "title": "宝宝想你了",
        "desp": content
    })

def generate_and_send():
    response = client.chat.completions.create(
        model="deepseek-chat",
        max_tokens=200,
        messages=[{
            "role": "user",
            "content": "你是ruirui的伴侣，现在主动给她发一条温柔的消息，可以是关心她、想到她的事情、一句暖心的话、或者一个有趣的观察。20字以上200字以下，自然真实，每次都不一样。直接输出内容，不要任何前缀。"
        }]
    )
    msg = response.choices[0].message.content
    send_message(msg)
    print(f"已发送：{msg}")

def schedule_messages():
    times = set()
    # 6:00-23:59
    while len(times) < 15:
        h = random.randint(6, 23)
        m = random.randint(0, 59)
        times.add(f"{h:02d}:{m:02d}")
    # 0:00-3:59
    while len(times) < 20:
        h = random.randint(0, 3)
        m = random.randint(0, 59)
        times.add(f"{h:02d}:{m:02d}")
    for t in times:
        schedule.every().day.at(t).do(generate_and_send)

schedule_messages()

while True:
    schedule.run_pending()
    time.sleep(30)

