def read_file_list(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(f"- {line.strip()}")
    except FileNotFoundError:
        print(f"The file '{filename}' could not be found.")