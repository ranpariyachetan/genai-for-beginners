import openai

openai.api_key = open('OpenAI_API_Key.txt', 'r').read().strip()

MODEL ='gpt-3.5-turbo'

# Prompt for Recipes
filter = input("Filter (For example, vegetarian, vegan or gluten-free: ")
no_recipes = input("Number of recipes (for example, 5:")
ingredients = input("List of ingredients (For example chicken, potatoes, and carrots: ")
prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipt, list all the ingredients used, no {filter}."

# prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
messages = [{'role':'user', 'content': prompt}]

completion = openai.chat.completions.create(
    messages=messages,
    model=MODEL
)

prompt_result = completion.choices[0].message.content

prompt = "Produces a shopping list for the generated recipes and please don't include ingredients that I already have."

new_prompt = f"{prompt_result} {prompt}"

messages = [{"role":"user", "content": new_prompt}]

completion = openai.chat.completions.create(
    model=MODEL,
    messages=messages
)

print("Shopping List:")
print(completion.choices[0].message.content)