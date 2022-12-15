from collections import Counter
# from simple_report import SimpleReport
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, produtos):
        fabricacao_antiga = self._find_fabricacao_antiga(produtos)
        validade_proxima = self._find_validade_proxima(produtos)
        empresa_frequente = self._find_most_common(produtos, "nome_da_empresa")
        produtos_empresa = self._quant_produtos(produtos, "nome_da_empresa")

        return f"""Data de fabricação mais antiga: {fabricacao_antiga}
Data de validade mais próxima: {validade_proxima}
Empresa com mais produtos: {empresa_frequente}
Produtos estocados por empresa:
{produtos_empresa}"""

    @staticmethod
    def _quant_produtos(lista, filtro):
        texto = """"""
        empresas = [item[filtro] for item in lista]
        contagem = Counter(empresas).items()

        for empresa in contagem:
            nome, quant = empresa
            texto += f"- {nome}: {quant}\n"

        return texto
