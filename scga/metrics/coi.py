def calculate_coi(code_files):
    coi = 0

    for lines in code_files.values():
        for line in lines:
            line = line.strip().lower()

            if line.startswith("return") and "error" in line:
                coi += 1

            if "cache" in line or "reuse" in line:
                coi += 1

            if "select" in line and "*" not in line:
                coi += 1

    return coi

