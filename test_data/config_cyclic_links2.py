x = {
    "layer1":
    {
        "links_list":
            [
                {
                    "column_name": "Размер НДС, ₽",
                    "links": ["Статус контракта", "Номер контракта (ГЗ)"],
                    "weights": [
                        [1, 2],
                        [1 / 2, 1]
                    ]
                 },
                {
                    "column_name": "Статус контракта",
                    "links": ["Размер НДС, ₽", "Номер контракта (ГЗ)"],
                    "weights": [
                        [1, 2],
                        [1 / 2, 1]
                    ]
                 }
             ],
    }

}
