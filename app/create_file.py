from datetime import datetime
import os
import sys


cli_args = sys.argv[1:]
file_name = ""
dir_path = ""

if "-f" in cli_args:
    index_f = cli_args.index("-f")
    file_name = cli_args[index_f + 1]
    del cli_args[index_f:index_f + 2]
if "-d" in cli_args:
    dir_path = os.path.join(*cli_args[1:])
    os.makedirs(dir_path, exist_ok=True)

if file_name:
    user_data = []
    line_number = 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    user_data.append(timestamp)
    while True:
        text_line = input("Enter content line: ")
        if text_line == "stop":
            break
        user_data.append(f"{line_number} {text_line}\n")
        line_number += 1

    full_path = os.path.join(dir_path, file_name)
    with open(full_path, "a") as file:
        if os.path.getsize(full_path):
            file.write("\n")
        file.writelines(user_data)
