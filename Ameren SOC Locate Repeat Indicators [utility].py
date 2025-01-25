"""
This playbook should be run at the end of a main playbook.  It will look through indicators, and find indicators that have been seen in the past.  If an indicator has been seen 3 or more times, a HUD care will be created.
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'gather_all_indicators' block
    gather_all_indicators(container=container)

    return

def gather_all_indicators(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("gather_all_indicators() called")

    id_value = container.get("id", None)

    parameters = []

    parameters.append({
        "container": id_value,
        "artifact_ids_include": None,
        "indicator_types_include": "email,ip,domain,url,network",
        "indicator_types_exclude": None,
        "indicator_tags_include": None,
        "indicator_tags_exclude": None,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/indicator_collect", parameters=parameters, name="gather_all_indicators", callback=create_hud_cards_for_repeats)

    return


def create_hud_cards_for_repeats(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("create_hud_cards_for_repeats() called")

    id_value = container.get("id", None)
    gather_all_indicators_data_all_indicators = phantom.collect2(container=container, datapath=["gather_all_indicators:custom_function_result.data.all_indicators.*.cef_value"])

    gather_all_indicators_data_all_indicators___cef_value = [item[0] for item in gather_all_indicators_data_all_indicators]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    
    # https://splunksoar-apm.ameren.com/rest/ioc?value=www.wnd.com
    import hashlib
    import re
    
    # Local exclusion list.  If we end up with a lot of repeats,
    # we can build this into a global list for excluding and ease of maintenance.
    excluded_indicators = [
        'ameren.com'
    ]
    
    AMEREN_EMAIL_MATCH = re.compile('.*?@ameren.com', re.IGNORECASE)
    
    search_url = phantom.build_phantom_rest_url('ioc')
    
    # Dedup
    indicator_values = list(set(gather_all_indicators_data_all_indicators___cef_value)) if gather_all_indicators_data_all_indicators___cef_value else []
    
    # Filter out excluded
    indicator_values = list(indicator for indicator in indicator_values if not indicator.lower().strip() in excluded_indicators)
    
    # Filter out @ameren.com matches
    indicator_values = list(indicator for indicator in indicator_values if not AMEREN_EMAIL_MATCH.match(indicator))
    
    # phantom.debug(f'After filter: {json.dumps(indicator_values, indent=4)}')
    
    # We want to get a list of all open containers, and exclude them from indicator matches.  We really only want to find matches in closed cases.
    open_container_ids = []
    container_url = phantom.build_phantom_rest_url('container')
    params = {
        "_exclude_status":'"closed"',
        "page_size":0
    }
    
    container_response = phantom.requests.get(f'{container_url}', verify=False, params=params)
    
    if container_response.status_code == 200:
        open_containers = container_response.json()['data']
        open_container_ids = list(container.get('id') for container in open_containers if container)
        
    else:
        phantom.error(f'Failed to get list of open containers.  Resp Code: {container_response.status_code} url: {container_url}')
        
    repeat_indicators = {}
    
    phantom.debug(f'Open Container Ids for filters: {open_container_ids}')
    
    for value in indicator_values:
        
        params = {
            "value": value
        }
        
        #phantom.debug(f'making req: url: {search_url} params: {json.dumps(params, indent=4)}')
        response = phantom.requests.get(search_url, verify=False, params=params)
        
        
        if response.status_code == 200:
            
            containers = response.json()['data'] if response.json()['data'] else []
            
            # filter out any open containers
            containers = list(container for container in containers if not container.get('container_id') in open_container_ids and container.get('container_id') != id_value)
            
            phantom.debug(f'Located containers with matching indicator that are not open: {json.dumps(containers, indent=4)}')
            
            if len(containers) >= 2: # 2 or more closed containers that contain the indicator in our current case.
                
                # this indicator has been seen in 3 containers, including ours.
                repeat_indicators[value] = {
                    'count': len(containers),
                    'containers': containers
                }
                
                
            else:
                phantom.error(f'Received invalid response making call to /ioc for Value: {value} Resp Code: {response.status_code}')
                
        phantom.error(f'Repeat Indicators Located: {json.dumps(repeat_indicators, indent=4)}')
            
        if len(repeat_indicators) > 0:
            for indicator, value in repeat_indicators.items():
                count = value.get('count')
                phantom.debug(f'Create HUD Card for indicator: {indicator} count: {count}')
                message = f'Indicator Seen in {count} prior containers'
                
                # Building a unique identifier for the hud card so it will never repeat.
                indicator_md5 = hashlib.md5(indicator.encode()).hexdigest()
                
                
                phantom.pin(container=id_value, message=message, data=indicator, pin_type='card', pin_style='red', truncate=True, name=f'repeat_indicator_{indicator_md5}', trace=False)
                
                

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # This function is called after all actions are completed.
    # summary of all the action and/or all details of actions
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    ################################################################################
    ## Custom Code End
    ################################################################################

    return