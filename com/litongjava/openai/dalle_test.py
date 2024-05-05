import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
  # This is the default and can be omitted
  api_key=os.environ.get("OPENAI_API_KEY"),
)
client = OpenAI()

prompt = ("In the top left panel, a young boy with messy hair and a big smile is playing fetch with his loyal golden retriever in a lush green park. The boy throws a bright red ball, and the dog joyfully bounds after it.\n\nIn the top right panel, the boy and his dog are sitting side by side on a cozy rug in front of a crackling fireplace. The boy is reading a book out loud, while the dog looks up at him with adoring eyes, enjoying the sound of his owner's voice.\n\nIn the bottom left panel, the boy is carefully bandaging a small cut on the dog's paw, his brow furrowed in concentration. The dog patiently sits still, looking up at the boy with trust and gratitude.\n\nIn the bottom right panel, the boy and his dog are curled up together in a makeshift tent in the backyard, gazing up at the stars through an opening in the tent. Their silhouettes are illuminated by a warm lantern, creating a heartwarming scene of companionship and love.")
response = client.images.generate(
  model="dall-e-3",
  prompt=prompt,
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

# 打印模型的回答
print(image_url)
