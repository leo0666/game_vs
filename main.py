from Trad.trad import load_translation
from VS import vs
import os

os.system('cls' if os.name == 'nt' else 'clear')

lang = 'EN'
messages = load_translation(lang)
auto_name = 2  # auto_name false

while True:
    print(messages["fonct_consol"])

    try:
        opt = int(input(messages["q_fonct_consol"]))

        if opt == 1:
            os.system('cls' if os.name == 'nt' else 'clear')

            while True:
                print(messages["mode_fonct_consol"])

                try:
                    mode = int(input(messages["q_fonct_consol"]))

                    if mode == 1:
                        os.system('cls' if os.name == 'nt' else 'clear')

                        a = int(input(messages["vs_a"]))
                        b = int(input(messages["vs_b"]))

                        vs(lang, a, b, auto_name)

                    elif mode == 2:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break

                    elif mode == 3:
                        exit(0)

                    else:
                        print(messages["error_valide_number"])

                except ValueError:
                    print(messages["error_not_number"])

        elif opt == 2:
            os.system('cls' if os.name == 'nt' else 'clear')

            while True:
                print(messages["param_consol"])

                try:
                    param = int(input(messages["q_param_consol"]))

                    if param == 1:
                        os.system('cls' if os.name == 'nt' else 'clear')

                        while True:
                            print(messages["lang_option"])

                            try:
                                lang_option = int(input(messages["q_lang_option"]))

                                if lang_option == 1:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    lang = 'FR'
                                    messages = load_translation(lang)

                                elif lang_option == 2:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    lang = 'EN'
                                    messages = load_translation(lang)

                                elif lang_option == 3:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    break

                                elif lang_option == 4:
                                    exit(0)

                                else:
                                    print(messages["error_valide_number"])

                            except ValueError:
                                print(messages["error_not_number"])

                    elif param == 2:
                        os.system('cls' if os.name == 'nt' else 'clear')

                        while True:
                            print("\n" + messages["auto_name"])

                            try:
                                q_auto_name = int(input("\n" + messages["q_auto_name"]))

                                if q_auto_name == 1:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    auto_name = 1

                                elif q_auto_name == 2:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    auto_name = 2

                                elif q_auto_name == 3:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    break

                                elif q_auto_name == 4:
                                    exit(0)

                                else:
                                    print(messages["error_valide_number"])

                            except ValueError:
                                print(messages["error_not_number"])

                    elif param == 3:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break

                    elif param == 3:
                        exit(0)

                    else:
                        print(messages["error_valide_number"])

                except ValueError:
                    print(messages["error_not_number"])

        elif opt == 3:
            exit(0)

        else:
            print(messages["error_valide_number"])

    except ValueError:
        print(messages["error_not_number"])
