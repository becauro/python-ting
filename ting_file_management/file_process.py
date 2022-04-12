import sys
# For local evaluator
# from ting_file_management.file_management import txt_importer

# For manual test local
from file_management import txt_importer


def process(path_file, instance):
    instance.enqueue(path_file)  # Instantiate file
    file_stats = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }

    instance.set_files_stats(file_stats)

    sys.stdout.write(
        str(
            file_stats
        )
    )


def remove(instance):
    removed = instance.dequeue()
    if removed is not None:
        sys.stdout.write(f"Arquivo {removed} removido com sucesso\n")
    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):

    try:
        node = instance.search(position)
        sys.stdout.write(
            str(
                {
                    "nome_do_arquivo": node,
                    "qtd_linhas": len(txt_importer(node)),
                    "linhas_do_arquivo": txt_importer(node),
                }
            )
        )
    except IndexError:
        sys.stderr.write("Posição inválida")
