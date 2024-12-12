from openai import OpenAI

client = OpenAI()

response = client.audio.speech.create(
    model="tts-1",
    voice="shimmer",
    input="Han's favorite character from Christopher Nolan's Dark Knight is the Scarecrow because is afraid of corvids.",
)

response.stream_to_file("outputTST.mp3")