def load_translation(lang):
    if lang == 'FR':
        from Trad.trad_fr import messages
    else:
        from Trad.trad_en import messages

    return messages
