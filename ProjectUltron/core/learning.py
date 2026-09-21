from database.database import Database


class Learning:

    def __init__(self):

        self.database = Database()


    def initialize(self):

        print("[LEARNING] Learning system initialized.")


    def learn(self, topic, information):

        self.database.add(
            topic,
            information
        )

        print("[LEARNING] New information stored.")


    def save(self):

        print("[LEARNING] Knowledge state saved.")