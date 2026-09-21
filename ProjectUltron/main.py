from core.agent import OmniAI

def main():

    print("=" * 50)
    print("           OMNI-AI SYSTEM")
    print("=" * 50)

    ai = OmniAI()

    ai.boot()

    while True:

        user_input = input("\nYou: ")

        if user_input.lower() == "shutdown":
            ai.shutdown()
            break

        response = ai.process(user_input)

        print("Omni-AI:", response)


if __name__ == "__main__":
    main()