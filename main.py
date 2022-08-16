from model.attribute import Attribute
from model.bonus import Bonus
from model.character import Character
from model.damage import Damage
from model.dice import Dice
from model.race import Race
from model.weapon import Weapon


def main():
    lang = ["Medio", "Nuu"]
    race = Race("Rae", "", "")
    char = Character("Raeniel", race, "Valiant", "Desbravadores do Vazio", "Ofensor", 1.82, 80, 50, languages=lang)
    char.actions["hit"].add_dice(Dice(1, 20))
    char.actions["hit"].add_dice(Dice(4, 6))
    char.actions["hit"].show_all_dice()
    print()
    char.show_attributes()
    print()
    char.show_actions()
    print()
    print(f"{char.name} rolled {char.actions['hit'].roll_action()} for {char.actions['hit'].name}")
    weapon = Weapon("Adaga Comum", "Laminas Curtas", damage=Damage(Dice(1, 6), Attribute("Body"), 1/4), bonus=Bonus("Hit", Dice(1, 4)))
    char.equip_weapon(weapon, "Hand1")
    print(weapon)
    print(char.equips["Hand1"].damage.attr)
    print(f"{char.name} rolou {char.attack('Hand1')} de dano")


if __name__ == '__main__':
    main()
