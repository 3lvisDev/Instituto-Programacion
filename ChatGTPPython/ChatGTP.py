import openai

openai.api_key = "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"

while True:
      
    prompt = input("\nIntroduce una pregunta: ")

    if prompt == "exit":
        break

    completion = openai.Completion.create(engine="text-davinci-003",
                                          prompt="prompt",
                                          max_tokens=2048)

                          
    print(completion.choices[0].text)
