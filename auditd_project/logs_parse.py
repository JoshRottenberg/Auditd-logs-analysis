from data_base import update_db
import sys
import re


def parser(event):
    cmd_name = re.search(r'key="([^"]+)"', event)
    user_name = re.search(r'UID="([^"]+)"', event)
    # TODO: extract the folder path (exe), if exist in event
    # folder_path =
    time_stamp = re.search(r'msg=autid\(([^:]+)', event)
    update_db(cmd_name, user_name, folder_path, time_stamp)


"""
TODO: A) make sure to run over all log files in directory in the first run, 
        afterwards only if has been changed
      B) make sure not to parser a line twice
"""


def read_log(log_path):
    regex = r'key="yrott_'
    try:
        with open(log_path, 'r') as auditd_log:
            lines = auditd_log.readlines()
            event = None
            for line in lines:
                if not event and re.search(regex, line):
                    event = line
                elif event and re.search(r'msg=audit\(([^"]+)', event) == re.search(r'msg=audit\(([^"]+)', line):
                    event = event + ' ' + line
                elif event:
                    event.rstrip('\n')
                    print(event)
                    # parser(event)
                    event = None
    except IOError:
        print(f'ERROR: opening file {log_path} \n')
