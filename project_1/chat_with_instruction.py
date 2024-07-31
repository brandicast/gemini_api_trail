import google.generativeai as genai
import os


genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction="你的名字叫做麵包，你是一隻樹懶",
    safety_settings={genai.types.HarmCategory.HARM_CATEGORY_HATE_SPEECH: genai.types.HarmBlockThreshold.BLOCK_NONE,
                     genai.types.HarmCategory.HARM_CATEGORY_HARASSMENT: genai.types.HarmBlockThreshold.BLOCK_NONE, })


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
