import subprocess
import datetime
import requests
import time
import json
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
root_dir = os.path.dirname(parent_dir)  # Go up one more level to the project root
sys.path.insert(0, root_dir)
from sprites.display import show_sprite, SpriteWidget, QApplication
from pet_states.state_updater import update_pet_state, load_json, save_json

#TODO: make this a terminal process?
GIT_USERNAME = 'RachelBethke' #add rkb76 later
GIT_TOKEN = os.environ.get('GITHUB_TOKEN')
INTERVAL = 1 # sec between polling (?)
#GIT_TIKEN = {'rachelbethke' : 'GITHUB_TOKEN'}
MOCK_PUSH = False

if not GIT_TOKEN:
    print("Error: GIT_TOKEN is not properly connected.")
    print("Please set up your token using 'export GITHUB_TOKEN=your_personal_access_token' in the terminal.")
    sys.exit(1)

def get_last_push_real():
    """
    Getter to load the last push info from github
    """
    headers = { 'authorization' : f'token {GIT_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }
    url = f'https://api.github.com/users/{GIT_USERNAME}/events'
    #print(f"Requesting URL: {url}")
    #print(f"Using headers: {headers}")
    response = requests.get(url, headers=headers)
    #print(f"Response status code: {response.status_code}") 
    if response.status_code != 200:
        print(f"Error fetching events: {response.status_code}")
        print(f"Response content: {response.content}")
        return None
    events = response.json()
    for i in events:
        if i['type'] == 'PushEvent':
            return i #events (?)
    print("No PushEvent found")
    return None

def get_last_push_mock():
    """
    Mock push that return a simulated push for testing.
    """
    return {
        'id': str(int(time.time())),  # Unique ID based on current time
        'type': 'PushEvent',
        'repo': {'name': 'mock-repo'},
        'created_at': datetime.datetime.utcnow().isoformat() + 'Z',
    }

def get_last_push():
    """
    Choose between real and mock push implementation.
    """
    if MOCK_PUSH:
        print("Using mock push")
        return get_last_push_mock()
    else:
        print("Getting real push event from GitHub.")
        return get_last_push_real()

# def save_last_push():
#     """
#     Save the last processed push info to a file
#     """
#     pass
def watch_pushes(sprite_call):
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    sprite = SpriteWidget()
    sprite.hide()  # Start hidden
    last_event = None
    while True:
        event = get_last_push()
        if event and event['id'] != last_event:
            last_event = event['id']
            print(f"New push detected: {event}")
            sprite_call() 
        time.sleep(INTERVAL)
        
def process_push(push, un):
    """
    Process new push data to update current state file
    """
    pet_state = load_json('state_data/pet_state.json')
    last_event_id = None
    while True:
        event = get_last_push()
        if event and event['id'] != last_event_id:
            last_event_id = event['id']
            now = datetime.now().isoformat()
            pet_state['pushes'].append(now)
            pet_state['tokens'] += 1
            save_json('state_data/pet_state.json', pet_state)

        update_pet_state()
        time.sleep(INTERVAL)

def update_log():
    """ 
    Update git log on the INTERVAL (minute) to reflect state
    """
    pass

if __name__ == '__main__':
    watch_pushes(show_sprite)
