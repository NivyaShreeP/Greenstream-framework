import os

def read_python_files(folder_path):
    code_files = {}

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                with open(full_path, "r", encoding="utf-8") as f:
                    code_files[full_path] = f.readlines()

    return code_files

