from inventory_report.inventory.product import Product


def test_cria_produto():
    test_product = Product(
        "01",
        "Controle Remoto",
        "CCI",
        "22/04/2000",
        "indeterminada",
        "123456-ABC",
        "Não molhar."
    )

    assert test_product.id == "01"
    assert test_product.nome_do_produto == "Controle Remoto"
    assert test_product.nome_da_empresa == "CCI"
    assert test_product.data_de_fabricacao == "22/04/2000"
    assert test_product.data_de_validade == "indeterminada"
    assert test_product.numero_de_serie == "123456-ABC"
    assert test_product.instrucoes_de_armazenamento == "Não molhar."
