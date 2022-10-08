import json

from model.basic.definition.accessory import Accessory
from model.basic.definition.action import Action
from model.basic.definition.armor import Armor
from model.basic.definition.path import Path
from model.basic.definition.race import Race
from model.basic.definition.skill import Skill
from model.basic.definition.weapon import Weapon
from model.basic.struc.attribute import Attribute
from model.basic.struc.damage import Damage
from model.basic.struc.dice import Dice
from model.character.characcessories import CharAccessories
from model.character.character import Character
from model.character.charactions import CharActions
from model.character.charattributes import CharAttributes
from model.character.charequipments import CharEquipments
from model.character.charpaths import CharPaths
from model.character.charskills import CharSkills


def parse_character_json(details, id_character):
    det = json.loads(details)

    # Basic character information
    name = det['nome_personagem']
    aspiration = det['aspiracao']['nome_aspiracao']
    movement_actions = det['AM']
    main_actions = det['AP']
    pd = det['PD']
    temp_pv = det['PV']['temp']
    current_pv = det['PV']['atual']
    total_pv = det['PV']['total']
    current_xp = det['XP']['atual']
    total_xp = det['XP']['total']
    height = det['altura']
    weight = det['peso']
    age = det['idade']
    coin = det['moeda']
    level = det['nivel']
    school = det['escola']['nome_escola']
    origin = det['origem']
    notes = det['anotacoes']
    inventory = det['inventario']

    # Race information
    race_name = det['raca']['nome_raca']
    race_restriction_name = det['raca']['nome_restricao_racial']
    race_restriction_desc = det['raca']['descricao_restricao_racial']
    race_ability_name = det['raca']['nome_habilidade_racial']
    race_ability_desc = det['raca']['descricao_habilidade_racial']
    race_ability = f"{race_ability_name}: {race_ability_desc}"
    race_restriction = f"{race_restriction_name}: {race_restriction_desc}"
    race = Race(race_name, race_ability, race_restriction)

    # Actions information
    hit = create_action('acertar', det)
    evade = create_action('esquivar', det)
    defend = create_action('defender', det)
    resist = create_action('resistir', det)
    channel = create_action('canalizar', det)
    char_actions = CharActions(hit, evade, defend, resist, channel)

    # Attributes information
    body = create_attribute('corpo', det)
    mind = create_attribute('mente', det)
    focus = create_attribute('foco', det)
    spirit = create_attribute('espirito', det)
    social = create_attribute('social', det)
    nature = create_attribute('natureza', det)
    char_attributes = CharAttributes(body, mind, focus, spirit, social, nature)

    # Equipment information
    hand1 = create_weapon('mao_direita', det)
    hand2 = create_weapon('mao_esquerda', det)
    body_equip = create_armor(det)
    char_equipments = CharEquipments(hand1, hand2, body_equip)

    # Accessory information
    hands = create_accessory('maos', det)
    body_acc = create_accessory('tronco', det)
    head_acc = create_accessory('cabeca', det)
    feet_acc = create_accessory('pes', det)
    char_accessories = CharAccessories(hands, body_acc, head_acc, feet_acc)

    # Paths information
    paths = [create_path(dic) for dic in det['caminhos_disponiveis']]
    active_path = det['caminho_ativo']
    char_paths = CharPaths(paths, active_path)

    # Skills information
    skills = [create_skill(dic) for dic in det['habilidades_adquiridas']]
    equipped_skills = {slot: value for slot, value in det['habilidades_equipadas'].items() if value != ""}
    char_skills = CharSkills(skills)
    for skill in equipped_skills.items():
        char_skills.equip_skill(skill[0], skill[1])

    # Create character
    char = Character(
        id_character=id_character,
        name=name,
        race=race,
        origin=origin,
        school=school,
        aspiration=aspiration,
        height=height,
        weight=weight,
        age=age,
        level=level,
        total_xp=total_xp,
        current_xp=current_xp,
        pd=pd,
        total_pv=total_pv,
        current_pv=current_pv,
        temp_pv=temp_pv,
        am=movement_actions,
        ap=main_actions,
        coin=coin,
        attributes=char_attributes,
        actions=char_actions,
        equips=char_equipments,
        accessories=char_accessories,
        paths=char_paths,
        skills=char_skills,
        notes=notes,
        inventory=inventory
    )

    return char


def parse_skill(response):
    id_skill, name_skill, category, description, cost, id_path = response
    return Skill(id_skill, id_path, name_skill, category, description, cost)


def create_action(action, dictionary):
    dice = {d: Dice(n, int(d[1:])) for d, n in dictionary['acoes'][action].items()}
    return Action(action, dice)


def create_attribute(attr_name, dictionary):
    temp = dictionary['atributos'][attr_name]['temp']
    current = dictionary['atributos'][attr_name]['atual']
    total = dictionary['atributos'][attr_name]['total']
    train = dictionary['atributos'][attr_name]['treino']
    return Attribute(attr_name, total, current, temp, train)


def create_weapon(slot, dictionary):
    id_weapon = dictionary['equipamentos'][slot]['id_equipamento']
    if id_weapon == '':
        return None
    name_weapon = dictionary['equipamentos'][slot]['nome_equipamento']
    bonus_weapon = dictionary['equipamentos'][slot]['dados_equipamento']
    damage_weapon = Damage.from_string(bonus_weapon['dano'])
    category_weapon = dictionary['equipamentos'][slot]['categoria']
    effect_weapon = dictionary['equipamentos'][slot]['efeito_equipamento']
    return Weapon(id_equipment=id_weapon, name=name_weapon, bonus=bonus_weapon, effect=effect_weapon,
                  damage=damage_weapon, category=category_weapon)


def create_armor(dictionary):
    id_armor = dictionary['equipamentos']['tronco']['id_equipamento']
    if id_armor == '':
        return None
    name_armor = dictionary['equipamentos']['tronco']['nome_equipamento']
    bonus_armor = dictionary['equipamentos']['tronco']['dados_equipamento']
    category_armor = dictionary['equipamentos']['tronco']['categoria']
    effect_armor = dictionary['equipamentos']['tronco']['efeito_equipamento']
    return Armor(id_equipment=id_armor, name=name_armor, bonus=bonus_armor, effect=effect_armor,
                 category=category_armor)


def create_accessory(slot, dictionary):
    id_accessory = dictionary['acessorios'][slot]['id_acessorio']
    if id_accessory == '':
        return None
    name_accessory = dictionary['acessorios'][slot]['nome_acessorio']
    effect_accessory = dictionary['acessorios'][slot]['efeito_acessorio']
    return Accessory(id_equipment=id_accessory, name=name_accessory, effect=effect_accessory, slot=slot)


def create_path(dictionary):
    id_path = dictionary['id_caminho']
    name_path = dictionary['nome_caminho']
    tier_path = dictionary['tier']
    level_path = dictionary['nivel']
    total_pc = dictionary['PC']['total']
    current_pc = dictionary['PC']['atual']
    master = dictionary['mestre']
    return Path(id_path=id_path, name_path=name_path, tier=tier_path, level=level_path, total_pc=total_pc,
                current_pc=current_pc, master=master)


def create_skill(dictionary):
    id_skill = dictionary['id_habilidade']
    id_path = dictionary['id_caminho']
    category = dictionary['categoria']
    name_skill = dictionary['nome_habilidade']
    desc_skill = dictionary['descricao_habilidade']
    return Skill(id_skill=id_skill, id_path=id_path, category=category, name_skill=name_skill, description=desc_skill)

