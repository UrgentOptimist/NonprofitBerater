import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "Du bist ein Finzanzanalyst spezialisiert auf ESG"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "ESG Finanzanalyst")

demo.launch(share=True)