import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, arquivo: str):
        if not arquivo.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        with open(arquivo, "r") as file:
            content = csv.DictReader(file, delimiter=",", quotechar='"')
            data = [row for row in content]

        return data
