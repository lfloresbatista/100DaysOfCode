PLACEHOLDER = "[name]"


with open("./Input/Letters/starting_letter.txt") as letter:
    def_letter = letter.read()
    with open("./Input/Names/invited_names.txt") as names:
        for new_name in names:
            new_name = new_name.strip()
            new_letter = def_letter.replace(PLACEHOLDER, new_name)
            with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as final_letter:
                final_letter.write(new_letter)



