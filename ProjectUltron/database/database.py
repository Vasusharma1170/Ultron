import sqlite3


class Database:

    def __init__(self):

        self.connection = sqlite3.connect(
            "database/knowledge.db"
        )

        self.cursor = self.connection.cursor()

        self.create_table()


    def create_table(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS knowledge (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT,
                information TEXT
            )
        """)

        self.connection.commit()


    def add(self, topic, information):

        self.cursor.execute(
            """
            INSERT INTO knowledge (topic, information)
            VALUES (?, ?)
            """,
            (topic, information)
        )

        self.connection.commit()


    def search(self, keyword):

        self.cursor.execute(
            """
            SELECT topic, information
            FROM knowledge
            WHERE topic LIKE ?
            OR information LIKE ?
            """,
            (
                "%" + keyword + "%",
                "%" + keyword + "%"
            )
        )

        return self.cursor.fetchall()