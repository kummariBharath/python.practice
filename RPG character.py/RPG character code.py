def create_character(name, strength, intelligence, charisma):
    


    # Name validations
    if not isinstance(name, str):
        return "The character name should be a string"

    if name == "":
        return "The character should have a name"

    if len(name) > 20:
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

    if strength > 20 or intelligence > 20  or charisma > 20:
        return "All stats should be no more than 20"

    if strength + intelligence + charisma > 20:
        return "The character should start with 20 points"

    # Output
    return (
        name + "\n"
        "STR " + "●" * strength + "○" * (20 - strength) + "\n"
        "INT " + "●" * intelligence + "○" * (20- intelligence) + "\n"
        "CHA " + "●" * charisma + "○" * (20 - charisma)
    )
if __name__ == "__main__":    #To control when code runs.
    try:
        name = input("Enter character name: ")
        strength = int(input("Enter strength (1-20): "))
        intelligence = int(input("Enter intelligence (1-20): "))
        charisma = int(input("Enter charisma (1-20): "))

        result = create_character(name, strength, intelligence, charisma)
        print("\nResult:\n")
        print(result)

    except ValueError:
        print("All stats should be integers")



