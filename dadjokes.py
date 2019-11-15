import requests
from pyfiglet import figlet_format
from termcolor import colored
from random import choice

# Functions:
def title(message):
    header = figlet_format(message)
    header = colored(header, color="blue")
    print(header)

title("Dad Jokes Pro!")

topic = input("Let me tell you a joke! Give me a topic: ")
url = "https://icanhazdadjoke.com/search"

res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term":topic}
).json()

num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about {topic}! Here's one of them:")
    print(choice(results)['joke'])
elif num_jokes == 1:
    print(f"I found {num_jokes} joke about {topic}! Here it is: ")
    print(results[0]['joke'])
else:
    print(f"There are no jokes about {topic}!")


