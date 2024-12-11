import json
from datetime import datetime, timedelta

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def update_pet_state():
    pet_state = load_json('state_data/pet_state.json')
    config = load_json('state_data/config.json')
    now = datetime.now()
    last_updated = datetime.fromisoformat(pet_state['updated'])

    days_passed = (now-last_updated).days
    if days_passed > 0:
        pet_state['tokens'] = max(0, pet_state['tokens'] - days_passed)
        pet_state['updated'] = now.isoformat()

    one_day = now - timedelta(days=1)
    pet_state['pushes'] = [
        p for p in pet_state['pushes'] if datetime.fromisoformat(p) > one_day
    ]

    # update the state for loop (crazy!)
    for state, rules in config['states'].items():
        if (
            len(pet_state['pushes']) >= rules['min_pushes'] or
            pet_state['tokens'] >= rules['min_tokens'] and
            days_passed <= rules['max_days']
        ):
            pet_state['state'] = state
            break
    save_json('state_data/pet_state.json', pet_state)
