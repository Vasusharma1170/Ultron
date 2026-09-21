from core.memory import Memory
from core.reasoning import Reasoning
from core.learning import Learning


class OmniAI:

    def __init__(self):

        self.name = "Omni-AI"

        self.memory = Memory()
        self.reasoning = Reasoning()
        self.learning = Learning()

        self.running = False


    def boot(self):

        print("[BOOT] Starting Omni-AI...")

        self.memory.initialize()
        self.reasoning.initialize()
        self.learning.initialize()

        self.running = True

        print("[BOOT] Memory: ONLINE")
        print("[BOOT] Reasoning: ONLINE")
        print("[BOOT] Learning: ONLINE")
        print("[BOOT] Omni-AI is ready.")


    def process(self, user_input):

        information = self.memory.search(user_input)

        response = self.reasoning.think(
            user_input,
            information
        )

        return response


    def shutdown(self):

        print("[SYSTEM] Saving state...")

        self.learning.save()

        self.running = False

        print("[SYSTEM] Omni-AI shutdown.")