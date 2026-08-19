import sqlite3


class KnowledgeBase:

    def __init__(
        self,
        database="data/knowledge.db"
    ):

        self.connection = sqlite3.connect(
            database
        )

        self.create_table()
        self.insert_data()


    def create_table(self):

        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS facts (
                entity TEXT,
                relation TEXT,
                value TEXT,
                UNIQUE(entity, relation, value)
            )
        """)

        self.connection.commit()


    def insert_data(self):

        cursor = self.connection.cursor()

        facts = [

            ("India", "capital", "New Delhi"),
            ("France", "capital", "Paris"),
            ("Japan", "capital", "Tokyo"),
            ("Australia", "capital", "Canberra"),

            ("India", "continent", "Asia"),
            ("France", "continent", "Europe"),
            ("Japan", "continent", "Asia"),
            ("Australia", "continent", "Australia"),

            ("Einstein", "occupation", "Physicist"),
            ("Newton", "occupation", "Physicist"),
            ("Marie Curie", "occupation", "Chemist")

        ]

        cursor.executemany(
            """
            INSERT OR IGNORE INTO facts
            (entity, relation, value)
            VALUES (?, ?, ?)
            """,
            facts
        )

        self.connection.commit()


    def query(
        self,
        entity,
        relation
    ):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT value
            FROM facts
            WHERE entity = ?
            AND relation = ?
            """,
            (
                entity,
                relation
            )
        )

        result = cursor.fetchone()

        if result:
            return result[0]

        return None


if __name__ == "__main__":

    kb = KnowledgeBase()

    print(
        "India capital:",
        kb.query("India", "capital")
    )

    print(
        "Japan capital:",
        kb.query("Japan", "capital")
    )