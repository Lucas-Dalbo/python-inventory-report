from inventory_report.importer.importer import Importer


class InventoryRefactor():
    def __init__(self, importer: Importer):
        self.importer = importer
        self.data = []

    def load_data(self, arquivo: str):
        data = self.importer.import_data(arquivo)
        for item in data:
            self.data.append(item)
