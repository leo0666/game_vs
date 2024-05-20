def Player(lang):
    from Trad.trad import load_translation

    messages = load_translation(lang)

    # class

    class PLAYER:
        def __init__(self, name, hp=100, damage_received=0, weapon=None, armor=None, power=None, healing=None):
            self.name = name
            self.total_hp = hp
            self.hp = hp
            self.damage_received = damage_received
            self.weapon = weapon
            self.armor = armor
            self.power = power
            self.healing = healing

        def Check_Percent_Hp(self, hp_remaining):
            total_hp = self.total_hp
            hp_begin = total_hp * 0.01
            hp_end = total_hp * 0.25

            if hp_begin <= hp_remaining <= hp_end:
                return True

            return False

        def Update_Hp(self, ARMOR):
            self.hp *= ARMOR.percent_hp_increase

        def Use_Healing(self, HEALING):
            hp_restored = self.total_hp
            hp_restored *= HEALING.percent_hp_restore if HEALING.usage_count > 0 and self.hp < self.total_hp else 0

            self.hp += hp_restored

            HEALING.usage_count -= 1

            message = f"{self.name} {messages["uses"]} {HEALING.name}, {hp_restored} {messages["hp_restored"]}"

            return message

        def Display_Info(self, WEAPON, AMMOTYPE, WEAPONMODE, ARMOR):
            print(
                f"\n{messages["stat_for"]} {self.name} :\n{messages["hp"]} : {self.hp:.2f}\n{messages["weapon"]} : {WEAPON.name}\n"
                f"{messages["ammo_type"]} : {AMMOTYPE.name if self.weapon.name != messages["no_weapon"] else messages["no_ammo"]}\n"
                f"{messages["mode"]} : {WEAPONMODE.name if self.weapon.name != messages["no_weapon"] else messages["no_mode"]}\n{messages["armor"]} : {ARMOR.name}")

        def Shoot(self, PLAYER):
            PLAYER.Receive_Damage(WEAPON=self.weapon)

        def Use_Power(self, PLAYER):
            PLAYER.Receive_Damage(POWER=self.power)
            PLAYER.Calculate_Damage(POWER=self.power)

            message = f"{self.name} {messages["uses"]} {self.power.name}, {self.power.damage} {messages["damage_on"]} {PLAYER.name}"

            return message

        def Receive_Damage(self, WEAPON=None, POWER=None):
            self.hp -= WEAPON.damage if WEAPON is not None else 0
            self.hp -= POWER.damage if POWER is not None else 0

        def Calculate_Damage(self, EVENT=None, PLAYER=None, POWER=None):
            self.damage_received += EVENT.damage if EVENT is not None else 0
            self.damage_received += PLAYER.weapon.damage if PLAYER is not None else 0
            self.damage_received += POWER.damage if POWER is not None else 0

            return self.damage_received

    return PLAYER
