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

        self._body = body
        self._mind = mind
        self._focus = focus
        self._spirit = spirit
        self._social = social
        self._nature = nature

    def __str__(self):
        return f"Attributes\n {self._body}\n {self._mind}\n {self._focus}\n {self._spirit}\n {self._social}\n {self._nature}\n"

    @property
    def body(self):
        return self._body

    @property
    def mind(self):
        return self._mind

    @property
    def focus(self):
        return self._focus

    @property
    def spirit(self):
        return self._spirit

    @property
    def social(self):
        return self._social

    @property
    def nature(self):
        return self._nature

    def match_attribute(self, attr: Attribute):
        if attr == self._body:
            return self._body
        elif attr == self._mind:
            return self._mind
        elif attr == self._focus:
            return self._focus
        elif attr == self._spirit:
            return self._spirit
        elif attr == self.social:
            return self._social
        elif attr == self._nature:
            return self._nature
        else:
            raise ValueError("Não existe este atributo para o personagem")

    def change_attribute(self, attr: Attribute):
        if attr == self._body:
            self._body = attr
        elif attr == self._mind:
            self._mind = attr
        elif attr == self._focus:
            self._focus = attr
        elif attr == self._spirit:
            self._spirit = attr
        elif attr == self.social:
            self._social = attr
        elif attr == self._nature:
            self._nature = attr
        else:
            raise ValueError("Não existe este atributo para o personagem")

