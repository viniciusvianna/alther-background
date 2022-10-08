import control.mydatabase as db


def main():
    skills = db.get_all_skills()
    for skill in skills:
        print(skill, skill.cost, 'PC')


if __name__ == '__main__':
    main()
