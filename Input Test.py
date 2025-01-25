"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'artifact_create_1' block
    artifact_create_1(container=container)

    return

def artifact_create_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("artifact_create_1() called")

    id_value = container.get("id", None)
    playbook_input_infection_date = phantom.collect2(container=container, datapath=["playbook_input:infection_date"])

    parameters = []

    # build parameters list for 'artifact_create_1' call
    for playbook_input_infection_date_item in playbook_input_infection_date:
        parameters.append({
            "container": id_value,
            "name": "dwell info",
            "label": None,
            "severity": None,
            "cef_field": "infection_date",
            "cef_value": playbook_input_infection_date_item[0],
            "cef_data_type": "*",
            "tags": None,
            "run_automation": None,
            "input_json": None,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/artifact_create", parameters=parameters, name="artifact_create_1")

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