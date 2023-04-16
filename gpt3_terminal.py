import openai
import sys
import colorama

from colorama import Fore, Style
colorama.init()

openai.api_key = "YOUR API KEY"

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()

while True:
    prompt = input(Fore.GREEN + "Enter a request: " + Style.RESET_ALL)
    if prompt == "exit":
        sys.exit(0)

    generated_text = generate_text(prompt)
    print(Fore.BLUE + "Ai:" + Style.RESET_ALL)
    print(generated_text)
