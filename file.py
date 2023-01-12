import openai 

openai.api_key = "####################"

prompt = input("How can I help?: ")
while prompt != 'q':
    completions = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024)
    message = completions.choices[0].text
    print(message)
    prompt = input("How can I help?: ")
