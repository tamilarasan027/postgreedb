import psycopg2

def list_tables():
    try:
        connection = psycopg2.connect(
            user="joosika",
            password="marriage",
            host="localhost",
            port="5432",
            database="joosika"
        )

        cursor = connection.cursor()

        # Fetch all table names in the current schema
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE'")
        tables = cursor.fetchall()

        # Print the table names
        print("Tables in the database:")
        for table in tables:
            print(table[0])

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        # Closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


# Call the function to list tables
list_tables()

