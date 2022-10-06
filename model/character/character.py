from model.basic.definition.action import Action
from model.basic.definition.weapon import Weapon
from model.basic.definition.race import Race


# Esta é a classe base que representa o personagem, sendo assim deve conter:
# Info básica que não envolve métodos: nome, raça, origem, escola, aspiração, altura, peso, idade e idiomas (v)
# Info básica que envolve métodos: nível, xp, pd, pv, am, ap, moeda (v)
# Atributos: corpo, mente, foco, espírito, social e natureza (v)
# Ações do personagem: acerto, esquiva, defesa, resistência e artes (v)
# Equipamentos: mão direita, mão esquerda, tronco (v)
# Efeitos: mão direita, mão esquerda, tronco, cabeça, pés, acessório (v)
# Caminhos: ativos e não ativos, pc
# Habilidades: intrínseca, padrão (x4), suporte (x2), movimento, reação e perfeita
# Inventário e Anotações
# Companheiro Animal
from model.character.charactions import CharActions
from model.character.charattributes import CharAttributes
from model.character.charequipments import CharEquipments


class Character:

    def __init__(self,
                 id_character: int,
                 name: str,
                 race: Race,
                 origin: str,
                 school: str,
                 aspiration: str,
                 height: float,
                 weight: float,
                 age: int,
                 languages=None,
                 level=1,
                 total_xp=0,
                 current_xp=-1,
                 pd=0,
                 total_pv=0,
                 current_pv=-1,
                 am=1,
                 ap=1,
                 coin="",
                 attributes=None,
                 actions=None,
                 equips=None):
        if languages is None:
            languages = ["Medio"]

        if actions is None:
            actions = CharActions()

        if attributes is None:
            attributes = CharAttributes()

        if equips is None:
            equips = CharEquipments()

        self._id_character = id_character
        self.name = name
        self.race = race
        self.origin = origin
        self.school = school
        self.aspiration = aspiration
        self.height = height
        self.weight = weight
        self.age = age
        self.languages = languages
        self.level = level
        self.total_xp = total_xp
        self.equips = equips

        if current_xp < 0:
            self.current_xp = total_xp
        else:
            self.current_xp = current_xp

        self.pd = pd
        self.total_pv = total_pv

        if current_pv < 0:
            self.current_pv = total_pv
        else:
            self.current_pv = current_pv

        self.am = am
        self.ap = ap
        self.coin = coin
        self.attributes = attributes
        self.actions = actions

    def __str__(self):
        return self.name

    def show_attributes(self):
        print(self.attributes)

    def show_actions(self):
        print(self.actions)

    def show_equipments(self):
        print(self.equips)

    def equip_weapon(self, weapon: Weapon, slot: str):
        attr = weapon.damage.attr
        weapon.equip(self.attributes.match_attribute(attr))
        self.equips.equip(weapon, slot)

    def attack(self, hand):
        equipment = self.equips.get_equipment(hand)
        if isinstance(equipment, Weapon):
            result = equipment.roll_damage()
        else:
            result = self.attributes.body.total_value / 4  # Ataque sem arma tem dano fixo de C4

        return result

    def act(self, action_name):
        self.actions.perform_action(action_name)
