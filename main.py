from src import add
from src import Agent
from src import SYSTEM_PROMPT

def main():
    print("Hello from my-project-str!")

    agent = Agent("Doctor")
    print(f"My agent name is {agent.name}")

    number_1 = 7
    number_2 = 7

    result = add(number_1,number_2)
    print(f"The result of {number_1} + {number_2} is {result}")

    print(f"My agent {agent.name} system prompt is \n {SYSTEM_PROMPT}")


if __name__ == "__main__":
    main()
