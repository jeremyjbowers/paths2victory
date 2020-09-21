from itertools import permutations

import ujson as json

import settings
import utils

def direction_test(cand, rating):
    if cand['condition'] == ">":
        if rating > 0:
            return True

    if cand['condition'] == "<":
        if rating < 0:
            return True

    return False


sheet = utils.get_sheet(settings.SHEET_ID, settings.SHEET_RANGE)

for cand in settings.CANDIDATES:
    states = [{
        "state": a['state'],
        "ev": int(a['ev']), 
        "pollclose": a['first_results'],
        "90pct12hrs": utils.x_to_bool(a['90pct12hr']), 
        "swing": utils.x_to_bool(a['swing2']), 
        "rating": int(a['rating'])
    } for a in sheet]

    swing = [a for a in states if a['swing'] == True]

    locked_states = [a for a in states if a['swing'] == False and direction_test(cand, a['rating'])]

    cand_evs = sum([a['ev'] for a in locked_states])

    paths = utils.elect_paths(swing, 270 - cand_evs)

    unique_paths = set([])

    for path in paths:
        path_evs = sum([p['ev'] for p in path]) + cand_evs
        states = sorted([f"{p['state']} ({p['ev']})" for p in path], key=lambda x: x[0])
        state_string = ", ".join(states)
        state_string = f"{path_evs}: {state_string}"
        unique_paths.add(state_string)

    parsed_paths = []

    for a in unique_paths:
        path_dict = {
            "evs": int(a.split(': ')[0]),
            "states": [{"state": z.split(" (")[0], "ev": int(z.split(" (")[1].replace(")", ""))} for z in a.split(": ")[1].split(", ")],
            "state_string": a.split(": ")[1]
        }
        path_dict['num_states'] = len(path_dict['states'])
        if path_dict['evs'] < 300:
            parsed_paths.append(path_dict)

    sorted_paths = sorted(parsed_paths, key=lambda x: x['num_states'])

    print(f"{cand['name']} has {cand_evs} locked-in EVs and {len(sorted_paths)} paths to victory")

    with open(f'{cand["slug"]}_paths.json', 'w') as writefile:
        writefile.write(json.dumps(sorted_paths, indent=4))