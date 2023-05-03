import openai
openai.api_key = open("api.cred", 'r').read()

messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]

while True:
    message = input("User : ")
    
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
      
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    print("\n\n")
    
    if message == "exit":
        break
    
    messages.append({"role": "assistant", "content":reply})
