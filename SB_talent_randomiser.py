import random

while True:
    talents = {
        'Intelligent':
            {'tree': "mind", 'cost': 1},
        'Curious':
            {'tree': "mind", 'cost': 2},
        'Spellslinger':
            {'tree': "mind", 'cost': 2},
        'Tracking':
            {'tree': "mind", 'cost': 3},
        'Hardened':
            {'tree': "mind", 'cost': 3},
        'Runic Fluency':
            {'tree': "mind", 'cost': 4},
        'Rebirth':
            {'tree': "mind", 'cost': 4},
        'Tough':
            {'tree': "body", 'cost': 1},
        'Dexterity':
            {'tree': "body", 'cost': 2},
        'Wellspring':
            {'tree': "body", 'cost': 2},
        'Fellowship':
            {'tree': "body", 'cost': 3},
        'Vigor':
            {'tree': "body", 'cost': 3},
        'Ambidextrous':
            {'tree': "body", 'cost': 4},
        'Athletic':
            {'tree': "body", 'cost': 4},
        'Mystical':
            {'tree': "spirit", 'cost': 1},
        'Vampiric':
            {'tree': "spirit", 'cost': 2},
        'Thirsty':
            {'tree': "spirit", 'cost': 2},
        'Fortitude':
            {'tree': "spirit", 'cost': 3},
        'Inspired':
            {'tree': "spirit", 'cost': 3},
        'Foresight':
            {'tree': "spirit", 'cost': 4},
        'Gilded':
            {'tree': "spirit", 'cost': 4}
    }

    def unpack_tree(to_unpack, tree):
        unpacked_tree = {key: value for (key, value) in to_unpack.items() if value['tree'] == tree}
        return unpacked_tree


    def unpack_cost(to_unpack, cost):
        unpacked_cost = {key: value for (key, value) in to_unpack.items() if value['cost'] == cost}
        return unpacked_cost


    mind_talent = unpack_tree(talents, 'mind')
    body_talent = unpack_tree(talents, 'body')
    spirit_talent = unpack_tree(talents, 'spirit')

    first_roll = random.randint(0, 4)
    second_roll = random.randint(0, 4)

    MAX_SPEND = 7  # The cost of talents cannot exceed the MAX_SPEND otherwise the choices become incompatible
    remaining_spend = MAX_SPEND - (first_roll + second_roll)

    if remaining_spend >= 4:
        third_roll = random.randint(0, 4)

    else:
        third_roll = random.randint(0, remaining_spend)

    if first_roll == 0:
        mind_talent = "None"
    else:
        mind_talent = random.choice(list(unpack_cost(mind_talent, first_roll)))

    if second_roll == 0:
        body_talent = "None"
    else:
        body_talent = random.choice(list(unpack_cost(body_talent, second_roll)))

    if third_roll == 0:
        spirit_talent = "None"
    else:
        spirit_talent = random.choice(list(unpack_cost(spirit_talent, third_roll)))

    print("***Talents***")
    print(f"Mind: {mind_talent}\nBody: {body_talent}\nSpirit: {spirit_talent}\n")

    while True:
        answer = input("Roll again? (y/n): ")
        if answer in ('y', 'n'):
            break
        print('Invalid input')

    if answer == 'y':
        print("\n" + "*" * 29 + "\n")
        continue
    else:
        print('Cya, nerd')
        break
