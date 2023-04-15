import os
import openai
openai.api_key = "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"

#감정분석 요소
while True:
    user_content = "다음 글에서 감정을 positive 또는 neutral 또는 negative 분류하세요, 결과값은 positive 또는 neutral 또는 negative만 나타나게 하세요" + input("users : ")
    messages.append({"role": "user", "content": f"{user_content}"})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    assistant_content = completion.choices[0].message["content"].strip()

    messages.append({"role":"assistant", "content": f"{assistant_content}"})

    print(f"gpt : {assistant_content}") # 챗gpt api를 이용한 챗봇 구현
