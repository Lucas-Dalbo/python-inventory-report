from inventory_report.inventory.product import Product


def test_relatorio_produto():
    test_product = Product(
        "01",
        "Chocolate",
        "Racta",
        "22-04-2000",
        "22-04-2001",
        "123456-ABC",
        "lugar fresco e arejado"
    )

    report = test_product.__repr__()

    assert report == "O produto Chocolate fabricado em 22-04-2000 por Racta com validade até 22-04-2001 precisa ser armazenado lugar fresco e arejado."
