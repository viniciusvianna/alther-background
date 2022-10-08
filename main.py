import model.connection.mydatabase as db


def main():
    # sk = Skill('SHEITS',
    #            'SHE',
    #            'Avatar',
    #            'intrinseca',
    #            'Shepians conseguem materializar seu espírito e atacar com ele. O '
    #             'espírito dos shepians causa 1d4 + E3 de dano espiritual em caso '
    #             'de sucesso no ataque e atormentam os inimigos, causando E5 de '
    #             'dano espiritual por 2 turnos subsequentes. O espírito dos '
    #             'shepians não pode ser atacado fisicamente, mas pode ser '
    #             'atingido por magia e possuem metade dos PV do shepian. Caso o '
    #              'espírito do shepian seja destruído, este fica atordoado por 3 '
    #              'turnos. Espíritos possuem movimento infinito em batalha.',
    #            0)
    # db.upload_new_skill(sk)

    skills = db.get_skills_by_category('intrinseca')
    for skill in skills:
        print(skill)


if __name__ == '__main__':
    main()
