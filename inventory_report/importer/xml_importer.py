import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, arquivo: str):
        if not arquivo.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        with open(arquivo, "r") as file:
            content = file.read()
            parse = xmltodict.parse(content)
            data = parse["dataset"]["record"]

        return data
