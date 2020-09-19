from itertools import permutations

import ujson as json

import settings
import utils


sheet = utils.get_sheet(settings.SHEET_ID, settings.SHEET_RANGE)

states = [{
    "state": a['state'],
    "ev": int(a['ev']), 
    "pollclose": a['first_results'],
    "90pct12hrs": utils.x_to_bool(a['90pct12hr']), 
    "swing": utils.x_to_bool(a['swing2']), 
    "rating": int(a['rating'])
 } for a in sheet]

swing = [a for a in states if a['swing'] == True]

for cand in settings.CANDIDATES:
    def direction_test(cand, rating):
        if cand['condition'] == ">":
            if rating > 0:
                return True

        if cand['condition'] == "<":
            if rating < 0:
                return True

        return False

    locked_states = [a for a in states if a['swing'] == False and direction_test(cand, a['rating'])]

    cand_evs = sum([a['ev'] for a in locked_states])

    print(f"{cand['name']} has {cand_evs} locked-in EVs")

    paths = utils.subset_sum(swing, 270 - cand_evs)

    payload = []

    for path in paths:
        payload.append(path)
        combo_string = f"{path[0]['state']} ({path[0]['ev']})"
        for state in path[1:]:
            combo_string += f", {state['state']} ({state['ev']})"

        evs = sum([p['ev'] for p in path]) + cand_evs
        print(f"Winning path: {cand['name']} {evs} EVs via {combo_string}")

    with open(f'{cand["slug"]}_paths.json', 'w') as writefile:
        writefile.write(json.dumps(payload))