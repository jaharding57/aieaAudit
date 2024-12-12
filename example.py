from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {	"role": "system", 
        	"content": "You are a sarcastic but fun assistant."},
        {
            "role": "user", 
            "content": "Write a limerick about Safeway's fried chicken."
        }
    ]
)

print(completion.choices[0].message)
