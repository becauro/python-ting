import re


def check_word_in_file_data(word, file_data_list):
    ocorrencias = []

    for i in range(len(file_data_list)):
        if re.search(word, file_data_list[i], re.IGNORECASE):
            ocorrencias.append({"linha": i + 1})

    return ocorrencias


def exists_word(word, instance):

    my_files_stats = []
    my_files_stats = instance.files_stats
    files_with_word = []
    match_lines_list = []

    for i in range(len(my_files_stats)):

        match_lines_list = check_word_in_file_data(
            word, my_files_stats[i]["linhas_do_arquivo"]
        )

        if len(match_lines_list) > 0:

            files_with_word.append(
                {
                    "palavra": word,
                    "arquivo": my_files_stats[i]["nome_do_arquivo"],
                    "ocorrencias": match_lines_list,
                }
            )

    return files_with_word


def check_word_in_file_data_details(word, file_data_list):
    ocorrencias = []

    for i in range(len(file_data_list)):
        if re.search(word, file_data_list[i], re.IGNORECASE):
            ocorrencias.append({"linha": i + 1, "conteudo": file_data_list[i]})

    return ocorrencias


def search_by_word(word, instance):
    my_files_stats = []
    my_files_stats = instance.files_stats
    files_with_word = []
    match_lines_list = []

    for i in range(len(my_files_stats)):

        match_lines_list = check_word_in_file_data_details(
            word, my_files_stats[i]["linhas_do_arquivo"]
        )

        if len(match_lines_list) > 0:

            files_with_word.append(
                {
                    "palavra": word,
                    "arquivo": my_files_stats[i]["nome_do_arquivo"],
                    "ocorrencias": match_lines_list,
                }
            )

    return files_with_word

    # {
    #     "palavra": "pedro",
    #     "arquivo": "statics/nome_pedro.txt",
    #     "ocorrencias": [{"linha": 1}, {"linha": 3}],
    # }


if __name__ == "__main__":

    pass
