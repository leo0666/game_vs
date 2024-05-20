def Power(lang):
    from Trad.trad import load_translation

    messages = load_translation(lang)

    # classes

    class POWER:
        def __init__(self, name, damage):
            self.name = name
            self.damage = damage

    class LIGHTNING(POWER):
        def __init__(self, name, damage=75):
            super().__init__(name, damage)

    # power program

    lightning = LIGHTNING(messages["name_lightning"])

    power_list = [lightning]

    return power_list
