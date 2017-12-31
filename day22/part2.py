import random

minimum_mana_spent = None

spells = {}
spells['Magic Missile'] = {'cost': 53, 'damage': 4, 'armor': 0, 'healing': 0, 'turns': 0, 'mana': 0}
spells['Drain'] = {'cost': 73, 'damage': 2, 'armor': 0, 'healing': 2, 'turns': 0, 'mana': 0}
spells['Shield'] = {'cost': 113, 'damage': 0, 'armor': 7, 'healing': 0, 'turns': 6, 'mana': 0}
spells['Poison'] = {'cost': 173, 'damage': 3, 'armor': 0, 'healing': 0, 'turns': 6, 'mana': 0}
spells['Recharge'] = {'cost': 229, 'damage': 0, 'armor': 0, 'healing': 0, 'turns': 5, 'mana': 101}

game_count = 0
while game_count < 100000:
    total_cost = 0
    spells_active = {}
    boss = {'hp': 55, 'damage': 8, 'armor': 0}
    player = {'hp': 50, 'mana': 500, 'damage': 0, 'armor': 0}
    while player['hp'] > 0 and boss['hp'] > 0:
        player['hp'] -= 1
        if player['hp'] <= 0:
            player_wins = False
            break
        spells_expiring = []
        spell_chosen = None
        spells_available = spells.copy()
        for spell in spells_active:
            player['armor'] = spells[spell]['armor']
            boss['hp'] -= spells[spell]['damage']
            player['mana'] += spells[spell]['mana']
        for spell in spells_active:
            spells_active[spell] -= 1
            if spells_active[spell] == 0:
                spells_expiring.append(spell)
        for spell in spells_expiring:
            if spells[spell]['armor'] > 0:
                player['armor'] = 0
            del spells_active[spell]
        for spell in spells_active:
            del spells_available[spell]
        can_cast_spell = False
        for spell in spells_available:
            if player['mana'] >= spells[spell]['cost']:
                can_cast_spell = True
        if can_cast_spell == False:
            player_wins = False
            break
        while spell_chosen == None:
            spell_chosen = random.choice(spells_available.keys())
            if player['mana'] < spells[spell_chosen]['cost']:
                spell_chosen = None
        if spells[spell_chosen]['turns'] > 0:
            spells_active[spell_chosen] = spells[spell_chosen]['turns']
        player['mana'] -= spells[spell_chosen]['cost']
        total_cost += spells[spell_chosen]['cost']
        if spells[spell_chosen]['turns'] == 0:
            boss['hp'] -= spells[spell_chosen]['damage']
            player['hp'] += spells[spell_chosen]['healing']
        if boss['hp'] <= 0:
            if player['hp'] > 0:
                player_wins = True
                break
            else:
                player_wins = False
                break
        spells_expiring = []
        for spell in spells_active:
            if spells[spell]['armor'] > 0:
                player['armor'] = spells[spell]['armor']
            if spells[spell]['damage'] > 0:
                boss['hp'] -= spells[spell]['damage']
            if spells[spell]['mana'] > 0:
                player['mana'] += spells[spell]['mana']
        for spell in spells_active:
            spells_active[spell] -= 1
            if spells_active[spell] == 0:
                spells_expiring.append(spell)
        for spell in spells_expiring:
            if spells[spell]['armor'] > 0:
                player['armor'] = 0
            del spells_active[spell]
        if boss['hp'] <= 0:
            if player['hp'] > 0:
                player_wins = True
                break
            else:
                player_wins = False
                break
        if boss['damage'] - player['armor'] <= 0:
            player['hp'] -= 1
        else:
            player['hp'] -= boss['damage'] - player['armor']
        if player['hp'] <= 0:
            player_wins = False
            break
    if player_wins == True:
        if minimum_mana_spent == None:
            minimum_mana_spent = total_cost
        elif total_cost < minimum_mana_spent:
            minimum_mana_spent = total_cost
    game_count += 1

print minimum_mana_spent
