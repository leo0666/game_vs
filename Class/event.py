def Event(lang):
    from Trad.trad import load_translation
    import random

    messages = load_translation(lang)

    # class
    class EVENT:
        def __init__(self, name, damage):
            self.name = name
            self.damage = damage

        def Inflict_Damage(self, PLAYER):
            PLAYER.Calculate_Damage(EVENT=self)
            PLAYER.hp -= self.damage
            message = f"{self.name} {messages["inflicts"]} {self.damage} {messages["damage_to"]} {PLAYER.name}"

            return message

        def Set_Damage(self, value):
            self.damage = value

    class STORM(EVENT):
        def __init__(self, name, damage=50):
            super().__init__(name, damage)

    class PROGRAMERROR(EVENT):
        def __init__(self, name, damage=0):  # variable damage
            super().__init__(name, damage)

    # EVENT program

    storm = STORM(messages["name_event_storm"])
    program_error = PROGRAMERROR(messages["name_event_program_error"])

    event_list = [storm, program_error]

    random.shuffle(event_list)

    return event_list, program_error
