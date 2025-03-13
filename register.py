from connection import Connection, sqlite3


class Register(Connection):
    def __init__(self) -> None:
        super().__init__()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS disorders(
            name varchar(50) NOT NULL,
            description TEXT NOT NULL,
            source TEXT NOT NULL
        );""")

    def create_disorder(self, name: str, description: str, source: str):
        lower_name = name.lower()
        self.cursor.execute(
            "INSERT INTO disorders(name, description, source) VALUES(? , ? , ?)",
            [lower_name, description, source],
        )

        self.commit()

    def search_by_name(self, name: str):
        lower_name = name.lower()

        res = self.cursor.execute(f"SELECT * FROM disorders WHERE name='{name}'")
        disorder = res.fetchone()

        return disorder

    def show_disorders(self):
        res = self.cursor.execute("SELECT * FROM disorders")
        disorders = res.fetchall()

        print(disorders)


if __name__ == "__main__":
    register = Register()
    register.show_disorders()
    name = input("Escribe el nombre del transtorno: ")

    disorder = register.search_by_name(name)
    print(disorder)
