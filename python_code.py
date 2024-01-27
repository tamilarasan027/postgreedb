import psycopg2

def insert_data():
    try:
        connection = psycopg2.connect(
            user="joosika",
            password="marriage",
            host="localhost",
            port="5432",
            database="joosika"
        )

        cursor = connection.cursor()

        # Get user input for name and mark
        name = input("Enter name: ")
        mark = int(input("Enter mark: "))

        # Insert data into the 'students' table
        postgres_insert_query = """ INSERT INTO students (name, mark) VALUES (%s,%s)"""
        record_to_insert = (name, mark)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into students table")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        # Closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


# Call the function to insert data
insert_data()

