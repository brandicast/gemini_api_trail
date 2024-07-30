import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

while True:
    print("> ", end="")
    prompt = input()

    if prompt == 'EXIT':
        exit()

    response = model.generate_content(prompt)

    for chunk in response:
        print(chunk.text)
        print("_" * 80)

    print("")
