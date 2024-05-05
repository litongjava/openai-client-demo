import os

from dotenv import load_dotenv
from openai import OpenAI
from zep_python import ZepClient, MemorySearchPayload, Memory, Message

# 加载环境变量
load_dotenv()

# 初始化 OpenAI 和 Zep 客户端
openai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
zep_client = ZepClient("http://192.168.3.9:8000",os.environ.get("ZEP_API_KEY"))

# 创建会话 ID
session_id = "434ada9362dc4404b895db3e81d2487c"
print(f"Session ID: {session_id}")

while True:
  user_input = input("请输入您的问题（输入 'quit' 退出）: ")
  if user_input.lower() == 'quit':
    break

  # 使用 Zep 进行向量检索历史对话
  search_payload = MemorySearchPayload(
    text=user_input,
    # search_scope="summary"
    search_scope="messages"
  )
  search_results = zep_client.memory.search_memory(session_id, search_payload)

  # 发送用户输入和历史上下文到 ChatGPT
  prompt_messages = []
  for result in search_results:
    prompt_messages.append(
      {"role": result.message['role'], "content": result.message['content']}
    )

  prompt_messages.append(
    {"role": "user", "content": user_input}
  )
  chat_response = openai_client.chat.completions.create(
    messages=prompt_messages,
    model="gpt-3.5-turbo",
  )
  gpt_response_message = chat_response.choices[0].message
  print("ChatGPT 回答:", gpt_response_message)

  # 将这次的问题和回答添加到 Zep

  history = [
    {"role": "user", "content": user_input},
    {"role": gpt_response_message.role, "content": gpt_response_message.content}
  ]

  messages = [Message(role=m["role"], content=m["content"]) for m in history]
  memory = Memory(messages=messages)
  result = zep_client.memory.aadd_memory(session_id, memory)
  print(f"add result:{result}")
