from database.database import Database


class Memory:

    def __init__(self):

        self.database = Database()


    def initialize(self):

        print("[MEMORY] Database connected.")


    def search(self, query):

        words = query.split()

        results = []

        for word in words:

            if len(word) < 3:
                continue

            found = self.database.search(word)

            for result in found:

                if result not in results:
                    results.append(result)

        return results