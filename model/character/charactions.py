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

        self._hit = hit
        self._evade = evade
        self._defend = defend
        self._resist = resist
        self._channel = channel

    def __str__(self):
        return f"Actions\n {self._hit}\n {self._evade}\n {self._defend}\n {self._resist}\n {self._channel}\n"

    def perform_action(self, action_name):
        if action_name == 'Acertar':
            action = self._hit
        elif action_name == 'Esquivar':
            action = self._evade
        elif action_name == 'Defender':
            action = self._defend
        elif action_name == 'Resistir':
            action = self._resist
        elif action_name == 'Canalizar':
            action = self._channel
        else:
            raise ValueError("No such action")

        return action.roll_action()

    def add_dice_to_action(self, action_name, dice):
        if action_name == 'Acertar':
            self._hit.add_dice(dice)
        elif action_name == 'Esquivar':
            self._evade.add_dice(dice)
        elif action_name == 'Defender':
            self._defend.add_dice(dice)
        elif action_name == 'Resistir':
            self._resist.add_dice(dice)
        elif action_name == 'Canalizar':
            self._channel.add_dice(dice)
        else:
            raise ValueError("No such action")
