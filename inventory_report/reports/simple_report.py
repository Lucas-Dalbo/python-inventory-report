from datetime import datetime
from collections import Counter


def find_most_common(lista, filtro):
    empresas = [item[filtro] for item in lista]
    mais_comum = Counter(empresas).most_common(1)[0]
    return mais_comum[0]


def find_validade_proxima(produtos):
    validades = []
    for item in produtos:
        validade = datetime.strptime(item["data_de_validade"], "%Y-%m-%d")
        if validade > datetime.now():
            validades.append(item["data_de_validade"])
    return min(validades)


class SimpleReport:
    @staticmethod
    def generate(produtos):
        fabricacao_antiga = min([item["data_de_fabricacao"]
                                for item in produtos])
        validade_proxima = find_validade_proxima(produtos)
        empresa_frequente = find_most_common(produtos, "nome_da_empresa")

        return f"""Data de fabricação mais antiga: {fabricacao_antiga}
Data de validade mais próxima: {validade_proxima}
Empresa com mais produtos: {empresa_frequente}"""
