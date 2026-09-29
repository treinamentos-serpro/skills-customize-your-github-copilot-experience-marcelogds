import sqlite3


def connect_db(db_name="tasks.db"):
    connection = sqlite3.connect(db_name)
    connection.row_factory = sqlite3.Row
    return connection


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
        """
    )
    connection.commit()


# TODO: Add a function to insert a new task
# TODO: Add a function to list all tasks
# TODO: Add a function to update a task as completed
# TODO: Add a function to delete a task
# TODO: Build a menu loop for the app


def main():
    connection = connect_db()
    create_table(connection)
    print("To-Do App")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task complete")
    print("4. Delete task")
    print("5. Exit")
    connection.close()


if __name__ == "__main__":
    main()
