# Esta classe reúne os atributos do personagem para facilitar a construção da entidade personagem
# Ela também é responsável por encontrar o atributo correto para os métodos de outras classes como
# armas, dano, etc...
from model.basic.struc.attribute import Attribute


class CharAttributes:

    def __init__(self,
                 body: Attribute = None,
                 mind: Attribute = None,
                 focus: Attribute = None,
                 spirit: Attribute = None,
                 social: Attribute = None,
                 nature: Attribute = None):
        if body is None:
            body = Attribute("Corpo")
        if mind is None:
            mind = Attribute("Mente")
        if focus is None:
            focus = Attribute("Foco")
        if spirit is None:
            spirit = Attribute("Espírito")
        if social is None:
            social = Attribute("Social")
        if nature is None:
            nature = Attribute("Natureza")

        self._attributes = {'body': body, 'mind': mind, 'focus': focus, 'spirit': spirit, 'social': social, 'nature': nature}

    def __str__(self):
        result = f"Attributes:\n"
        for attribute in self._attributes.items():
            result += f"{attribute[1]}\n"
        return result

    @property
    def body(self):
        return self._attributes['body']

    @body.setter
    def body(self, new):
        self._attributes['body'] = new

    @property
    def mind(self):
        return self._attributes['mind']

    @mind.setter
    def mind(self, new):
        self._attributes['mind'] = new

    @property
    def focus(self):
        return self._attributes['focus']

    @focus.setter
    def focus(self, new):
        self._attributes['focus'] = new

    @property
    def spirit(self):
        return self._attributes['spirit']

    @spirit.setter
    def spirit(self, new):
        self._attributes['spirit'] = new

    @property
    def social(self):
        return self._attributes['social']

    @social.setter
    def social(self, new):
        self._attributes['social'] = new

    @property
    def nature(self):
        return self._attributes['nature']

    @nature.setter
    def nature(self, new):
        self._attributes['nature'] = new

    def match_attribute(self, attribute: Attribute):
        for attr in self._attributes:
            if attr == attribute:
                return attr
