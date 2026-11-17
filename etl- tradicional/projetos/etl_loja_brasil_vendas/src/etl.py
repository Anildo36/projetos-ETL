""" Pipeline ETL - Fluxo de execução """

from utils import importar_modulo

setup_dw = importar_modulo("00_setup_dw.py", "setup_dw")
extract = importar_modulo("01_extract.py", "extract")


def main():
    # Garantindo existência das camadas
    setup_dw.configurar_dw()

    # Extrair dados (E)
    extract.extracao_bd_loja_brasil()

    # Transformar dados (T)
    # processar_silver()

    # Carregar dados (L)
    # processar_gold()

    print("Pipeline ETL concluído.")


if __name__ == "__main__":
    main()