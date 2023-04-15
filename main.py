import os
import openai
openai.api_key = "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"


messages = []
#system_content = input("상담신청 : ")
#messages.append("role" : "system", "content" :f"{system_content}")

while True:
    user_content = input("users : ")
    messages.append({"role": "user", "content": f"{user_content}"})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    assistant_content = completion.choices[0].message["content"].strip()

    messages.append({"role":"assistant", "content": f"{assistant_content}"})

    print(f"gpt : {assistant_content}") # 챗gpt api를 이용한 챗봇 구현



