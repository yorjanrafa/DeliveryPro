def service_type():
    return (
        ('Corto', 'Corto = 1.5'),
        ('Corto + acompañante', 'Corto + acompañante = 2.0'),
        ('Largo', 'Largo = 2.5'),
        ('Largo + acompañante', 'Largo + acompañante = 3.0'),
        ('Extra largo', 'Extra largo = 3.5'),
        ('Extra largo + acompañante', 'Extra largo + acompañante = 4.0'),

        ('Carro corto', 'Carro corto = 2.0'),
        ('Carro largo', 'Carro largo = 3.0'),
        ('Carro Extra largo', 'Carro Extra largo= 4.0'),

        ('Preferencial', 'Preferencial'),
    )


def service_type_amount(type):
    amount = {
        'Corto': 1.5,
        'Corto + acompañante': 2.0,
        'Largo': 2.5,
        'Largo + acompañante': 3.0,
        'Extra largo': 3.5,
        'Extra largo + acompañante': 4.0,

        'Carro corto': 2.0,
        'Carro largo': 3.0,
        'Carro Extra largo': 4.0,
    }
    return amount[type]


def service_type2():
    return (
        ('Delivery', 'Delivery'),
        ('Transporte', 'Transporte'),
    )
