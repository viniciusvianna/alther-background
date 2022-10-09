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
                 mov: Skill = None,
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
        if mov is None:
            mov = ""
        if reaction is None:
            reaction = ""
        if perfect is None:
            perfect = ""

        self._available_skills = available_skills
        self._equipped_skills = {'intrinsic': "", 'main1': "", 'main2': "", 'main3': "", 'main4': "",
                                 'sup1': "", 'sup2': "", 'mov': "", 'reaction': "",
                                 'perfect': ""}
        self.equip_skill('intrinsic', intrinsic)
        self.equip_skill('main1', main1)
        self.equip_skill('main2', main2)
        self.equip_skill('main3', main3)
        self.equip_skill('main4', main4)
        self.equip_skill('sup1', sup1)
        self.equip_skill('sup2', sup2)
        self.equip_skill('mov', mov)
        self.equip_skill('reaction', reaction)
        self.equip_skill('perfect', perfect)

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
        return self._equipped_skills['intrinsic']

    @property
    def main1(self):
        return self._equipped_skills['main1']

    @property
    def main2(self):
        return self._equipped_skills['main2']

    @property
    def main3(self):
        return self._equipped_skills['main3']

    @property
    def main4(self):
        return self._equipped_skills['main4']

    @property
    def sup1(self):
        return self._equipped_skills['sup1']

    @property
    def sup2(self):
        return self._equipped_skills['sup2']

    @property
    def movement(self):
        return self._equipped_skills['mov']

    @property
    def reaction(self):
        return self._equipped_skills['reaction']

    @property
    def perfect(self):
        return self._equipped_skills['perfect']

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
                return
            else:
                self._equipped_skills[slot] = ""



