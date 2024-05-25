def vs(lang, nb_team, nb_player, auto_name):
    from Class.player import Player
    from Class.weapon import Weapon
    from Class.power import Power
    from Class.armor import Armor
    from Class.healing import Healing
    from Class.event import Event
    from Trad.trad import load_translation
    import random, os

    messages = load_translation(lang)
    PLAYER = Player(lang)
    weapon_list = Weapon(lang)
    power_list = Power(lang)
    armor_list = Armor(lang)
    healing_list = Healing(lang)
    event_list, program_error = Event(lang)

    total_player, p_no_weapon, i = nb_player, 1, 0
    teams, player_names, list_events_in_game = [[] for _ in range(nb_team)], [], []
    player_info_table, event_message, healing_message, power_message, target = "", "", "", "", ""

    for _ in range(total_player):
        player_name = input(f"\n{messages["enter_name_player"]} {_ + 1} : ") if auto_name == 2 else messages["auto_name_for"] + f"{_ + 1}"

        player = PLAYER(player_name)
        player.weapon = random.choice(weapon_list)
        player.power = random.choice(power_list)
        player.armor = random.choice(armor_list)
        player.healing = random.choice(healing_list)
        player.Update_Hp(player.armor)

        player_names.append(player.name)

        assigned = False
        while not assigned:
            t = random.randint(0, nb_team - 1)
            if len(teams[t]) < nb_player - (nb_team - 1):
                teams[t].append(player)
                player.team = t
                assigned = True

    for team in teams:
        if not team:
            random_team = random.choice([team for team in teams if len(team) >= 2])
            random_player = random_team.pop(random.randint(0, len(random_team) - 1))
            team.append(random_player)
            random_player.team = teams.index(team)

    max_name_length, min_name_length,  = max(len(name) for name in player_names), min(len(name) for name in player_names)

    for team in teams:
        for player in team:
            if player.weapon.name == messages["no_weapon"]:
                p_no_weapon += 1

                if p_no_weapon == total_player:
                    print(messages["warning_no_weapon"])

    while True:
        n = input(messages["pass_enter"])

        if n.lower() in [messages["pass"], ""]:
            break

        else:
            print(messages["error_pass_enter"])

    if n.lower() == messages["pass"]:

        while any(player.hp > 0 for team in teams for player in team):

            event = random.randint(1, 5)
            power = random.randint(1, 7)
            healing = random.randint(1, 10)
            program_error.Set_Damage(random.randint(1, 10 ** 50))

            if event == 3:
                event_message = random.choice(event_list).Inflict_Damage(random.choice([player for team in teams for player in team]))
                list_events_in_game.append(event_message)

            targets_this_round = set()

            for team in teams:
                for attacker in team:
                    if attacker.hp > 0:
                        target_teams = [t for t in teams if t != team and any(player.hp > 0 for player in t)]

                        if target_teams:
                            target_team = random.choice(target_teams)

                            alive_targets = [player for player in target_team if player.hp > 0 and player not in targets_this_round]

                            if alive_targets:
                                target = random.choice(alive_targets)
                                targets_this_round.add(target)

                                attacker.Shoot(target)
                                target.Calculate_Damage(PLAYER=attacker)

                                if target.Check_Percent_Hp(target.hp) or healing == 4:
                                    target.Use_Healing(target.healing)

                                if power == 5:
                                    attacker.Use_Power(target)

            if all(player.hp <= 0 for team in teams for player in team):
                print(f"{messages["number_rounds"]}{i}\n\n{messages["number_events"]}{len(list_events_in_game)}"
                      f"{messages["event_list"]} : {messages["no_event"] if len(list_events_in_game) == 0 else ', '.join(str(event_) for event_ in list_events_in_game)}"
                      f"\n\n{messages["tableau_player"]}{' ' * (max_name_length - min_name_length)}{messages["tableau_team"]}    {messages["tableau_total_damage"]}\n{'-' * (max_name_length + 21)}")

                for team in teams:
                    for player in team:
                        player_info_table = f"{player.name}{' ' * (max_name_length - len(player.name) + 3)}{player.team}    {player.damage_received:.2f}"
                        print(f"{player_info_table}")

                for team in teams:
                    for player in team:
                        player.Display_Info(player.weapon, player.weapon.ammo_type, player.weapon.mode, player.armor)

                input(messages["press_enter"])
                os.system('cls' if os.name == 'nt' else 'clear')

            i += 1

    elif n == "":
        print(messages["initial_stat_player"])

        for team in teams:
            for player in team:
                player.Display_Info(player.weapon, player.weapon.ammo_type, player.weapon.mode, player.armor)

        input(messages["press_enter"])

        while any(player.hp > 0 for team in teams for player in team):
            print(f"\n{"=" * 50}")

            event = random.randint(1, 5)
            power = random.randint(1, 7)
            healing = random.randint(1, 10)
            program_error.Set_Damage(random.randint(1, 10 ** 50))

            if event == 3:
                event_message = random.choice(event_list).Inflict_Damage(random.choice([player for team in teams for player in team]))
                list_events_in_game.append(event_message)

            targets_this_round = set()

            for team in teams:
                for attacker in team:
                    if attacker.hp > 0:
                        target_teams = [t for t in teams if t != team and any(player.hp > 0 for player in t)]

                        if target_teams:
                            target_team = random.choice(target_teams)

                            alive_targets = [player for player in target_team if
                                             player.hp > 0 and player not in targets_this_round]

                            if alive_targets:
                                target = random.choice(alive_targets)
                                targets_this_round.add(target)

                                attacker.Shoot(target)
                                target.Calculate_Damage(PLAYER=attacker)

                                if target.Check_Percent_Hp(target.hp) or healing == 4:
                                    target.Use_Healing(target.healing)

                                if power == 5:
                                    attacker.Use_Power(target)

                        if target.hp <= 0:
                            print(f"{target.name} {messages["has_died"]}")

            if any(player.hp > 0 for team in teams for player in team):
                print(f"\n{messages["round"]}{i}{"\n" * 2 if event_message != "" else "\n"}{event_message}{"\n" * 2 if power_message != "" else ""}{power_message}"
                      f"{"\n" * 2 if healing_message != "" else ""}{healing_message}{"\n" * 2 if healing_message != "" else ""}"
                      f"\n{messages["tableau_player"]}{' ' * (max_name_length - min_name_length)}{messages["tableau_damage_HP"]}\n{'-' * (max_name_length + 35)}")

                for team in teams:
                    for player in team:
                        player_info_table = f"{player.name}{' ' * (max_name_length - len(player.name) + 3)}{player.damage_received:.2f}{' ' * (17 - len(str(player.damage_received)))}{player.hp:.2f}"
                        print(f"{player_info_table}")

                for i, team in enumerate(teams, start=1):
                    if i == 1:
                        print(f"\n{i}. Team {i}")

                    else:
                        print(f"{i}. Team {i}")

                    if i == len(teams):
                        print(f"{i + 1}. tous les joueurs\n")

                players_stat_team = int(input(messages["message_view_stat"]))

                while True:
                    try:
                        if 1 <= players_stat_team <= len(teams) + 2:
                            if players_stat_team == len(teams) + 1:
                                for team in teams:
                                    for player in team:
                                        if player.hp > 0:
                                            player.Display_Info(player.weapon, player.weapon.ammo_type, player.weapon.mode, player.armor)
                                break
                            else:
                                for player in teams[players_stat_team - 1]:
                                    if player.hp > 0:
                                        player.Display_Info(player.weapon, player.weapon.ammo_type, player.weapon.mode, player.armor)
                                break

                    except:
                        print(messages["error_valide_number"])

                input(messages["press_enter"])

            elif all(player.hp <= 0 for team in teams for player in team):
                # {player1.name if player1.hp <= 0 else player2.name}{messages["has_died"]}{"\n" * 2}
                print(
                    f"{messages["number_rounds"]}{i}{"\n" * 2}{messages["number_events"]}{len(list_events_in_game)}\n{messages["event_list"]}"
                    f" : {messages["no_event"] if len(list_events_in_game) == 0 else ', '.join(str(event_) for event_ in list_events_in_game)}"
                    f"{"\n" * 2}{messages["tableau_player"]}{' ' * (max_name_length - min_name_length)}{messages["tableau_team"]}    {messages["tableau_total_damage"]}\n{'-' * (max_name_length + 21)}")

                for team in teams:
                    for player in team:
                        player_info_table = f"{player.name}{' ' * (max_name_length - len(player.name) + 3)}{player.team}    {player.damage_received:.2f}"
                        print(f"{player_info_table}")

                for team in teams:
                    for player in team:
                        player.Display_Info(player.weapon, player.weapon.ammo_type, player.weapon.mode, player.armor)

                input(messages["press_enter"])
                os.system('cls' if os.name == 'nt' else 'clear')

            i += 1
