from src import add
from src import Agent
from src import SYSTEM_PROMPT
import time

import os 
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Hello from my-project-str!")

    password = os.getenv("password")
    print(f"user passsword is: {password[0:3]}*******")

    openai_api_key = os.getenv("OPENAI_API_KEY")
    print(f"OPENAI_API_KEY is: {openai_api_key[0:7]}**************")

    start = time.perf_counter()

    agent = Agent("Doctor")
    print(f"My agent name is {agent.name}")

    number_1 = 7
    number_2 = 7

    result = add(number_1,number_2)
    print(f"The result of {number_1} + {number_2} is {result}")

    elapsed = time.perf_counter() - start
    print(f"Time taken  to created agent: {elapsed} seconds")

    print(f"My agent {agent.name} system prompt is \n {SYSTEM_PROMPT}")


if __name__ == "__main__":
    main()
