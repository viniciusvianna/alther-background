from model.basic.definition.action import Action


class CharActions:

    def __init__(self,
                 hit: Action = None,
                 evade: Action = None,
                 defend: Action = None,
                 resist: Action = None,
                 channel: Action = None):
        if hit is None:
            hit = Action("Acertar")
        if evade is None:
            evade = Action("Esquivar")
        if defend is None:
            defend = Action("Defender")
        if resist is None:
            resist = Action("Resistir")
        if channel is None:
            channel = Action("Canalizar")

        self._actions = {'hit': hit, 'evade': evade, 'defend': defend, 'resist': resist, 'channel': channel}

    def __str__(self):
        result = f"Actions:\n"
        for action in self._actions.items():
            result += f"{action[1]}\n"
        return result

    @property
    def hit(self):
        return self._actions['hit']

    @property
    def evade(self):
        return self._actions['evade']

    @property
    def defend(self):
        return self._actions['defend']

    @property
    def resist(self):
        return self._actions['resist']

    @property
    def channel(self):
        return self._actions['channel']

    def perform_action(self, action_type):
        return self._actions[action_type].roll_action()

    def add_dice_to_action(self, action_type, dice):
        self._actions[action_type].add_dice(dice)
