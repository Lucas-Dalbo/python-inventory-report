import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    __report_types = {
      "simples": SimpleReport,
      "completo": CompleteReport
    }

    @classmethod
    def import_data(cls, arquivo: str, rep_type: str):
        with open(arquivo, "r") as file:
            data = []
            if arquivo.endswith(".csv"):
                content = csv.DictReader(file, delimiter=",", quotechar='"')
                data = [row for row in content]
            elif arquivo.endswith(".json"):
                content = file.read()
                data = json.loads(content)
            elif arquivo.endswith(".xml"):
                content = file.read()
                parse = xmltodict.parse(content)
                data = parse["dataset"]["record"]
        return cls.__report_types[rep_type].generate(data)
