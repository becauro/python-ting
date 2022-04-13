# import re
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


# def check_word_in_file_data(word, file_data_list):
#     ocorrencias = []

#     for i in range(len(file_data_list)):
#         if re.search(file_data_list[i].lower(), word.lower()):
#             ocorrencias.append({"linha": i + 1})

#     return ocorrencias


if __name__ == "__main__":

    print(txt_importer("statics/arquivo_teste.txt"))
