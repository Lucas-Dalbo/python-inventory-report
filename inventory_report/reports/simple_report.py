from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(produtos):
        fabricacao_antiga = min([item["data_de_fabricacao"]for item in produtos])
        validade_proxima = min([item["data_de_validade"]
                               for item in produtos
                               if datetime.strptime(item["data_de_validade"], "%Y-%m-%d") > datetime.now()])
        empresa_frequente = SimpleReport.__find_most_common(produtos, "nome_da_empresa")

        return f"""Data de fabricação mais antiga: {fabricacao_antiga}
Data de validade mais próxima: {validade_proxima}
Empresa com mais produtos: {empresa_frequente}"""

    @staticmethod
    def __find_most_common(lista, filtro):
        empresas = [item[filtro] for item in lista]
        mais_comum = Counter(empresas).most_common(1)[0]
        return mais_comum[0]

