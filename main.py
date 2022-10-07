import control.mydatabase as db


def main():
    char = db.get_character_by_id(3)
    print(char, char.name, char.race, char.height, char.actions, char.attributes)


if __name__ == '__main__':
    main()
