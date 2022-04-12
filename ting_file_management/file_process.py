import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    instance.enqueue(path_file)

    sys.stdout.write(str({
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(txt_importer(path_file)),
            "linhas_do_arquivo": txt_importer(path_file)
    }))


def remove(instance):
    removed = instance.dequeue()
    if removed is not None:
        sys.stdout.write(f"Arquivo {removed} removido com sucesso\n")
    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
