from model.basic.struc.attribute import Attribute
from model.basic.struc.bonus import Bonus
from model.character.character import Character
from model.basic.struc.damage import Damage
from model.basic.struc.dice import Dice
from model.basic.definition.race import Race
from model.basic.definition.weapon import Weapon


def main():
    lang = ["Medio", "Nuu"]
    race = Race("Rae", "", "")
    char = Character(1, "Raeniel", race, "Valiant", "Desbravadores do Vazio", "Ofensor", 1.82, 80, 50, languages=lang)
    char.actions["hit"].add_dice(Dice(1, 20))
    char.actions["hit"].add_dice(Dice(4, 6))
    char.actions["hit"].show_all_dice()
    body = Attribute("Corpo", 12)
    char.attributes.change_attribute(body)
    print()
    char.show_attributes()
    print()
    char.show_actions()
    print()
    print(f"{char.name} rolled {char.actions['hit'].roll_action()} for {char.actions['hit'].name}")
    weapon = Weapon("ADGCMN", "Adaga Comum", "Laminas Curtas", damage=Damage(Dice(1, 6), Attribute("Corpo"), 1 / 4),
                    bonus=Bonus("Hit", Dice(1, 4)))
    char.equip_weapon(weapon, "hand1")
    print(weapon)
    print(f"{char.name} rolou {char.attack('hand1')} de dano")


if __name__ == '__main__':
    main()
