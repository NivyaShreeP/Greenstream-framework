def calculate_dlw(code_files):
    dlw = 0

    for lines in code_files.values():
        for line in lines:
            line = line.strip().lower()

            if "while true" in line:
                dlw += 2

            if line.startswith("for ") and "range" not in line:
                dlw += 1

            if line.startswith("while ") and "true" not in line:
                dlw += 1

    return dlw
