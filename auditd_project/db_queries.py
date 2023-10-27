import sqlite3

# TODO: complete unwritten queries


def num_of_commands():
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()
    query = "SELECT COUNT(DISTINCT command) FROM auditd_info"
    cursor.execute(query)
    output = cursor.fetchall()
    return output[0]


def frequent_command():
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()
    query = "SELECT"
    cursor.execute(query)
    output = cursor.fetchall()
    return output[0]


def frequent_user():
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()
    query = "SELECT"
    cursor.execute(query)
    output = cursor.fetchall()
    return output[0]


def least_common_cmd():
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()
    query = "SELECT"
    cursor.execute(query)
    output = cursor.fetchall()
    return output[0]


def act_folder_path():
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()
    query = "SELECT"
    cursor.execute(query)
    output = cursor.fetchall()
    return output[0]


def num_of_entries():
    # assumption: no lines were deleted from table
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()
    query = "SELECT"
    cursor.execute(query)
    output = cursor.fetchall()
    return output[0]
