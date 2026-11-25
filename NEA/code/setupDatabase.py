import sqlite3 # This should only be ran once when its the first time using the program

def setupDatabase():
    # Connect to the database file (creates it if it doesn't exist)
    conn = sqlite3.connect("quizApp.db")
    cursor = conn.cursor() # Cursor allows us to excecute SQL commands
             # conn is short for connect

    # Create User table - the NOT Exsits function will prevent 
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS User (
            userID INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """) # Docstring used to allow us to write a string that is multiple lines without any special breaks
    
    # No need to use varchar for storing username and password as there will be error handing methods in place so the correct data can be stored to the database


    # Create Quizzes table (only applicable to set quizzes)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Quizzes (
            quizID INTEGER PRIMARY KEY AUTOINCREMENT,
            userID INTEGER NOT NULL,
            difficulty TEXT NOT NULL,
            quizDuration TEXT NOT NULL,
            FOREIGN KEY (userID) REFERENCES User(userID)
        )
    """)

    # Create Results table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Results (
            resultID INTEGER PRIMARY KEY AUTOINCREMENT,
            userID INTEGER NOT NULL,
            quizID INTEGER NOT NULL,
            score INTEGER NOT NULL,
            timeTaken TEXT NOT NULL,
            FOREIGN KEY (userID) REFERENCES User(userID),
            FOREIGN KEY (quizID) REFERENCES Quizzes(quizID)
        )
    """)

    conn.commit() # Commits the current transaction (changes), no need to do it itertievly after every transaction, only until you close the connection or query the database
    print("Database setup complete")
    
    # Display data inside tables
    printTables(cursor)

    conn.close() # Good coding practice - closes the database connection

def printTables(cursor):
    tables = ["User", "Quizzes", "Results"]
    
    for table in tables:
        print("Contents of", table, "table:")
        cursor.execute("SELECT * FROM " + table)
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print("No data in", table, "table.")
        print("-" * 40)

# Run the setup function
setupDatabase()


