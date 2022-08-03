from character import Character
from dice import Dice


def main():
    char = Character("Raeniel")
    char.actions["hit"].add_dice(Dice(1, 20))
    char.actions["hit"].add_dice(Dice(4, 6))
    char.actions["hit"].show_all_dice()
    print()
    char.show_attributes()
    print()
    char.show_actions()
    print()
    print(f"{char.name} rolled {char.actions['hit'].roll_action()} for {char.actions['hit'].name}")


if __name__ == '__main__':
    main()
