def calculate_cic(code_files):
    cic = 0

    for lines in code_files.values():
        for line in lines:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if "=" in line and "==" not in line:
                cic += 1

            if "(" in line and ")" in line:
                cic += 1

            for op in ["+", "-", "*", "/"]:
                if op in line:
                    cic += 1

    return cic

