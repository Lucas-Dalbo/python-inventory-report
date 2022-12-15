from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(self, produtos):
        fabricacao_antiga = min([item["data_de_fabricacao"]
                                for item in produtos])
        validade_proxima = self._find_validade_proxima(produtos)
        empresa_frequente = self._find_most_common(produtos, "nome_da_empresa")

        return f"""Data de fabricação mais antiga: {fabricacao_antiga}
Data de validade mais próxima: {validade_proxima}
Empresa com mais produtos: {empresa_frequente}"""

    def _find_most_common(lista, filtro):
        empresas = [item[filtro] for item in lista]
        mais_comum = Counter(empresas).most_common(1)[0]
        return mais_comum[0]

    def _find_validade_proxima(produtos):
        validades = []
        for item in produtos:
            validade = datetime.strptime(item["data_de_validade"], "%Y-%m-%d")
            if validade > datetime.now():
                validades.append(item["data_de_validade"])
        return min(validades)
