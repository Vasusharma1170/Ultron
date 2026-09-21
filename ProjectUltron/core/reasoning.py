class Reasoning:

    def initialize(self):

        print("[REASONING] Reasoning engine initialized.")


    def think(self, question, information):

        if not information:

            return "I do not have information about this in my current knowledge base."


        response = "I found the following information:\n\n"

        for topic, data in information:

            response += f"{topic}: {data}\n"

        return response