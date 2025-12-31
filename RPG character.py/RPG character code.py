def create_character(name, strength, intelligence, charisma):
    name =input("Enter character name: ")
    strength =int(input("Enter strength (1-4): "))
    intelligence =int(input("Enter intelligence (1-4):"))
    charisma =int(input("Enter charisma (1-4): "))
    return create_character(name, strength, intelligence, charisma)

    # Name validations
    if not isinstance(name, str):
        return "The character name should be a string"

    if name == "":
        return "The character should have a name"

    if len(name) > 10:
        return "The character name is too long"

    if " " in name:
        return "The character name should not contain spaces"

    # Stats validations
    if not (
        isinstance(strength, int)
        and isinstance(intelligence, int)
        and isinstance(charisma, int)
    ):
        return "All stats should be integers"

    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"

    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"

    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

    # Output
    return (
        name + "\n"
        "STR " + "●" * strength + "○" * (10 - strength) + "\n"
        "INT " + "●" * intelligence + "○" * (10 - intelligence) + "\n"
        "CHA " + "●" * charisma + "○" * (10 - charisma)
    )
