from model.basic.definition.skill import Skill


class CharSkills:

    def __init__(self, available_skills: list,
                 intrinsic: Skill = None,
                 main1: Skill = None,
                 main2: Skill = None,
                 main3: Skill = None,
                 main4: Skill = None,
                 sup1: Skill = None,
                 sup2: Skill = None,
                 movement: Skill = None,
                 reaction: Skill = None,
                 perfect: Skill = None):
        if intrinsic is None:
            intrinsic = ""
        if main1 is None:
            main1 = ""
        if main2 is None:
            main2 = ""
        if main3 is None:
            main3 = ""
        if main4 is None:
            main4 = ""
        if sup1 is None:
            sup1 = ""
        if sup2 is None:
            sup2 = ""
        if movement is None:
            movement = ""
        if reaction is None:
            reaction = ""
        if perfect is None:
            perfect = ""

        self._available_skills = available_skills
        self._equipped_skills = {'intrinseca': intrinsic, 'padrao1': main1, 'padrao2': main2, 'padrao3': main3, 'padrao4': main4,
                                 'suporte1': sup1, 'suporte2': sup2, 'movimento': movement, 'reacao': reaction,
                                 'perfeita': perfect}

    def __str__(self):
        result = f"Skills:\n"
        for skill in self._equipped_skills.items():
            result += f"{skill[0]}: {skill[1]}\n"
        return result

    @property
    def available_skills(self):
        return self._available_skills

    @property
    def equipped_skills(self):
        return self._equipped_skills

    @property
    def intrinsic(self):
        return self._equipped_skills['intrinseca']

    @property
    def main1(self):
        return self._equipped_skills['padrao1']

    @property
    def main2(self):
        return self._equipped_skills['padrao2']

    @property
    def main3(self):
        return self._equipped_skills['padrao3']

    @property
    def main4(self):
        return self._equipped_skills['padrao4']

    @property
    def sup1(self):
        return self._equipped_skills['suporte1']

    @property
    def sup2(self):
        return self._equipped_skills['suporte2']

    @property
    def movement(self):
        return self._equipped_skills['movimento']

    @property
    def reaction(self):
        return self._equipped_skills['reacao']

    @property
    def perfect(self):
        return self._equipped_skills['perfeita']

    def learn_skill(self, skill):
        self._available_skills.append(skill)

    def unlearn_skill(self, skill):
        for s in self._available_skills:
            if s == skill:
                self._available_skills.remove(s)

    def equip_skill(self, slot, skill_id):
        for skill in self._available_skills:
            if skill.id_skill == skill_id:
                self._equipped_skills[slot] = skill



