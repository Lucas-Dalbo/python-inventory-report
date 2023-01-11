import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, arquivo: str):
        if not arquivo.endswith(".json"):
            raise ValueError("Arquivo inválido")

        with open(arquivo, "r") as file:
            content = file.read()
            data = json.loads(content)

        return data
