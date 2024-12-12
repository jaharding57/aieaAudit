from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="a grizzly bear banana slug hybrid with a bearish but banana slug face but the lower body of a grizzly bear",
  size="1024x1024",
  quality="standard",
  n=1,
)

print(response.data[0].url)
