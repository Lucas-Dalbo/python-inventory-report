from collections.abc import Iterable
from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer: Importer):
        self.importer = importer
        self.data = []
        self.__report_types = {
            "simples": SimpleReport,
            "completo": CompleteReport
        }

    def import_data(self, arquivo: str, rep_type: str):
        data = self.importer.import_data(arquivo)
        for item in data:
            self.data.append(item)

        return self.__report_types[rep_type].generate(data)

    def __iter__(self):
        return InventoryIterator(self.data)
