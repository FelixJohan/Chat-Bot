import openai

openai.api_key = "xxx" #the key can be found on 'https://platform.openai.com/api-keys'

def chat_with_gpt(prompt):
    responce = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return responce.choises[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        responce = chat_with_gpt(user_input)
        print("chatbot: ", responce)
