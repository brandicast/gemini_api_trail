import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

while True:
    print("> ", end="")
    prompt = input()

    if prompt == 'EXIT':
        exit()

    # response = model.generate_content(prompt)
    response = chat.send_message(prompt, stream=True)

    for chunk in response:
        print(chunk.text)
        print("_" * 80)

    print("")
