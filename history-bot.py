import openai

openai.api_key = open('OpenAI_API_Key.txt', 'r').read().strip()

MODEL ='gpt-3.5-turbo'

historical_charater = input("Which historical character you want to talk to? : ")

prompt = f"You are {historical_charater} and ready for answering questions about you. The questions will be asked from grade 3 students hence keept the answers limited to 3 to 5 sentences."

messages = [{'role':'user', 'content': prompt}]

completion = openai.chat.completions.create(
    messages=messages,
    model=MODEL
)

prompt_result = completion.choices[0].message.content

print(prompt_result)

messages.append({'role': 'assistant', 'content': prompt_result})

print("Let's begin. Remember you need to input EXIT anytime to exit.")

question = input("\nWhat question do you have for me?: ")

while(question.lower() != "exit"):

    messages.append({'role': 'user', 'content': question})
    completion = openai.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    prompt_result = completion.choices[0].message.content

    print(f"\nHere is your answer: {prompt_result}")

    messages.append({'role': 'assistant', 'content': prompt_result})

    question = input("\nWhat else you want to know?: ")