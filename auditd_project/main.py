from data_base import create_db
from logs_parse import read_log
from db_queries import *

""" assumption: auditd is installed and active (sudo systemctl status auditd)
rules are defined (sudo auditctl -l)"""


# TODO: add a config file (contain 64 bites, path to log files and db (regex pattern?!))

def main():
    # TODO: create db only if not exists- add check function
    create_db()
    read_log("/var/log/audit/audit.log")
    # execute queries
    print(num_of_commands())
    print(frequent_command())
    print(frequent_user())
    print(least_common_cmd)
    print(act_folder_path())
    print(num_of_entries())


if __name__ == "__main__":
    main()
