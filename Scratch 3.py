"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'check_state' block
    check_state(container=container)

    return

def check_state(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("check_state() called")

    status_value = container.get("status", None)

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            [status_value, "==", "new"]
        ])

    # call connected blocks if condition 1 matched
    if found_match_1:
        handle_new_status(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'elif' condition 2
    found_match_2 = phantom.decision(
        container=container,
        conditions=[
            [status_value, "==", "open"]
        ])

    # call connected blocks if condition 2 matched
    if found_match_2:
        handle_open_status(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'elif' condition 3
    found_match_3 = phantom.decision(
        container=container,
        conditions=[
            [status_value, "==", "closed"]
        ])

    # call connected blocks if condition 3 matched
    if found_match_3:
        handle_closed_status(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 4
    handle_unknown_status(action=action, success=success, container=container, results=results, handle=handle)

    return


def handle_new_status(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("handle_new_status() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'Container status is New')

    ################################################################################
    ## Custom Code End
    ################################################################################

    set_status_to_open(container=container)

    return


def handle_open_status(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("handle_open_status() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'Container status is Open')

    ################################################################################
    ## Custom Code End
    ################################################################################

    set_status_to_closed(container=container)

    return


def handle_closed_status(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("handle_closed_status() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'Container status is Closed')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


def handle_unknown_status(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("handle_unknown_status() called")

    status_value = container.get("status", None)

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'Unknown container status: {status_value}')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


def set_status_to_open(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("set_status_to_open() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.set_status(container=container, status="open")

    container = phantom.get_container(container.get('id', None))

    return


def set_status_to_closed(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("set_status_to_closed() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.set_status(container=container, status="closed")

    container = phantom.get_container(container.get('id', None))

    return


def create_open_artifact(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("create_open_artifact() called")

    status_value = container.get("status", None)
    id_value = container.get("id", None)

    parameters = []

    parameters.append({
        "name": status_value,
        "tags": None,
        "label": None,
        "severity": None,
        "cef_field": "destinationAddress",
        "cef_value": "1.1.1.1",
        "container": id_value,
        "input_json": None,
        "cef_data_type": None,
        "run_automation": None,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    parameters = []

    parameters.append({
        "container": id_value,
        "name": status_value,
        "label": None,
        "severity": None,
        "cef_field": "destinationAddress",
        "cef_value": "1.1.1.1",
        "cef_data_type": None,
        "tags": None,
        "run_automation": "true",
        "input_json": None,
    })

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/artifact_create", parameters=parameters, name="create_open_artifact")

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