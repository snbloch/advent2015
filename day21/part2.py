from itertools import combinations

gold_spent = None

# must have 1
weapons = {}
weapons['Dagger'] = {'cost': 8, 'damage': 4, 'armor': 0}
weapons['Shortsword'] = {'cost': 10, 'damage': 5, 'armor': 0}
weapons['Warhammer'] = {'cost': 25, 'damage': 6, 'armor': 0}
weapons['Longsword'] = {'cost': 40, 'damage': 7, 'armor': 0}
weapons['Greataxe'] = {'cost': 74, 'damage': 8, 'armor': 0}

# may have 0-1
armor = {}
armor['Leather'] = {'cost': 13, 'damage': 0, 'armor': 1}
armor['Chainmail'] = {'cost': 31, 'damage': 0, 'armor': 2}
armor['Splintmail'] = {'cost': 53, 'damage': 0, 'armor': 3}
armor['Bandedmail'] = {'cost': 75, 'damage': 0, 'armor': 4}
armor['Platemail'] = {'cost': 102, 'damage': 0, 'armor': 5}

# may have 0-2
rings = {}
rings['Damage +1'] = {'cost': 25, 'damage': 1, 'armor': 0}
rings['Damage +2'] = {'cost': 50, 'damage': 2, 'armor': 0}
rings['Damage +3'] = {'cost': 100, 'damage': 3, 'armor': 0}
rings['Defense +1'] = {'cost': 20, 'damage': 0, 'armor': 1}
rings['Defense +2'] = {'cost': 40, 'damage': 0, 'armor': 2}
rings['Defense +3'] = {'cost': 80, 'damage': 0, 'armor': 3}

possible_weapons = []
possible_armor = []
possible_rings = []
for w in list(combinations(weapons, 1)):
    possible_weapons.append(w)

for count in xrange(0,2):
    for a in list(combinations(armor, count)):
        possible_armor.append(a)

for count in xrange(0,3):
    for r in list(combinations(rings, count)):
        possible_rings.append(r)

for p_w in possible_weapons:
    for p_a in possible_armor:
        for p_r in possible_rings:
            for w in p_w:
                total_cost = weapons[w]['cost']
                total_damage = weapons[w]['damage']
                total_armor = weapons[w]['armor']
            for a in p_a:
                if armor.get(a) != None:
                    total_cost += armor[a]['cost']
                    total_damage += armor[a]['damage']
                    total_armor += armor[a]['armor']
            for r in p_r:
                if rings.get(r) != None:
                    total_cost += rings[r]['cost']
                    total_damage += rings[r]['damage']
                    total_armor += rings[r]['armor']

            boss = {'hp': 104, 'damage': 8, 'armor': 1}
            player = {'hp': 100, 'damage': 0, 'armor': 0}
            player['damage'] = total_damage
            player['armor'] = total_armor
            while player['hp'] > 0 and boss['hp'] > 0:
                if player['damage'] - boss['armor'] <= 0:
                    boss['hp'] -= 1
                else:
                    boss['hp'] -= player['damage'] - boss['armor']
                if boss['hp'] <= 0:
                    break
                if boss['damage'] - player['armor'] <= 0:
                    player['hp'] -= 1
                else:
                    player['hp'] -= boss['damage'] - player['armor']
                if player['hp'] <= 0:
                    break
            if boss['hp'] > 0:
                if gold_spent == None:
                    gold_spent = total_cost
                elif total_cost > gold_spent:
                    gold_spent = total_cost

print gold_spent
