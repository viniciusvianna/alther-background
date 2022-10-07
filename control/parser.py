import json

from model.basic.definition.action import Action
from model.basic.definition.race import Race
from model.basic.struc.attribute import Attribute
from model.basic.struc.dice import Dice
from model.character.character import Character
from model.character.charactions import CharActions
from model.character.charattributes import CharAttributes


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
    hit = create_action('acerto', det)
    evade = create_action('esquiva', det)
    defend = create_action('defesa', det)
    resist = create_action('resistencia', det)
    channel = create_action('artes', det)
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
        actions=char_actions
    )

    return char


def create_action(action, dictionary):
    dice = {d: Dice(n, int(d[1:])) for d, n in dictionary['acoes'][action].items()}
    return Action(action, dice)


def create_attribute(attr_name, dictionary):
    temp = dictionary['atributos'][attr_name]['temp']
    current = dictionary['atributos'][attr_name]['atual']
    total = dictionary['atributos'][attr_name]['total']
    train = dictionary['atributos'][attr_name]['treino']
    return Attribute(attr_name, total, current, temp, train)

