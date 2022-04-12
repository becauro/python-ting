import sys

file_lines_without_n = []


def txt_importer(path_file):
    file_lines = []
    # file_lines_without_n = []

    if ".txt" not in path_file:
        return sys.stderr.write("Formato inválido\n")
    else:
        try:
            with open(path_file, mode="r") as file:
                for line in file:
                    file_lines.append(line)

            file_lines_without_n = "".join(file_lines).split("\n")
            return file_lines_without_n
        except Exception:
            sys.stderr.write(f"Arquivo {path_file} não encontrado\n")


if __name__ == "__main__":

    print(txt_importer("statics/arquivo_teste.txt"))
