def calculate_rsi(code_files):
    rsi = 0

    for lines in code_files.values():
        for line in lines:
            line = line.strip().lower()

            # Penalize repeated resource acquisition
            if "connect(" in line:
                rsi += 1

            # Penalize open without close
            if "open(" in line and "close(" not in line:
                rsi += 1

    return rsi
