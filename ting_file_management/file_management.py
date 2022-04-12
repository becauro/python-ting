def txt_importer(path_file):
    file_lines = []

    with open(path_file, mode="r") as file:
        for line in file:
            file_lines.append(line)

    return file_lines


if __name__ == "__main__":

    print(txt_importer("statics/arquivo_teste.txt"))
