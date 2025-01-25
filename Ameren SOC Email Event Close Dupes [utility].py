"""
This playbook will be invoked at the end of our email main event.  It will look for events/cases that already exist based on a duplicate threatId from proofpoint, merge the duplicate event into the original event and close the new event as a duplicate
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'initialize' block
    initialize(container=container)

    return

def initialize(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("initialize() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.save_run_data(value="False", key='duplicate_event', auto=True)
    

    ################################################################################
    ## Custom Code End
    ################################################################################

    get_email_events_or_cases(container=container)

    return


def get_email_events_or_cases(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("get_email_events_or_cases() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    parameters = []

    parameters.append({
        "location": "/rest/container?_filter_label__in=[\"email_event_automation\"]&_filter_statu__name__in=[\"new\",\"open\",\"in+progress\"]",
        "verify_certificate": False,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("get data", parameters=parameters, name="get_email_events_or_cases", assets=["local rest"], callback=locate_duplicate_event)

    return


def locate_duplicate_event(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("locate_duplicate_event() called")

    id_value = container.get("id", None)
    label_value = container.get("label", None)
    get_email_events_or_cases_result_data = phantom.collect2(container=container, datapath=["get_email_events_or_cases:action_result.data.*.parsed_response_body.data"], action_results=results)
    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.threatID"])

    get_email_events_or_cases_result_item_0 = [item[0] for item in get_email_events_or_cases_result_data]
    container_artifact_cef_item_0 = [item[0] for item in container_artifact_data]

    locate_duplicate_event__duplicate_event_id = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    
    base_url = phantom.build_phantom_rest_url('artifact')
    
    
    events = get_email_events_or_cases_result_item_0[0] if get_email_events_or_cases_result_item_0 and len(get_email_events_or_cases_result_item_0) > 0 else []
    threatIds = list(item for item in container_artifact_cef_item_0 if item)
    threatId = threatIds[0] if len(threatIds) == 1 else None
    is_tap_click_alert = label_value == "tap_click_event_automation"
    
    phantom.debug(f'eval case threat ids: {threatId}')
    duplicate_event_id = None
    my_event_id = id_value
    
    if threatId and events:
        
        for event in events:
            # We do not want to match on our own event.
            if event and event.get('id') and event.get('id') != my_event_id:
                event_id = event.get('id')
                
                artifact_url = f'{base_url}?_filter_container_id={event_id}'
                #phantom.debug(f'sending req: {artifact_url}')
                
                response = phantom.requests.get(artifact_url, verify=False)
                
                if response.status_code == 200:
                    for artifact in response.json()['data']:
                        if artifact and artifact.get('cef'):
                            cef = artifact.get('cef')
                            #phantom.debug(f'eval match: {cef.get("threatID")} {threatId}')
                            if cef.get('threatID') and cef.get('threatID') == threatId:
                                #phantom.debug(f'Hit on duplicate artifact: {json.dumps(artifact, indent=4)} event_id: {event_id}')
                                duplicate_event_id = event_id
                                break
                                
                else:
                    phantom.error(f'HTTP Req failure getting artifacts for event_id: {event_id} Resp code: {response.status_code}')
                    
                    
    locate_duplicate_event__duplicate_event_id = duplicate_event_id
    
    if locate_duplicate_event__duplicate_event_id:
        # Save our duplicate_event state so we can return that this was indeed a duplicate
        phantom.save_run_data(value="True", key='duplicate_event', autom=True)
        phantom.debug(f'Found Dup Event: {locate_duplicate_event__duplicate_event_id}')
        

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="locate_duplicate_event:duplicate_event_id", value=json.dumps(locate_duplicate_event__duplicate_event_id))

    decision_1(container=container)

    return


def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("decision_1() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["locate_duplicate_event:custom_function:duplicate_event_id", "!=", ""]
        ])

    # call connected blocks if condition 1 matched
    if found_match_1:
        merge_into_duplicate(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 2
    join_set_return_results(action=action, success=success, container=container, results=results, handle=handle)

    return


def merge_into_duplicate(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("merge_into_duplicate() called")

    id_value = container.get("id", None)
    locate_duplicate_event__duplicate_event_id = json.loads(phantom.get_run_data(key="locate_duplicate_event:duplicate_event_id"))

    parameters = []

    parameters.append({
        "target_container": locate_duplicate_event__duplicate_event_id,
        "container_list": id_value,
        "workbook": "Scratch Workbook",
        "close_containers": False,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="phantom_pb_templates/ameren_container_merge", parameters=parameters, name="merge_into_duplicate", callback=close_case)

    return


def close_case(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("close_case() called")

    id_value = container.get("id", None)
    merge_into_duplicate__result = phantom.collect2(container=container, datapath=["merge_into_duplicate:custom_function_result.success"])
    locate_duplicate_event__duplicate_event_id = json.loads(phantom.get_run_data(key="locate_duplicate_event:duplicate_event_id"))

    merge_into_duplicate_success = [item[0] for item in merge_into_duplicate__result]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    
    success = merge_into_duplicate_success[0] if merge_into_duplicate_success else False
    target_event_id = locate_duplicate_event__duplicate_event_id
    event_id = id_value
    merged_event = container # Need to get our event.
    
    
    if success and merged_event and target_event_id:
        
        # status":"closes" "description":"Merged into case id: 333" "custom_fields":{"Impact":"None","Classification":"Child Event"}}:
        current_description = " -- " + merged_event.get('description') if merged_event.get('description') else ''
        
        phantom.debug(f'Current desc: {current_description}')
        
        update_data = {
            "status": "closed",
            "description": f'Duplicate event. Merged into event/case id: {target_event_id}' + current_description,
            "custom_fields": {
                "Impact": "None",
                "Classification": "Child Event"
            }
        }
        
        
        success, message = phantom.update(merged_event, update_data)
        
        if success:
            phantom.debug(f'Successfully closed case/event: {event_id}')
        else:
            phantom.error(f'Failed to close case/event: {event_id} Message Returned: {message}')
            

    ################################################################################
    ## Custom Code End
    ################################################################################

    join_set_return_results(container=container)

    return


def join_set_return_results(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("join_set_return_results() called")

    # if the joined function has already been called, do nothing
    if phantom.get_run_data(key="join_set_return_results_called"):
        return

    # save the state that the joined function has now been called
    phantom.save_run_data(key="join_set_return_results_called", value="set_return_results")

    # call connected block "set_return_results"
    set_return_results(container=container, handle=handle)

    return


def set_return_results(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("set_return_results() called")

    set_return_results__event_merged = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    duplicate_event = phantom.get_run_data(key='duplicate_event')
    
    phantom.debug(f'Value of duplicate event: {duplicate_event} {type(duplicate_event)}')
    
    set_return_results__event_merged = duplicate_event == "True"
    
    phantom.debug(f'Set Return results: {set_return_results__event_merged} {type(set_return_results__event_merged)}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="set_return_results:event_merged", value=json.dumps(set_return_results__event_merged))

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