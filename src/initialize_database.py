from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists calculations;
    ''')

    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table calculations (
            ID PRIMERY KEY,
            calculation TEXT,
            timestamp DATE
        );
    ''')

    connection.commit()


def initialize_database():
    print("start")
    connection = get_database_connection()

    drop_tables(connection)
    print("DROP TABLE toimii ")
    create_tables(connection)
    print("CREATE TABLE toimii")


if __name__ == "__main__":
    initialize_database()
