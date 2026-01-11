def calculate_fcl(code_files):
    fcl = 0
    inside_loop = False

    for lines in code_files.values():
        for line in lines:
            line = line.strip()

            if line.startswith(("for ", "while ")):
                inside_loop = True
                continue

            if inside_loop and "(" in line and ")" in line:
                fcl += 1

            if line == "" or line.startswith("#"):
                inside_loop = False

    return fcl

