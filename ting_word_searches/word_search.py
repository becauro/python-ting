import re

# For manual test local
# from ting_file_management.file_process import process  # Just for test
# from queue import Queue  # Just for test

# sys.path.append("ting_file_management")
# For local evaluator
# from queue import Queue  # Just for test
# from ting_file_management.file_management import check_word_in_file_data


def check_word_in_file_data(word, file_data_list):
    ocorrencias = []

    for i in range(len(file_data_list)):
        # if re.search(file_data_list[i].lower(), word.lower()):
        # print(f"AQUII_2: {file_data_list[i]}")
        # print(f"MATCH: {re.search(word, file_data_list[i], re.IGNORECASE)}")

        # if re.search(f"{word}", file_data_list[i]):
        if re.search(word, file_data_list[i], re.IGNORECASE):
            ocorrencias.append({"linha": i + 1})

    return ocorrencias


def exists_word(word, instance):

    my_files_stats = []
    my_files_stats = instance.files_stats
    files_with_word = []
    match_lines_list = []

    for i in range(len(my_files_stats)):

        # for i in range(1):
        # print('Entrou no FOR..')
        match_lines_list = check_word_in_file_data(
            word, my_files_stats[i]["linhas_do_arquivo"]
        )
        # print(f"AQUII_1: {match_lines_list}")

        if len(match_lines_list) > 0:

            # print("IF do FOR")
            files_with_word.append(
                {
                    "palavra": word,
                    "arquivo": my_files_stats[i]["nome_do_arquivo"],
                    "ocorrencias": match_lines_list,
                }
            )
    # print(f"AQUII: {my_files_stats}")
    # print(f"OUTRA VAR AQUI: {files_with_word}")

    return files_with_word

    # {
    #     "palavra": "pedro",
    #     "arquivo": "statics/nome_pedro.txt",
    #     "ocorrencias": [{"linha": 1}, {"linha": 3}],
    # }


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


if __name__ == "__main__":

    pass
