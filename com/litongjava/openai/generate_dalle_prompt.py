import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # 这将加载.env文件中的所有环境变量

client = OpenAI(
  # This is the default and can be omitted
  api_key=os.environ.get("OPENAI_API_KEY"),
  base_url="http://127.0.0.1/openai/v1"
)

chat_completion = client.chat.completions.create(
  messages=[
    {
      "role": "system",
      "content": "Just say hi",
    },
    {
      "role": "user",
      "content": "create a story about a boy with dog",
    }
  ],
  model="gpt-3.5-turbo",
  # stream=True
  # model="gpt-4-0125-preview",
  # model="gpt-4-turbo-preview"

)

# 打印模型的回答
print(chat_completion.choices[0].message)
