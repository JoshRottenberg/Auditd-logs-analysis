import sqlite3


def create_db():
    # Connect to db
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()

    # Define schema
    table_schema = """
    CREATE TABLE IF NOT EXISTS auditd_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        command TEXT,
        user TEXT,
        folder TEXT,
        time TEXT   
    );
    
    CREATE TABLE IF NOT EXISTS meta_data (
        run id INTEGER KEY AUTO INCREMENT,
        log TEXT,
        run_time TEXT
    )
                                        
    """
    # create table
    cursor.execute(table_schema)
    connection.commit()
    connection.close()


def update_db(cmd, user_name, folder_path, time_stamp):
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    # Insert data into the auditd_info table
    cursor.execute("""
    INSERT INTO auditd_info (command_rule, user, folder, time)
    VALUES (?, ?, ?, ?)""",
    (cmd, user_name, folder_path, time_stamp))

    conn.commit()
    conn.close()


create_db()
update_db("command", "usname", "path/to/folder", 123455)