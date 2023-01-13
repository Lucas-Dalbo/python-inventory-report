import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    file_types = {
        "xml": XmlImporter,
        "csv": CsvImporter,
        "son": JsonImporter
    }

    if sys.argv.__len__() != 3:
        return print("Verifique os argumentos", file=sys.stderr)

    unused, file, rep_type = sys.argv
    file_type = file[-3:]
    inventario = InventoryRefactor(file_types[file_type])
    data = inventario.import_data(file, rep_type)

    return print(data, end='')
