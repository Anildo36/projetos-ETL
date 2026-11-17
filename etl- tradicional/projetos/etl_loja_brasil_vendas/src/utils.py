import importlib.util
from pathlib import Path

def importar_modulo(nome_arquivo, nome_modulo):
    caminho = Path(__file__).parent / nome_arquivo

    spec = importlib.util.spec_from_file_location(nome_modulo, caminho)

    modulo = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(modulo)

    return modulo