"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'prompt_user_for_case_event_id' block
    prompt_user_for_case_event_id(container=container)

    return

def prompt_user_for_case_event_id(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("prompt_user_for_case_event_id() called")

    # set user and message variables for phantom.prompt call

    user = "brian"
    
    import custom_functions.Global_Util as utils
    user = utils.current_playbook_run_username()
    message = """Please provide that target case/event ID that the selected events/cases will be merged into.\n"""

    # parameter list for template variable replacement
    parameters = [
        "artifact:*.cef.app"
    ]

    # responses
    response_types = [
        {
            "prompt": "Target Case/Event ID",
            "options": {
                "type": "message",
            },
        }
    ]

    phantom.prompt2(container=container, user=user, message=message, respond_in_mins=30, name="prompt_user_for_case_event_id", parameters=parameters, response_types=response_types, callback=decision_1)

    return

def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("decision_1() called")

    id_value = container.get("id", None)

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        logical_operator="and",
        conditions=[
            ["prompt_user_for_case_event_id:action_result.summary.responses.0", "!=", ""],
            ["prompt_user_for_case_event_id:action_result.summary.responses.0", "!=", id_value]
        ])

    # call connected blocks if condition 1 matched
    if found_match_1:
        code_2(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 2
    code_1(action=action, success=success, container=container, results=results, handle=handle)

    return


def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'Else clause taken')

    ################################################################################
    ## Custom Code End
    ################################################################################

    return


def code_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("code_2() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(f'If clause taken')

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