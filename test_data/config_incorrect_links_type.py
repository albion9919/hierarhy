x = {
    "layer1":
    {
        "links_list":
            [
                {
                    "column_name": "Размер НДС, ₽",
                    "links": 1,
                    "weights": [
                        [1, 2],
                        [1 / 2, 1]
                    ]
                 },
                {
                    "column_name": "Цена контракта",
                    "links": ["Статус контракта", "Номер контракта (ГЗ)"],
                    "weights": [
                        [1, 2],
                        [1 / 2, 1]
                    ]
                 }
             ],
    }

}
