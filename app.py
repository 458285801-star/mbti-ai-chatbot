from openai import OpenAI
from mbti_prompts import mbti_prompts

client = OpenAI()

def mbti_chat(mbti, question):
    personality = mbti_prompts.get(mbti.upper(), "")

    prompt = f"""
你的人格类型是 {mbti}

人格特点：
{personality}

请用这种人格的说话方式回答问题。

用户问题：
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

if __name__ == "__main__":

    mbti = input("输入MBTI类型: ")
    question = input("输入问题: ")

    reply = mbti_chat(mbti, question)

    print("\nAI回答:")
    print(reply)
