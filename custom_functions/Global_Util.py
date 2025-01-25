def Global_Util(**kwargs):
    """
    DO NOT DELETE
    
    Returns a JSON-serializable object that implements the configured data paths:
        
    """
    ############################ Custom Code Goes Below This Line #################################

import json
import phantom.rules as phantom
import ipaddress

# Reloads this module when called to load new content
def reload_module(module):
    from importlib import reload
    reloaded_module = reload(module)

# Returns the username of the user who executed the current playbook run
def current_playbook_run_username():
    user_id = phantom.get_current_playbook_info()[0]['effective_user_id']
    user_url = 'https://127.0.0.1:9999/rest/ph_user/{0}'.format(user_id)
    response = phantom.requests.get(user_url, verify=False)
    if response.status_code == 200:
        try:
            content = json.loads(response.text)
            return content['username']
        except Exception as e:
            return("Exception thrown while getting username: {}".format(e))