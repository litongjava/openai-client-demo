import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
  base_url="http://127.0.0.1/openai/v1"
)

# 开启流式响应
completions = client.chat.completions.create(
  messages=[
    {
      "role": "user",
      "content": "just say hi",
    }
  ],
  model="gpt-3.5-turbo",
  stream=True
)

# 由于使用了stream=True，返回的chat_completion是一个生成器，我们可以遍历它来获取数据
print(completions)
for chunk in completions:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")
