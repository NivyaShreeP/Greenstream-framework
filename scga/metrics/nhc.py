def calculate_nhc(code_files):
    max_depth = 0

    for lines in code_files.values():
        current_depth = 0

        for line in lines:
            line = line.strip()

            if line.startswith(("if ", "elif ", "else", "for ", "while ")):
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            else:
                current_depth = max(0, current_depth - 1)

    return max_depth

